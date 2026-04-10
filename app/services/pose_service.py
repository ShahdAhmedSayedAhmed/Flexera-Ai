import cv2
import numpy as np
import base64

import app.state as state
from app.core.exercise_rules import ERROR_RULES
from app.core.exercise_validator import ExerciseState
from app.models.session import ExerciseSession


def decode_base64_frame(image_base64: str) -> np.ndarray:
    img_bytes = base64.b64decode(image_base64)
    nparr = np.frombuffer(img_bytes, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if frame is None:
        raise ValueError("Failed to decode image")
    return frame


def _build_joint_angles(session: ExerciseSession, keypoints: np.ndarray,
                        active_side: str, primary_angle: float) -> dict:
    """
    Build the joint_angles dict expected by ExerciseCorrection.detect_errors().

    The dict must contain:
      - "{side}_{primary_joint_name}" = primary joint angle
      - "{side}_{secondary_joint_name}" = secondary joint angle (computed from
        keypoints if the exercise has a secondary joint, e.g. knee straightness
        check in the straight-leg raise)

    Without this, the secondary-joint error check in exercise_correction.py
    would read the primary angle and compare it against secondary thresholds,
    producing wrong errors every frame.
    """
    rules = ERROR_RULES.get(session.exercise_key, {})
    primary_joint_name = rules.get('joint', 'knee')

    angles = {f"{active_side}_{primary_joint_name}": primary_angle}

    # Compute secondary joint angle from raw keypoints when needed
    secondary_joint_name = rules.get('secondary_joint')
    if secondary_joint_name:
        active_v = (session.validator.left_validator
                    if active_side == 'left'
                    else session.validator.right_validator)
        _, sec_indices = active_v.get_side_adjusted_indices(active_side)
        if sec_indices and active_v.check_keypoint_confidence(keypoints, sec_indices):
            sec_angle = float(active_v.calculate_angle(
                keypoints[sec_indices[0], :2],
                keypoints[sec_indices[1], :2],
                keypoints[sec_indices[2], :2],
            ))
            angles[f"{active_side}_{secondary_joint_name}"] = sec_angle

    return angles


def run_pose_and_validate(frame: np.ndarray, session: ExerciseSession) -> dict:
    results = state.pose_model(frame, verbose=False)

    if not results or len(results[0].keypoints.data) == 0:
        return {
            "success": False,
            "left_angle": 0.0,
            "right_angle": 0.0,
            "left_reps": 0,
            "right_reps": 0,
            "total_reps": session.validator.get_total_reps(),
            "is_valid": False,
            "feedback": "No person detected — please position yourself in the camera view",
            "active_side": "none",
            "state": "idle",
            "errors": [],
            "keypoints": None,
        }

    keypoints = results[0].keypoints.data[0].cpu().numpy()
    validation = session.validator.validate_frame(keypoints)

    left = validation["left"]
    right = validation["right"]
    active_side = "left" if left.rep_count >= right.rep_count else "right"
    active = validation[active_side]

    joint_angles = _build_joint_angles(
        session, keypoints, active_side, float(active.current_angle)
    )

    rep_state = "idle" if active.state == ExerciseState.INVALID else active.state.value

    feedback_result = session.correction.provide_feedback(
        exercise_name=session.exercise_key,
        joint_angles=joint_angles,
        current_rep_state=rep_state,
        is_valid_motion=active.is_valid,
        side=active_side,
    )

    errors_serialised = [
        {
            "type": e.error_type,
            "severity": e.severity,
            "recommendation": e.recommendation,
            "joint": e.joint_name,
            "current_value": round(e.current_value, 1),
        }
        for e in feedback_result.get("errors", [])
    ]

    return {
        "success": True,
        "left_angle": float(left.current_angle),
        "right_angle": float(right.current_angle),
        "left_reps": int(left.rep_count),
        "right_reps": int(right.rep_count),
        "total_reps": int(session.validator.get_total_reps()),
        "is_valid": bool(active.is_valid),
        "feedback": feedback_result.get("recommendation") or "Keep going!",
        "active_side": active_side,
        "state": rep_state,
        "errors": errors_serialised,
        "keypoints": keypoints.tolist(),
    }

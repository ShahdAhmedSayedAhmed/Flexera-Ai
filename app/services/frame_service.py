from app.models.session import ExerciseSession


def build_frame_response(session: ExerciseSession, raw: dict) -> dict:
    """
    Combine raw pose result with session progress into the final
    Flutter-ready FrameProcessResponse dict.
    """
    set_complete = session.check_set_complete()

    return {
        "success": raw["success"],
        "session_key": session.session_key,
        "current_reps": raw["total_reps"],
        "target_reps": session.target_reps,
        "current_set": session.current_set,
        "completed_sets": session.completed_sets,
        "target_sets": session.target_sets,
        "set_complete": set_complete,
        "exercise_complete": session.is_complete,
        "left_angle": raw["left_angle"],
        "right_angle": raw["right_angle"],
        "is_valid_form": raw["is_valid"],
        "feedback": raw["feedback"],
        "active_side": raw["active_side"],
        "rep_state": raw["state"],
        "keypoints": raw.get("keypoints"),
    }

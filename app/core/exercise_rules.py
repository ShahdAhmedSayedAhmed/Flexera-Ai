from dataclasses import dataclass
from typing import Tuple


@dataclass
class ErrorDetection:
    error_type: str
    severity: str
    recommendation: str
    joint_name: str
    current_value: float
    expected_range: Tuple[float, float]


# ─────────────────────────────────────────────────────────────────────────────
# CAMERA CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────

EXERCISE_CAMERA_CONFIG = {
    # Session 1 – lower body
    'bending_knee_no_support_seated_s1': {
        'focus_area': 'lower_body',
        'zoom_level': 0.6,
        'key_landmarks': [11, 12, 13, 14, 15, 16],
        'camera_hint': "Position camera at the side to show your full legs while seated",
    },
    'bending_knee_with_support_seated_s1': {
        'focus_area': 'lower_body',
        'zoom_level': 0.6,
        'key_landmarks': [11, 12, 13, 14, 15, 16],
        'camera_hint': "Position camera at the side to show your legs and back support",
    },
    'lift_extended_leg_supine_s1': {
        'focus_area': 'full_body',
        'zoom_level': 0.8,
        'key_landmarks': [5, 11, 13, 15],  # shoulder, hip, knee, ankle – all needed for hip angle
        'camera_hint': "Lie on your side facing the camera — camera must show shoulder, hip, knee, and ankle",
    },
    'bending_knee_bed_support_supine_s1': {
        'focus_area': 'lower_body',
        'zoom_level': 0.6,
        'key_landmarks': [11, 13, 15],  # hip, knee, ankle
        'camera_hint': "Position camera at your side so it shows hip, knee, and ankle clearly",
    },
    # Session 2 – lower body
    'bending_knee_no_support_seated_s2': {
        'focus_area': 'lower_body',
        'zoom_level': 0.6,
        'key_landmarks': [11, 12, 13, 14, 15, 16],
        'camera_hint': "Position camera at the side to show your full legs while seated",
    },
    'bending_knee_with_support_seated_s2': {
        'focus_area': 'lower_body',
        'zoom_level': 0.6,
        'key_landmarks': [11, 12, 13, 14, 15, 16],
        'camera_hint': "Position camera at the side to show your legs and back support",
    },
    'lift_extended_leg_supine_s2': {
        'focus_area': 'full_body',
        'zoom_level': 0.8,
        'key_landmarks': [5, 11, 13, 15],
        'camera_hint': "Lie on your side facing the camera — camera must show shoulder, hip, knee, and ankle",
    },
    'bending_knee_bed_support_supine_s2': {
        'focus_area': 'lower_body',
        'zoom_level': 0.6,
        'key_landmarks': [11, 13, 15],
        'camera_hint': "Position camera at your side so it shows hip, knee, and ankle clearly",
    },
    # Session 1 – upper body
    'shoulder_flexion_seated_s1': {
        'focus_area': 'upper_body',
        'zoom_level': 0.7,
        'key_landmarks': [5, 7, 11],  # shoulder, elbow, hip
        'camera_hint': "Sit sideways to the camera — it must see your hip, shoulder, and elbow",
    },
    'horizontal_weighted_openings_standing_s1': {
        'focus_area': 'upper_body',
        'zoom_level': 0.7,
        'key_landmarks': [5, 6, 7, 8, 11, 12],
        'camera_hint': "Face the camera directly — stand back so your full arm span is visible",
    },
    'external_rotation_shoulders_elastic_s1': {
        'focus_area': 'upper_body',
        'zoom_level': 0.6,
        'key_landmarks': [5, 7, 9],  # shoulder, elbow, wrist
        'camera_hint': "Face the camera — it must clearly see both elbows and wrists",
    },
    'circular_pendulum_standing_s1': {
        'focus_area': 'upper_body',
        'zoom_level': 0.7,
        'key_landmarks': [5, 7, 11],
        'camera_hint': "Position camera at your side — it must see your hip, shoulder, and hanging arm",
    },
    # Session 2 – upper body
    'shoulder_flexion_seated_s2': {
        'focus_area': 'upper_body',
        'zoom_level': 0.7,
        'key_landmarks': [5, 7, 11],
        'camera_hint': "Sit sideways to the camera — it must see your hip, shoulder, and elbow at all heights",
    },
    'horizontal_weighted_openings_standing_s2': {
        'focus_area': 'upper_body',
        'zoom_level': 0.8,
        'key_landmarks': [5, 6, 7, 8, 11, 12],
        'camera_hint': "Face the camera — stand further back, wider spread needs more frame",
    },
    'external_rotation_shoulders_elastic_s2': {
        'focus_area': 'upper_body',
        'zoom_level': 0.6,
        'key_landmarks': [5, 7, 9],
        'camera_hint': "Face the camera — it must clearly see both elbows and wrists",
    },
    'circular_pendulum_standing_s2': {
        'focus_area': 'upper_body',
        'zoom_level': 0.8,
        'key_landmarks': [5, 7, 11],
        'camera_hint': "Position camera at your side — stand back, larger circles need more frame",
    },
}


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE INSTRUCTIONS
# ─────────────────────────────────────────────────────────────────────────────

EXERCISE_INSTRUCTIONS = {
    # ── Session 1 – lower body ────────────────────────────────────────────────
    'bending_knee_no_support_seated_s1': {
        'name': "Knee Extension – Seated Without Support (Session 1)",
        'starting_position': [
            "Sit upright on a chair, feet flat on the floor",
            "Knee is bent to about 90 degrees in the resting position",
            "Hold the sides of the chair lightly for balance",
        ],
        'how_to': [
            "Slowly lift one foot off the floor",
            "Straighten your leg forward — aim for about 155 degrees at the knee",
            "Hold for 2 seconds at the top",
            "Slowly lower your foot back to the floor (return to 90 degrees)",
            "Repeat with the same leg",
        ],
        'tips': [
            "Keep your back upright — do not lean back",
            "Move slowly and with control — no jerking",
            "Stop if you feel pain; today's goal is a gentle partial extension",
        ],
        'voice_intro': "Session 1. Seated knee extension, no support. Lift and straighten your leg to about 155 degrees, then slowly lower.",
    },
    'bending_knee_with_support_seated_s1': {
        'name': "Knee Extension – Seated With Back Support (Session 1)",
        'starting_position': [
            "Sit on a chair with your back fully resting against the back support",
            "Feet flat on the floor, knee bent to about 90 degrees",
            "Let the chair support your posture throughout",
        ],
        'how_to': [
            "Slowly extend one leg forward",
            "Straighten your knee to about 150 degrees",
            "Hold for 2 seconds",
            "Slowly lower your foot back to the floor",
            "Repeat the same leg",
        ],
        'tips': [
            "Keep your back fully in contact with the chair",
            "Breathe out as you extend, breathe in as you lower",
            "Focus on smooth movement — the chair support lets you concentrate on the leg",
        ],
        'voice_intro': "Session 1. Seated knee extension with back support. Extend to 150 degrees and return smoothly.",
    },
    'lift_extended_leg_supine_s1': {
        'name': "Straight Leg Raise – Lying Down (Session 1)",
        'starting_position': [
            "Lie flat on your back on a firm surface",
            "Bend the non-exercising leg with foot flat on the surface",
            "Keep the exercising leg completely straight",
        ],
        'how_to': [
            "Tighten the thigh muscle of your straight leg (quad set)",
            "Slowly raise the straight leg upward",
            "Stop when the leg is about 30 degrees above the surface",
            "Hold for 2 seconds at the top",
            "Slowly lower the leg all the way back down to the surface",
        ],
        'tips': [
            "Keep your knee locked straight throughout the entire movement",
            "Press your lower back firmly into the surface while lifting",
            "30 degrees is about the height of one leg above the other when they are side by side",
        ],
        'voice_intro': "Session 1. Straight leg raise. Keep your knee straight and lift your leg to about 30 degrees, then lower completely.",
    },
    'bending_knee_bed_support_supine_s1': {
        'name': "Heel Slide – Lying Down (Session 1)",
        'starting_position': [
            "Lie flat on your back on a bed or mat",
            "Both legs straight, arms relaxed at your sides",
            "The surface supports your entire leg",
        ],
        'how_to': [
            "Slowly slide one heel along the surface toward your buttocks",
            "Bend your knee to about 70 degrees",
            "Hold for 2 seconds at the bent position",
            "Slowly slide your heel back out until your leg is straight (about 160 degrees)",
            "Repeat the same leg",
        ],
        'tips': [
            "Keep your heel in contact with the surface throughout — slide, do not lift",
            "Keep your lower back pressed to the surface",
            "Move smoothly without jerking",
        ],
        'voice_intro': "Session 1. Heel slide lying down. Slide your heel toward your body to 70 degrees, then slide it back to straight.",
    },

    # ── Session 2 – lower body ────────────────────────────────────────────────
    'bending_knee_no_support_seated_s2': {
        'name': "Knee Extension – Seated Without Support (Session 2)",
        'starting_position': [
            "Sit upright on a chair, feet flat on the floor",
            "Knee bent to about 90 degrees at rest",
            "Hold the sides of the chair if needed",
        ],
        'how_to': [
            "Slowly lift one foot off the floor",
            "Push for a fuller extension — aim for about 175 degrees (nearly straight)",
            "Hold for 2 seconds at the top",
            "Slowly lower your foot back to the floor",
            "Repeat with the same leg",
        ],
        'tips': [
            "You are pushing for near-full extension today — avoid locking the knee hard",
            "Keep your back upright throughout",
            "Control the lowering phase — do not let the leg drop",
        ],
        'voice_intro': "Session 2. Seated knee extension, no support. Push for near-full extension to 175 degrees today.",
    },
    'bending_knee_with_support_seated_s2': {
        'name': "Knee Extension – Seated With Back Support (Session 2)",
        'starting_position': [
            "Sit with your back fully against the chair back support",
            "Feet flat on the floor, knee bent to about 90 degrees",
        ],
        'how_to': [
            "Slowly extend one leg forward",
            "Push further than last session — aim for about 165 degrees",
            "Hold for 2 seconds",
            "Slowly lower back to the floor",
        ],
        'tips': [
            "You are working to a fuller range than Session 1",
            "Breathe steadily — do not hold your breath",
            "The chair back keeps your posture stable so you can focus on the leg",
        ],
        'voice_intro': "Session 2. Seated knee extension with support. Push to 165 degrees — a fuller range than last time.",
    },
    'lift_extended_leg_supine_s2': {
        'name': "Straight Leg Raise – Lying Down (Session 2)",
        'starting_position': [
            "Lie flat on your back on a firm surface",
            "Bend the non-exercising leg with foot flat on the surface",
            "Keep the exercising leg completely straight",
        ],
        'how_to': [
            "Tighten the thigh muscle of your straight leg",
            "Slowly raise the straight leg upward",
            "Aim to raise the leg to about 45–60 degrees above the surface",
            "Hold for 2 seconds at the top",
            "Slowly lower the leg completely back to the surface",
        ],
        'tips': [
            "Keep your knee locked straight the entire time",
            "Raising to 60 degrees means your foot is roughly at the height of the bent knee",
            "Press your lower back into the surface — do not let it arch",
        ],
        'voice_intro': "Session 2. Straight leg raise. Lift to 45 to 60 degrees today — higher than last session. Keep the knee locked straight.",
    },
    'bending_knee_bed_support_supine_s2': {
        'name': "Heel Slide – Lying Down (Session 2)",
        'starting_position': [
            "Lie flat on your back on a bed or mat",
            "Both legs straight, arms relaxed at your sides",
        ],
        'how_to': [
            "Slowly slide one heel along the surface toward your buttocks",
            "Push for a deeper bend — aim for about 55 degrees",
            "Hold for 2 seconds",
            "Slowly slide your heel back out until your leg is as straight as possible (about 165 degrees)",
            "Repeat the same leg",
        ],
        'tips': [
            "Sliding further today — push the heel closer to your body than last session",
            "Keep your heel on the surface throughout",
            "Move slowly and in full control",
        ],
        'voice_intro': "Session 2. Heel slide. Slide deeper to 55 degrees today and extend back to 165 degrees.",
    },

    # ── Session 1 – upper body ────────────────────────────────────────────────
    'shoulder_flexion_seated_s1': {
        'name': "Shoulder Flexion – Seated (Session 1)",
        'starting_position': [
            "Sit on a chair with back support, feet flat on the floor",
            "Arm resting at your side (shoulder angle ≈ 10–15 degrees)",
            "Elbow straight but not locked",
        ],
        'how_to': [
            "Slowly raise your arm forward and upward",
            "Stop when your arm reaches shoulder height — about 90 degrees above the body",
            "Hold for 2 seconds",
            "Slowly lower your arm back to your side",
        ],
        'tips': [
            "Keep your elbow straight throughout the movement",
            "Do not arch your back — keep your core gently engaged",
            "Today's goal is shoulder height only — we will go higher next session",
        ],
        'voice_intro': "Session 1. Shoulder flexion seated. Raise your arm to shoulder height and lower slowly. Keep the elbow straight.",
    },
    'horizontal_weighted_openings_standing_s1': {
        'name': "Horizontal Arm Openings With Weights (Session 1)",
        'starting_position': [
            "Stand with feet shoulder-width apart, good posture",
            "Hold a light weight in each hand",
            "Arms hanging at your sides or extended slightly forward",
        ],
        'how_to': [
            "Raise your arms out to the sides and forward to shoulder height",
            "Open your arms further apart — aim for a moderate spread (about 110 degrees)",
            "Hold for 1 second at the open position",
            "Slowly bring your arms back together",
            "Repeat",
        ],
        'tips': [
            "Keep arms at shoulder height throughout — do not let them drop",
            "Use light weights today to focus on form",
            "Keep a slight bend in your elbows — do not lock them",
        ],
        'voice_intro': "Session 1. Horizontal arm openings. Open your arms to a moderate spread at shoulder height. Light weights today.",
    },
    'external_rotation_shoulders_elastic_s1': {
        'name': "Shoulder External Rotation With Elastic Band (Session 1)",
        'starting_position': [
            "Stand or sit with good posture",
            "Hold the elastic band with both hands",
            "Elbows bent to 90 degrees, tucked close to your sides",
            "Forearms pointing forward, parallel to the floor",
        ],
        'how_to': [
            "Keep elbows firmly against your sides",
            "Slowly rotate your forearms outward, stretching the band",
            "Stop at a comfortable rotation — elbows stay at 90 degrees",
            "Hold for 2 seconds",
            "Slowly return forearms to the starting position",
        ],
        'tips': [
            "Elbows must not drift away from your sides",
            "Use a light band today — focus on keeping form correct",
            "The movement comes from rotating the shoulder, not bending the elbows",
        ],
        'voice_intro': "Session 1. Shoulder external rotation with band. Keep elbows at your sides at 90 degrees and rotate outward gently.",
    },
    'circular_pendulum_standing_s1': {
        'name': "Circular Pendulum – Standing (Session 1)",
        'starting_position': [
            "Stand beside a table or chair and hold it with your non-exercising hand",
            "Bend forward at the waist about 30–45 degrees",
            "Let your exercising arm hang down freely — completely relaxed",
        ],
        'how_to': [
            "Use a gentle body rock to start your arm swinging",
            "Guide the arm into small clockwise circles — about 20 cm diameter",
            "Do 10 circles clockwise",
            "Then switch to 10 circles counter-clockwise",
            "Keep your arm and shoulder completely relaxed throughout",
        ],
        'tips': [
            "Let gravity do the work — do NOT use your shoulder muscles to swing",
            "Small circles today — about the size of a dinner plate (20 cm)",
            "If you feel your shoulder tense up, stop and relax before continuing",
        ],
        'voice_intro': "Session 1. Circular pendulum. Bend forward, let your arm hang, and make small relaxed circles. About 20 centimeters.",
    },

    # ── Session 2 – upper body ────────────────────────────────────────────────
    'shoulder_flexion_seated_s2': {
        'name': "Shoulder Flexion – Seated (Session 2)",
        'starting_position': [
            "Sit on a chair with back support, feet flat on the floor",
            "Arm resting at your side",
            "Elbow straight",
        ],
        'how_to': [
            "Slowly raise your arm forward and upward",
            "Continue past shoulder height — raise all the way overhead",
            "Aim for about 170 degrees (arm nearly vertical overhead)",
            "Hold for 2 seconds at the top",
            "Slowly lower your arm all the way back to your side",
        ],
        'tips': [
            "Keep your elbow straight throughout",
            "Do not arch your lower back as you reach overhead — engage your core",
            "Lower the arm fully before the next repetition",
        ],
        'voice_intro': "Session 2. Shoulder flexion seated. Raise your arm all the way overhead to 170 degrees, then lower fully.",
    },
    'horizontal_weighted_openings_standing_s2': {
        'name': "Horizontal Arm Openings With Weights (Session 2)",
        'starting_position': [
            "Stand with feet shoulder-width apart, good posture",
            "Hold weights in each hand",
            "Arms extended slightly forward at shoulder height",
        ],
        'how_to': [
            "Open your arms out to the sides",
            "Push for the full spread — aim for about 130 degrees (T position)",
            "Hold for 1 second at the fully open position",
            "Slowly bring your arms back together in front of you",
            "Repeat",
        ],
        'tips': [
            "Full T spread today — wider than Session 1",
            "Keep arms at shoulder height — do not let them drop as you open wider",
            "Control the return movement — do not let the weights pull you forward",
        ],
        'voice_intro': "Session 2. Horizontal arm openings. Open to a full T spread at 130 degrees. Wider than last time.",
    },
    'external_rotation_shoulders_elastic_s2': {
        'name': "Shoulder External Rotation With Elastic Band (Session 2)",
        'starting_position': [
            "Stand or sit with good posture",
            "Hold a medium-resistance elastic band with both hands",
            "Elbows bent to 90 degrees, tucked close to your sides",
            "Forearms pointing forward",
        ],
        'how_to': [
            "Keep elbows firmly against your sides",
            "Slowly rotate your forearms further outward than last session",
            "Push for a wider rotation — stretch the band more",
            "Hold for 2 seconds at maximum rotation",
            "Slowly and with control return to starting position",
        ],
        'tips': [
            "Use a medium resistance band — more challenge than Session 1",
            "Rotate further out — push the range",
            "Control the band on the return — do not let it snap back",
        ],
        'voice_intro': "Session 2. Shoulder external rotation with band. Use a stronger band and rotate further outward. Control both directions.",
    },
    'circular_pendulum_standing_s2': {
        'name': "Circular Pendulum – Standing (Session 2)",
        'starting_position': [
            "Stand beside a table or chair and hold it with your non-exercising hand",
            "Bend forward at the waist about 30–45 degrees",
            "Let your exercising arm hang down freely",
        ],
        'how_to': [
            "Use body rocking to start your arm swinging in larger circles",
            "Guide into circles about 40–50 cm in diameter",
            "Do 10 circles clockwise",
            "Then switch to 10 circles counter-clockwise",
            "Maintain a relaxed shoulder throughout",
        ],
        'tips': [
            "Larger circles today than Session 1 — about 40 to 50 cm diameter",
            "Still use gravity and body momentum — not your shoulder muscles",
            "Stay relaxed — tension in the shoulder defeats the purpose of this exercise",
        ],
        'voice_intro': "Session 2. Circular pendulum. Make larger circles today — 40 to 50 centimeters. Stay completely relaxed.",
    },
}


# ─────────────────────────────────────────────────────────────────────────────
# ERROR RULES
#
# Angle reference for each exercise (matches exercise_validator.py):
#
# bending_knee_no_support_seated_s1/s2 : knee hip→knee→ankle
#   MIN = seated resting ≈85°  |  MAX = extended ≈155°(S1) / 175°(S2)
#   Error logic (at the EXTENDED/MAX position):
#     insufficient_extension : angle < max_a - 20  (not straightening enough)
#     excessive_extension    : angle > max_a + 5   (hyperextending)
#   Error logic (at the BENT/MIN position):
#     insufficient_flexion   : angle > min_a + 15  (not bending enough to return)
#
# lift_extended_leg_supine_s1/s2 : hip  shoulder→hip→knee
#   MIN = leg RAISED  ≈145°(S1) / ≈120°(S2)  |  MAX = leg FLAT ≈170°
#   Formula: hip_angle = 180° − raise_angle_from_horizontal
#   Error logic:
#     insufficient_lift : angle > min_a + 15  (not raising high enough)
#     excessive_lift    : angle < min_a - 15  (raising dangerously high)
#     leg_not_straight  : checked via secondary joint (knee angle must be 160–180°)
#
# bending_knee_bed_support_supine_s1/s2 : knee hip→knee→ankle
#   MIN = knee FLEXED ≈70°(S1) / ≈55°(S2)  |  MAX = leg EXTENDED ≈160°(S1) / 165°(S2)
#
# shoulder_flexion_seated_s1/s2 : shoulder hip→shoulder→elbow
#   MIN = arm at side ≈10°  |  MAX = arm raised ≈120°(S1) / ≈170°(S2)
#
# horizontal_weighted_openings_standing_s1/s2 : shoulder elbow→shoulder→hip
#   MIN = arms closed ≈50°  |  MAX = arms open ≈110°(S1) / ≈130°(S2)
#
# external_rotation_shoulders_elastic_s1/s2 : elbow shoulder→elbow→wrist
#   Stays near 90° ± tolerance  ≈75–105°(S1) / ≈65–115°(S2)
#
# circular_pendulum_standing_s1/s2 : shoulder hip→shoulder→elbow  (continuous)
#   Oscillation range ≈5–40°(S1) / ≈10–65°(S2)
# ─────────────────────────────────────────────────────────────────────────────

ERROR_RULES = {

    # ── Session 1 – lower body ────────────────────────────────────────────────

    'bending_knee_no_support_seated_s1': {
        'joint': 'knee',
        'min_angle': 85,   # seated resting – knee bent
        'max_angle': 155,  # partial extension target
        'errors': {
            # Not extending far enough (angle stays too low)
            'insufficient_extension': {
                'condition': lambda angle, min_a, max_a: angle < max_a - 20,
                'recommendation': "Straighten your leg more — aim for 155 degrees",
                'severity': 'medium',
            },
            # Hyperextending past target
            'excessive_extension': {
                'condition': lambda angle, min_a, max_a: angle > max_a + 5,
                'recommendation': "Ease off slightly — do not force the knee beyond the target",
                'severity': 'low',
            },
            # Not returning to the bent rest position between reps
            'insufficient_return': {
                'condition': lambda angle, min_a, max_a: angle > min_a + 20,
                'recommendation': "Lower your foot fully to the floor before the next rep",
                'severity': 'medium',
            },
        },
        'movement_speed_check': True,
        'min_rep_duration': 2.5,
    },

    'bending_knee_with_support_seated_s1': {
        'joint': 'knee',
        'min_angle': 85,
        'max_angle': 150,
        'errors': {
            'insufficient_extension': {
                'condition': lambda angle, min_a, max_a: angle < max_a - 20,
                'recommendation': "Straighten your leg more — aim for 150 degrees",
                'severity': 'medium',
            },
            'excessive_extension': {
                'condition': lambda angle, min_a, max_a: angle > max_a + 5,
                'recommendation': "Do not push beyond today's target range",
                'severity': 'low',
            },
            'insufficient_return': {
                'condition': lambda angle, min_a, max_a: angle > min_a + 20,
                'recommendation': "Lower your foot fully to the floor before the next rep",
                'severity': 'medium',
            },
        },
        'movement_speed_check': True,
        'min_rep_duration': 2.0,
    },

    'lift_extended_leg_supine_s1': {
        # MIN = leg raised (hip angle ≈145°)  |  MAX = leg flat (hip angle ≈170°)
        # shoulder→hip→knee angle = 180° − raise_angle_from_horizontal
        'joint': 'hip',
        'min_angle': 145,  # raised ~30–35° from horizontal
        'max_angle': 170,  # lying flat
        'secondary_joint': 'knee',
        'secondary_min': 160,
        'secondary_max': 180,
        'errors': {
            'leg_not_straight': {
                # Handled by secondary joint check in exercise_correction.py
                'condition': lambda angle, min_a, max_a: False,
                'recommendation': "Keep your knee locked straight — do not bend it while lifting",
                'severity': 'high',
            },
            # angle > 160 means leg is not raised to ~30° yet
            'insufficient_lift': {
                'condition': lambda angle, min_a, max_a: angle > min_a + 15,
                'recommendation': "Raise your leg higher — aim for about 30 degrees above the surface",
                'severity': 'medium',
            },
            # angle < 130 means leg is raised more than ~50° — too high for S1
            'excessive_lift': {
                'condition': lambda angle, min_a, max_a: angle < min_a - 15,
                'recommendation': "Lower your leg a little — do not raise above 35 degrees this session",
                'severity': 'high',
            },
            # angle < 160 means leg has not returned fully to the surface
            'incomplete_lowering': {
                'condition': lambda angle, min_a, max_a: angle < max_a - 10,
                'recommendation': "Lower your leg completely to the surface before the next rep",
                'severity': 'low',
            },
        },
        'movement_speed_check': True,
        'min_rep_duration': 2.5,
    },

    'bending_knee_bed_support_supine_s1': {
        # MIN = knee flexed ≈70°  |  MAX = knee extended ≈160°
        'joint': 'knee',
        'min_angle': 70,
        'max_angle': 160,
        'errors': {
            # Not bending deep enough
            'insufficient_flexion': {
                'condition': lambda angle, min_a, max_a: angle > min_a + 20,
                'recommendation': "Slide your heel closer to your body — bend your knee more",
                'severity': 'medium',
            },
            # Bending beyond safe range
            'excessive_flexion': {
                'condition': lambda angle, min_a, max_a: angle < min_a - 10,
                'recommendation': "Do not bend further — stay within today's comfortable range",
                'severity': 'high',
            },
            # Not extending back to straight
            'insufficient_extension': {
                'condition': lambda angle, min_a, max_a: angle < max_a - 20,
                'recommendation': "Slide your heel back out — straighten your leg more fully",
                'severity': 'medium',
            },
        },
        'movement_speed_check': True,
        'min_rep_duration': 2.5,
    },

    # ── Session 2 – lower body ────────────────────────────────────────────────

    'bending_knee_no_support_seated_s2': {
        'joint': 'knee',
        'min_angle': 85,
        'max_angle': 175,
        'errors': {
            'insufficient_extension': {
                'condition': lambda angle, min_a, max_a: angle < max_a - 20,
                'recommendation': "Push further — aim for near-full extension at 175 degrees",
                'severity': 'medium',
            },
            'excessive_extension': {
                'condition': lambda angle, min_a, max_a: angle > max_a + 5,
                'recommendation': "Do not hyperextend — keep a slight softness at full extension",
                'severity': 'low',
            },
            'insufficient_return': {
                'condition': lambda angle, min_a, max_a: angle > min_a + 20,
                'recommendation': "Lower your foot fully to the floor before the next rep",
                'severity': 'medium',
            },
        },
        'movement_speed_check': True,
        'min_rep_duration': 2.0,
    },

    'bending_knee_with_support_seated_s2': {
        'joint': 'knee',
        'min_angle': 85,
        'max_angle': 165,
        'errors': {
            'insufficient_extension': {
                'condition': lambda angle, min_a, max_a: angle < max_a - 20,
                'recommendation': "Extend further today — push toward 165 degrees",
                'severity': 'medium',
            },
            'excessive_extension': {
                'condition': lambda angle, min_a, max_a: angle > max_a + 5,
                'recommendation': "Do not force past the target — ease off slightly",
                'severity': 'low',
            },
            'insufficient_return': {
                'condition': lambda angle, min_a, max_a: angle > min_a + 20,
                'recommendation': "Lower your foot to the floor fully before starting the next rep",
                'severity': 'medium',
            },
        },
        'movement_speed_check': True,
        'min_rep_duration': 2.0,
    },

    'lift_extended_leg_supine_s2': {
        # MIN = leg raised (hip angle ≈120°, ~55–60° from horizontal)  |  MAX = flat ≈170°
        'joint': 'hip',
        'min_angle': 120,
        'max_angle': 170,
        'secondary_joint': 'knee',
        'secondary_min': 160,
        'secondary_max': 180,
        'errors': {
            'leg_not_straight': {
                'condition': lambda angle, min_a, max_a: False,
                'recommendation': "Keep your knee locked straight throughout the entire lift",
                'severity': 'high',
            },
            # angle > 135 means not raised to 45° yet
            'insufficient_lift': {
                'condition': lambda angle, min_a, max_a: angle > min_a + 15,
                'recommendation': "Raise your leg higher — aim for 45 to 60 degrees above the surface",
                'severity': 'medium',
            },
            # angle < 105 means raised beyond 75° — too high
            'excessive_lift': {
                'condition': lambda angle, min_a, max_a: angle < min_a - 15,
                'recommendation': "Lower your leg slightly — do not raise above 65 degrees",
                'severity': 'high',
            },
            # angle < 160 means leg not fully returned to flat
            'incomplete_lowering': {
                'condition': lambda angle, min_a, max_a: angle < max_a - 10,
                'recommendation': "Lower your leg completely to the surface before the next rep",
                'severity': 'low',
            },
        },
        'movement_speed_check': True,
        'min_rep_duration': 3.0,
    },

    'bending_knee_bed_support_supine_s2': {
        # MIN = knee flexed ≈55°  |  MAX = extended ≈165°
        'joint': 'knee',
        'min_angle': 55,
        'max_angle': 165,
        'errors': {
            'insufficient_flexion': {
                'condition': lambda angle, min_a, max_a: angle > min_a + 20,
                'recommendation': "Slide your heel further — push for a deeper bend today",
                'severity': 'medium',
            },
            'excessive_flexion': {
                'condition': lambda angle, min_a, max_a: angle < min_a - 10,
                'recommendation': "Do not bend further than feels comfortable",
                'severity': 'high',
            },
            'insufficient_extension': {
                'condition': lambda angle, min_a, max_a: angle < max_a - 20,
                'recommendation': "Slide your heel back out — extend your leg more fully",
                'severity': 'medium',
            },
        },
        'movement_speed_check': True,
        'min_rep_duration': 2.0,
    },

    # ── Session 1 – upper body ────────────────────────────────────────────────

    'shoulder_flexion_seated_s1': {
        # MIN = arm at side ≈10°  |  MAX = arm at shoulder height ≈120°
        'joint': 'shoulder',
        'min_angle': 10,
        'max_angle': 120,
        'errors': {
            # Not raising to shoulder height
            'insufficient_raise': {
                'condition': lambda angle, min_a, max_a: angle < max_a - 25,
                'recommendation': "Raise your arm higher — aim for shoulder height (90 degrees elevation)",
                'severity': 'medium',
            },
            # Raising above target for this session
            'excessive_raise': {
                'condition': lambda angle, min_a, max_a: angle > max_a + 15,
                'recommendation': "Do not raise above shoulder height this session — lower your arm slightly",
                'severity': 'low',
            },
            # Not lowering arm fully back to side
            'incomplete_lowering': {
                'condition': lambda angle, min_a, max_a: angle > min_a + 25,
                'recommendation': "Lower your arm fully back to your side before the next rep",
                'severity': 'medium',
            },
        },
        'movement_speed_check': True,
        'min_rep_duration': 2.0,
    },

    'horizontal_weighted_openings_standing_s1': {
        # MIN = arms closed ≈50°  |  MAX = arms moderately open ≈110°
        'joint': 'shoulder',
        'min_angle': 50,
        'max_angle': 110,
        'errors': {
            # Not opening wide enough
            'insufficient_opening': {
                'condition': lambda angle, min_a, max_a: angle < max_a - 20,
                'recommendation': "Open your arms wider — spread further to the sides",
                'severity': 'medium',
            },
            # Opening beyond the S1 target
            'excessive_opening': {
                'condition': lambda angle, min_a, max_a: angle > max_a + 10,
                'recommendation': "Do not open wider than today's target — control the range",
                'severity': 'high',
            },
            # Not closing arms back together
            'insufficient_closing': {
                'condition': lambda angle, min_a, max_a: angle > min_a + 15,
                'recommendation': "Bring your arms back together in front before the next rep",
                'severity': 'low',
            },
        },
        'movement_speed_check': True,
        'min_rep_duration': 2.0,
    },

    'external_rotation_shoulders_elastic_s1': {
        # Elbow angle (shoulder→elbow→wrist) stays ≈75–105°
        # Elbow stays bent at ~90°; range captures light outward rotation
        'joint': 'elbow',
        'min_angle': 75,
        'max_angle': 105,
        'errors': {
            # Elbow drifting away from body (over-open)
            'elbow_drifting_out': {
                'condition': lambda angle, min_a, max_a: angle > max_a + 10,
                'recommendation': "Keep your elbows tucked against your sides",
                'severity': 'high',
            },
            # Elbow collapsing inward
            'elbow_collapsing': {
                'condition': lambda angle, min_a, max_a: angle < min_a - 10,
                'recommendation': "Do not collapse your elbows inward — maintain the 90-degree bend",
                'severity': 'medium',
            },
            'too_fast': {
                'condition': lambda angle, min_a, max_a: False,
                'recommendation': "Slow down — control the band in both directions",
                'severity': 'medium',
            },
        },
        'movement_speed_check': True,
        'min_rep_duration': 2.5,
    },

    'circular_pendulum_standing_s1': {
        # Continuous oscillation; range ≈5–40° (small circles ≈20 cm)
        'joint': 'shoulder',
        'min_angle': 5,
        'max_angle': 40,
        'errors': {
            # Circles too big for S1
            'circles_too_large': {
                'condition': lambda angle, min_a, max_a: angle > max_a + 10,
                'recommendation': "Make smaller circles — keep them about 20 centimeters today",
                'severity': 'medium',
            },
            # Barely moving
            'insufficient_motion': {
                'condition': lambda angle, min_a, max_a: angle < min_a + 3,
                'recommendation': "Let your arm swing a little more freely in the circles",
                'severity': 'low',
            },
            # Arm stopped moving (checked via motion history in exercise_correction.py)
            'stopped_motion': {
                'condition': lambda angle, min_a, max_a: False,
                'recommendation': "Keep your arm moving — do not stop mid-exercise",
                'severity': 'medium',
            },
        },
        'continuous_motion': True,
        'movement_speed_check': False,
    },

    # ── Session 2 – upper body ────────────────────────────────────────────────

    'shoulder_flexion_seated_s2': {
        # MIN = arm at side ≈10°  |  MAX = arm fully overhead ≈170°
        'joint': 'shoulder',
        'min_angle': 10,
        'max_angle': 170,
        'errors': {
            # Not raising all the way overhead
            'insufficient_raise': {
                'condition': lambda angle, min_a, max_a: angle < max_a - 30,
                'recommendation': "Raise your arm higher — push all the way overhead to 170 degrees",
                'severity': 'medium',
            },
            'excessive_raise': {
                'condition': lambda angle, min_a, max_a: angle > max_a + 10,
                'recommendation': "Lower your arm slightly — do not force past the natural range",
                'severity': 'low',
            },
            'incomplete_lowering': {
                'condition': lambda angle, min_a, max_a: angle > min_a + 25,
                'recommendation': "Lower your arm fully to your side before the next rep",
                'severity': 'medium',
            },
        },
        'movement_speed_check': True,
        'min_rep_duration': 2.0,
    },

    'horizontal_weighted_openings_standing_s2': {
        # MIN = arms closed ≈50°  |  MAX = full T spread ≈130°
        'joint': 'shoulder',
        'min_angle': 50,
        'max_angle': 130,
        'errors': {
            'insufficient_opening': {
                'condition': lambda angle, min_a, max_a: angle < max_a - 20,
                'recommendation': "Open your arms wider — push for the full T spread",
                'severity': 'medium',
            },
            'excessive_opening': {
                'condition': lambda angle, min_a, max_a: angle > max_a + 10,
                'recommendation': "Do not over-extend beyond the target — control the range",
                'severity': 'high',
            },
            'insufficient_closing': {
                'condition': lambda angle, min_a, max_a: angle > min_a + 15,
                'recommendation': "Bring your arms fully back together in front before the next rep",
                'severity': 'low',
            },
        },
        'movement_speed_check': True,
        'min_rep_duration': 2.0,
    },

    'external_rotation_shoulders_elastic_s2': {
        # Elbow angle ≈65–115°; wider rotation range with stronger band
        'joint': 'elbow',
        'min_angle': 65,
        'max_angle': 115,
        'errors': {
            'elbow_drifting_out': {
                'condition': lambda angle, min_a, max_a: angle > max_a + 10,
                'recommendation': "Keep your elbows tucked against your sides",
                'severity': 'high',
            },
            'elbow_collapsing': {
                'condition': lambda angle, min_a, max_a: angle < min_a - 10,
                'recommendation': "Do not collapse your elbows inward",
                'severity': 'medium',
            },
            'too_fast': {
                'condition': lambda angle, min_a, max_a: False,
                'recommendation': "Control the band on the way back — do not let it snap",
                'severity': 'medium',
            },
        },
        'movement_speed_check': True,
        'min_rep_duration': 2.5,
    },

    'circular_pendulum_standing_s2': {
        # Continuous oscillation; range ≈10–65° (larger circles ≈40–50 cm)
        'joint': 'shoulder',
        'min_angle': 10,
        'max_angle': 65,
        'errors': {
            # Circles too big even for S2
            'circles_too_large': {
                'condition': lambda angle, min_a, max_a: angle > max_a + 10,
                'recommendation': "Reduce the circle size slightly — stay within the target range",
                'severity': 'medium',
            },
            'insufficient_motion': {
                'condition': lambda angle, min_a, max_a: angle < min_a + 5,
                'recommendation': "Let your arm swing in bigger circles today — aim for 40 centimeters",
                'severity': 'low',
            },
            'stopped_motion': {
                'condition': lambda angle, min_a, max_a: False,
                'recommendation': "Keep your arm moving continuously — do not stop",
                'severity': 'medium',
            },
        },
        'continuous_motion': True,
        'movement_speed_check': False,
    },
}

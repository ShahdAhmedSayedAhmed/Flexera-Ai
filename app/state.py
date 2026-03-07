from typing import Optional, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.session import ExerciseSession

# YOLOv8 pose model (loaded on startup)
pose_model = None  # Optional[YOLO]

# Active exercise sessions keyed by session_key
active_sessions: Dict[str, "ExerciseSession"] = {}

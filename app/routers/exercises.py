from typing import List
from fastapi import APIRouter, HTTPException

from app.config import EXERCISE_CATALOG
from app.models.schemas import ExerciseListItem, ExerciseDetailResponse
from app.core.exercise_rules import EXERCISE_INSTRUCTIONS, EXERCISE_CAMERA_CONFIG, EXERCISE_RULES

router = APIRouter(prefix="/exercises", tags=["Exercises"])


@router.get("", response_model=List[ExerciseListItem], summary="List all exercises")
async def list_exercises():
    """
    Returns all 16 exercises in a format compatible with Flutter's ExerciseItem model.
    Categories match the Flutter app: lower_left, lower_right, upper_left, upper_right.
    """
    return [
        ExerciseListItem(
            id=ex_id,
            name=info["name"],
            key=info["key"],
            category=info["category"],
            session=info["session"],
            image=info["image"],
        )
        for ex_id, info in EXERCISE_CATALOG.items()
    ]


@router.get(
    "/category/{category}",
    response_model=List[ExerciseListItem],
    summary="Get exercises by category",
)
async def get_exercises_by_category(category: str):
    """
    Filter exercises by Flutter category:
    lower_left | lower_right | upper_left | upper_right | knee | shoulder
    """
    category_map = {
        "knee": ["lower_left", "lower_right"],
        "shoulder": ["upper_left", "upper_right"],
    }
    target_categories = category_map.get(category, [category])

    results = [
        ExerciseListItem(
            id=ex_id,
            name=info["name"],
            key=info["key"],
            category=info["category"],
            session=info["session"],
            image=info["image"],
        )
        for ex_id, info in EXERCISE_CATALOG.items()
        if info["category"] in target_categories
    ]

    if not results:
        raise HTTPException(status_code=404, detail=f"No exercises found for category: {category}")
    return results


@router.get(
    "/{exercise_id}",
    response_model=ExerciseDetailResponse,
    summary="Get exercise detail",
)
async def get_exercise_detail(exercise_id: str):
    """
    Full exercise info including instructions, camera guidance, and angle rules.
    Use this to populate the ExerciseDetailScreen in Flutter.
    """
    info = EXERCISE_CATALOG.get(exercise_id)
    if not info:
        raise HTTPException(status_code=404, detail=f"Exercise {exercise_id} not found")

    key = info["key"]
    instructions = EXERCISE_INSTRUCTIONS.get(key, {})
    camera_config = EXERCISE_CAMERA_CONFIG.get(key, {})

    # Serialize rules (exclude lambdas)
    raw_rules = EXERCISE_RULES.get(key, {})
    safe_rules: dict = {}
    for k, v in raw_rules.items():
        if k == "errors":
            safe_rules["errors"] = {
                err_name: {
                    "recommendation": err_data["recommendation"],
                    "severity": err_data["severity"],
                }
                for err_name, err_data in v.items()
            }
        elif not callable(v):
            safe_rules[k] = v

    return ExerciseDetailResponse(
        id=exercise_id,
        name=info["name"],
        key=key,
        category=info["category"],
        session=info["session"],
        image=info["image"],
        instructions=instructions,
        camera_config=camera_config,
        rules=safe_rules,
    )

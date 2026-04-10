from typing import List
from fastapi import APIRouter, HTTPException

from app.config import EXERCISE_CATALOG
from app.models.schemas import ExerciseListItem, ExerciseDetailResponse
from app.core.exercise_rules import EXERCISE_INSTRUCTIONS, EXERCISE_CAMERA_CONFIG, ERROR_RULES

router = APIRouter(prefix="/exercises", tags=["Exercises"])


def _to_list_item(ex_id: str, info: dict) -> ExerciseListItem:
    return ExerciseListItem(
        id=ex_id,
        name=info["name"],
        key=info["key"],
        category=info["category"],
        session=info["session"],
        image=info["image"],
    )


@router.get("", response_model=List[ExerciseListItem], summary="List all 16 exercises")
async def list_exercises():
    return [_to_list_item(ex_id, info) for ex_id, info in EXERCISE_CATALOG.items()]


@router.get(
    "/session/{session_num}",
    response_model=List[ExerciseListItem],
    summary="Get all exercises for a session number (1 or 2)",
)
async def get_exercises_by_session(session_num: int):
    if session_num not in (1, 2):
        raise HTTPException(status_code=400, detail="session_num must be 1 or 2")
    results = [
        _to_list_item(ex_id, info)
        for ex_id, info in EXERCISE_CATALOG.items()
        if info["session"] == session_num
    ]
    return results


@router.get(
    "/category/{category}",
    response_model=List[ExerciseListItem],
    summary="Get exercises by body category. Use 'knee', 'shoulder', or a raw category like 'lower_left'",
)
async def get_exercises_by_category(category: str):
    # Accept both friendly names and raw category strings
    category_map = {
        "knee": ["lower_left", "lower_right"],
        "shoulder": ["upper_left", "upper_right"],
        "lower": ["lower_left", "lower_right"],
        "upper": ["upper_left", "upper_right"],
    }
    target_categories = category_map.get(category, [category])

    results = [
        _to_list_item(ex_id, info)
        for ex_id, info in EXERCISE_CATALOG.items()
        if info["category"] in target_categories
    ]
    if not results:
        raise HTTPException(status_code=404, detail=f"No exercises found for category: {category}")
    return results


@router.get(
    "/session/{session_num}/category/{category}",
    response_model=List[ExerciseListItem],
    summary="Get exercises filtered by both session number and body category",
)
async def get_exercises_by_session_and_category(session_num: int, category: str):
    if session_num not in (1, 2):
        raise HTTPException(status_code=400, detail="session_num must be 1 or 2")

    category_map = {
        "knee": ["lower_left", "lower_right"],
        "shoulder": ["upper_left", "upper_right"],
        "lower": ["lower_left", "lower_right"],
        "upper": ["upper_left", "upper_right"],
    }
    target_categories = category_map.get(category, [category])

    results = [
        _to_list_item(ex_id, info)
        for ex_id, info in EXERCISE_CATALOG.items()
        if info["session"] == session_num and info["category"] in target_categories
    ]
    if not results:
        raise HTTPException(
            status_code=404,
            detail=f"No exercises found for session={session_num}, category={category}",
        )
    return results


@router.get("/{exercise_id}", response_model=ExerciseDetailResponse, summary="Get full exercise detail by ID (01–16)")
async def get_exercise_detail(exercise_id: str):
    info = EXERCISE_CATALOG.get(exercise_id)
    if not info:
        raise HTTPException(status_code=404, detail=f"Exercise {exercise_id} not found")

    key = info["key"]
    raw_rules = ERROR_RULES.get(key, {})

    # Serialize error rules — strip non-serialisable lambda conditions
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
        instructions=EXERCISE_INSTRUCTIONS.get(key, {}),
        camera_config=EXERCISE_CAMERA_CONFIG.get(key, {}),
        rules=safe_rules,
    )

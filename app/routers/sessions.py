from fastapi import APIRouter, HTTPException

import app.state as state
from app.config import EXERCISE_CATALOG
from app.models.schemas import SessionStartRequest, SessionStatusResponse
from app.models.session import ExerciseSession

router = APIRouter(prefix="/session", tags=["Sessions"])


@router.post(
    "/start",
    response_model=SessionStatusResponse,
    summary="Start an exercise session",
)
async def start_session(req: SessionStartRequest):
    """
    Start a new AI validation session for a user.
    Returns a session_key to use in subsequent /process or WebSocket calls.

    Flutter usage: call this when user taps 'Start Exercise'.
    """
    if req.exercise_id not in EXERCISE_CATALOG:
        raise HTTPException(status_code=404, detail=f"Exercise {req.exercise_id} not found")

    if state.pose_model is None:
        raise HTTPException(status_code=503, detail="AI model is still loading, try again shortly")

    session = ExerciseSession(
        exercise_id=req.exercise_id,
        user_id=req.user_id,
        target_sets=req.target_sets,
        target_reps=req.target_reps,
    )
    state.active_sessions[session.session_key] = session

    return SessionStatusResponse(**session.to_dict())


@router.get(
    "/{session_key}",
    response_model=SessionStatusResponse,
    summary="Get session progress",
)
async def get_session(session_key: str):
    """Get the current progress of an active exercise session."""
    session = state.active_sessions.get(session_key)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found or expired")
    return SessionStatusResponse(**session.to_dict())


@router.post(
    "/{session_key}/next-set",
    response_model=SessionStatusResponse,
    summary="Advance to next set",
)
async def advance_to_next_set(session_key: str):
    """
    Manually advance the session to the next set (or mark complete).
    Flutter should call this after the user confirms a set is done.
    """
    session = state.active_sessions.get(session_key)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found or expired")
    if session.is_complete:
        raise HTTPException(status_code=400, detail="Exercise is already complete")

    session.advance_set()
    return SessionStatusResponse(**session.to_dict())


@router.post(
    "/{session_key}/reset",
    response_model=SessionStatusResponse,
    summary="Reset session from beginning",
)
async def reset_session(session_key: str):
    """Reset the session back to set 1, rep 0."""
    session = state.active_sessions.get(session_key)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found or expired")
    session.reset_all()
    return SessionStatusResponse(**session.to_dict())


@router.delete(
    "/{session_key}",
    summary="End and remove a session",
)
async def end_session(session_key: str):
    """
    Delete the session when the user exits the exercise screen.
    Flutter should call this in the screen's dispose() method.
    """
    if session_key not in state.active_sessions:
        raise HTTPException(status_code=404, detail="Session not found or expired")
    del state.active_sessions[session_key]
    return {"message": "Session ended", "session_key": session_key}

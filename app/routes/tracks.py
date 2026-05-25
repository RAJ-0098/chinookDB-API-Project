from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas.track import TrackResponse
from app.services.track_service import fetch_tracks


router = APIRouter()


@router.get(
    "/tracks",
    response_model=list[TrackResponse]
)
def get_tracks(
    db: Session = Depends(get_db)
):

    return fetch_tracks(db)
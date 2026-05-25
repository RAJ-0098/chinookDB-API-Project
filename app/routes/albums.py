from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas.album import AlbumResponse
from app.services.album_service import fetch_albums


router = APIRouter()


@router.get(
    "/albums",
    response_model=list[AlbumResponse]
)
def get_albums(
    db: Session = Depends(get_db)
):

    return fetch_albums(db)
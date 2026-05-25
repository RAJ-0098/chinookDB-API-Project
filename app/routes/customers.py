from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.customer import CustomerResponse
from app.services.customer_service import fetch_customers
from app.db import get_db
router = APIRouter() #creates modular route container.


@router.get(
    "/customers",
    response_model=list[CustomerResponse]
)
def get_customers(
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db)
):

    return fetch_customers(
        db,
        limit,
        offset
    )
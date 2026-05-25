from fastapi import APIRouter
from sqlalchemy import text 
from app.db import engine
from app.schemas.customer import CustomerResponse
router = APIRouter()
@router.get("/customers",
         response_model=CustomerResponse)
def fetch_customers(
    db,
    limit:int = 10,
    offset: int = 0
):
    query = text("""
        SELECT customer_id,
               first_name,
               last_name,
               email
        FROM customer
        LIMIT :limit
        OFFSET :offset
    """)

    

    result = db.execute(
            query,
            {
               "limit":limit,
              "offset": offset
              })

    customers = []

    for row in result:
            customers.append({
                "id": row.customer_id,
                "name": row.first_name + " " + row.last_name,
                "email": row.email
            })

    return customers
@router.get("/customers/{customer_id}",
    response_model=CustomerResponse)

def fetch_customer(customer_id: int,db):
    query = text(""" 
                 SELECT customer_id,
                 first_name,
                 last_name,
                 email
                 FROM customer
                 WHERE customer_id = :id
                 """)
    result = db.execute(query,
        {
            "id": customer_id
        })
    row = result.fetchone() 
#fetchone is used because single row is expected
    if row is None:
            return {
                "error": "Customer not found"
            }
    return{
            "id": row.customer_id,
            "name": row.first_name+" "+row.last_name,
            "email": row.email
        }

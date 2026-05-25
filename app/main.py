from fastapi import FastAPI
from sqlalchemy import text
from app.db import engine

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Chinook API Running"
    }

@app.get("/customers")
def get_customers():

    query = text("""
        SELECT customer_id,
               first_name,
               last_name,
               email
        FROM customer
        LIMIT 10
    """)

    with engine.connect() as conn:

        result = conn.execute(query)

        customers = []

        for row in result:
            customers.append({
                "id": row.customer_id,
                "name": row.first_name + " " + row.last_name,
                "email": row.email
            })

    return customers

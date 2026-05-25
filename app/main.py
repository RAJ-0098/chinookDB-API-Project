from fastapi import FastAPI

from app.routes.customers import router as customer_router
from app.routes.albums import router as album_router
from app.routes.tracks import router as track_router

app = FastAPI()


app.include_router(customer_router)
app.include_router(album_router)
app.include_router(track_router)


@app.get("/")
def home():

    return {
        "message": "Chinook API Running"
    }
# the 3,4,5 lines import modules from seperate files.
# the 10,11,12 lines go inside the imported modules and files.
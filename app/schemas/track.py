from pydantic import BaseModel


class TrackResponse(BaseModel):

    id: int
    name: str
    duration: int

#pydantic is a python framework and basemodel is a parent class provided by pydantic for request handling etc.. 
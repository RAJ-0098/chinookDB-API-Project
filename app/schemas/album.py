from pydantic import BaseModel


class AlbumResponse(BaseModel):

    id: int
    title: str
#pydantic is a python framework and basemodel is a parent class provided by pydantic for request handling etc.. 
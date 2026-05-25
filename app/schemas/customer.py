from pydantic import BaseModel


class CustomerResponse(BaseModel):

    id: int
    name: str
    email: str

#pydantic is a python framework and basemodel is a parent class provided by pydantic for request handling etc.. 
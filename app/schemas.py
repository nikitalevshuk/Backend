from pydantic import BaseModel

class Service(BaseModel):
    id: int
    name: str
    description: str
    price: int
    duration: int

    model_config = {'extra': "forbid"}

class Specialist(BaseModel):
    id: int
    name: str

    model_config = {'extra': "forbid"}
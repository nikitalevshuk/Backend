from pydantic import BaseModel
from pydantic import Field
from typing import Literal

class ServiceUpdate(BaseModel):
    id: int | None = None
    name: str | None = None
    description: str | None = None
    price: Literal[20,30,40, None] = None
    duration: Literal[30,45,60,75, None] = None

class Service(BaseModel):
    id: int = Field(examples=[1])
    name: str = Field(examples=["Service"])
    description: str = Field(examples=["All service characteristics"])
    price: Literal[20,30,40] = Field(examples=[20])
    duration: Literal[30,45,60,75] = Field(examples=[45])

class Specialist(BaseModel):
    id: int = Field(examples=[1])
    name: str = Field(examples=["Name"])

    
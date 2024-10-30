from pydantic import BaseModel, Field
from typing import Literal, Optional

class ServiceUpdate(BaseModel):
    id: Optional[int] = Field(default=None, example=1)
    name: Optional[str] = Field(default=None, example="Название услуги")
    description: Optional[str] = Field(default=None, example="Описание услуги")
    price: Optional[Literal[20, 30, 40]] = Field(default=None, example=20)
    duration: Literal[30, 45, 60, 75, None] = Field(default=None, example=30)

class Service(BaseModel):
    id: int = Field(example=1)
    name: str = Field(example="Название услуги")
    description: str = Field(example="Описание услуги")
    price: Literal[20, 30, 40] = Field(example=20)
    duration: Literal[30, 45, 60, 75] = Field(example=45)

class Specialist(BaseModel):
    id: int = Field(example=1)
    name: str = Field(example="Name")

class Orders(BaseModel):
    id: int = Field(example=1)
    name: str = Field(example="Юрий")
    service_id: int = Field(example=1)
    specialist_id: int = Field(example=1)
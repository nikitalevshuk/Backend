from pydantic import BaseModel, Field

# эта модель требует пересмотра, как и операция, к которой она относится
class ServiceUpdate(BaseModel):
    id: int | None = Field(default=None, example=None)
    name: str | None = Field(default=None, example=None)
    description: str | None = Field(default=None, example=None)
    price: int | None = Field(default=None, example=None)
    duration: int | None = Field(default=None, example=None)

class ServiceWithoutId(BaseModel):
    name: str = Field(example="Название услуги")
    description: str = Field(example="Описание услуги")
    price: int = Field(example=20)
    duration: int = Field(example=45)


class Service(ServiceWithoutId):
    id: int = Field(example=1)
    
    class Config:
        from_attributes = True

class SpecialistwithoutId(BaseModel):
    name: str = Field(example="Name")

class Specialist(SpecialistwithoutId):
    id: int = Field(example=1)

    class Config:
        from_attributes = True

class Orders(BaseModel):
    id: int = Field(example=1)
    name: str = Field(example="Юрий")
    service_id: int = Field(example=1)
    specialist_id: int = Field(example=1)
from fastapi import FastAPI, HTTPException, Path, Query, Body
from typing import Annotated, List
from fastapi.exceptions import RequestValidationError

from app.schemas import Service, Specialist,ServiceUpdate
from app.models import services, specialists

app = FastAPI()

#читаем все услуги
@app.get("/services/", response_model = List[Service], tags=["Services"])
async def read_services():
    return list(services.values())

#читаем одну услугу
@app.get("/services/{service_id}", response_model=Service, tags=["Services"])
async def read_service(service_id: Annotated[int, Path(description="The identification number of service", example= 1)]):
    if service_id not in services:
        raise HTTPException(status_code=422)
    return services[service_id]

#создаем услугу
@app.post("/services", response_model=Service, tags=["Services"])
async def create_service(service:Annotated[Service, Body(description="New service parameters")]):
    if service.id in services:
        raise HTTPException(status_code=400, detail="Service id is already exists")
    services[service.id] = service
    return services[service.id]

#редактируем услугу
@app.put("/services/{service_id}", response_model=ServiceUpdate, tags = ["Services"])
async def edit_service(service_id:Annotated[int, Path(description="The id of service to edit",example=1)], service:Annotated[ServiceUpdate, Body()]):
    if service_id not in services:
        raise HTTPException(status_code=404, detail = "Service not found")
    stored_service_data = services[service_id]
    stored_service_model = Service(**stored_service_data)
    update_data = service.model_dump(exclude_unset=True)
    updated_service = stored_service_model.copy(update=update_data)
    services[service_id] = updated_service
    return updated_service
   

#удаляем услугу
@app.delete("/services/{service_id}", response_model=dict, tags=["Services"])
async def delete_service(service_id: Annotated[int, Path(description="The ID of the service to delete", example=1)]):
    if service_id not in services:
        raise HTTPException(status_code=404, detail = "Service not found")
    del services[service_id]
    return {"detail": "Service deleted successfully"}

#смотрим всех специалистов
@app.get("/specialists/", response_model=List[Specialist], tags=["Specialists"])
async def get_allSpecialists():
    return list(specialists.values())

#смотрим только одного специалиста
@app.get("/specialists/{specialist_id}", response_model=Specialist, tags=["Specialists"])
async def get_specialist(specialist_id:Annotated[int, Path(description="The ID of specialist to read", example=1)]):
    if specialist_id not in specialists:
        raise HTTPException(status_code=404, detail="Specialist not found")
    return specialists[specialist_id]

#добавляем нового специалиста
@app.post("/specialists", response_model=Specialist, tags=["Specialists"])
async def create_specialist(new_specialist: Annotated[Specialist, Body(description="New specialist fields")]):
    if new_specialist.id in specialists:
        raise HTTPException(status_code=400, detail="Specialist id is already exists")
    specialists[new_specialist.id] = new_specialist
    return new_specialist

@app.delete("/specialists/{specialist_id}", response_model=dict, tags=["Specialists"])
async def delete_service(specialist_id: Annotated[int, Path(description="The ID of the service to delete", example=1)]):
    if specialist_id not in specialists:
        raise HTTPException(status_code=404, detail = "Specialist not found")
    del specialists[specialist_id]
    return {"detail": "Specialist deleted successfully"}




    
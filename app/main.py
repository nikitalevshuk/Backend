from fastapi import FastAPI, HTTPException, Path, Query, Body
from typing import Annotated, List, Optional

from app.schemas import Service, Specialists
from app.models import services, specialists

app = FastAPI()

#читаем все услуги
@app.get("/services/", response_model = List[Service])
async def read_services():
    return list(services.values())

#читаем одну услугу
@app.get("/services/{service_id}", response_model=Service)
async def read_service(service_id: Annotated[int, Path(description="The identification number of service")]):
    if service_id not in services:
        raise HTTPException(status_code=404, detail="Service not found")
    return services[service_id]

#создаем услугу
@app.post("/services", response_model=Service)
async def create_service(service:Annotated[Service, Body()]):
    if service.id in services:
        raise HTTPException(status_code=400, detail="Service id is already exists")
    services[service.id] = service
    return services[service.id]

#редактируем услугу
@app.put("/services/{service_id}", response_model=Service)
async def edit_service(service_id:Annotated[int, Path()], updated_service:Annotated[Service, Body()]):
    if service_id not in services:
        raise HTTPException(status_code=404, detail = "Service not found")
    services[service_id] = updated_service
    return updated_service

#удаляем услугу
@app.delete("/services/{service_id}", response_model=dict)
async def delete_service(service_id: Annotated[int, Path(description="The ID of the service to delete")]):
    if service_id not in services:
        raise HTTPException(status_code=404, detail = "Service not found")
    del services[service_id]
    return {"detail": "Service deleted successfully"}

@app.get("/specialists/", response_model=List[Specialists])
async def get_allSpecialists():
    return list(specialists.values())
    
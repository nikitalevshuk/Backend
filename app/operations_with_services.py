from fastapi import FastAPI, Path, Body, Depends, HTTPException, APIRouter
from typing import Annotated, List
from app.schemas import Service, ServiceUpdate
from app.models import services
from app.dependencies import get_service_or_404

router = APIRouter(prefix="/services", tags=["Services"])

#читаем все услуги
@router.get("/")
async def read_services() -> Service:
    return list(services.values())

#читаем одну услугу
@router.get("/{service_id}")
async def read_service(service:Annotated[Service, Depends(get_service_or_404)]) -> Service:
    return service

#создаем услугу
@router.post("/")
async def create_service(service:Annotated[Service, Body()]) -> dict:
    if service.id in services:
        raise HTTPException(status_code=400, detail="Service id is already exists")
    services[service.id] = service
    return services[service.id]

#редактируем услугу
@router.put("/{service_id}")
async def edit_service(
    service_id: Annotated[int, Path(example=1)],
    service: Annotated[ServiceUpdate, Body()],
    stored_service: Annotated[Service, Depends(get_service_or_404)]
) -> dict:    
    update_data = service.dict(exclude_unset=True)
    updated_service_data = {**stored_service.dict(), **update_data} 
    
    services[service_id] = updated_service_data
    
    return updated_service_data
   
#удаляем услугу
@router.delete("/{service_id}")
async def delete_service(
    service: Annotated[Service, Depends(get_service_or_404)]  
) -> dict:
    del services[service.id]
    return {"detail": "Service deleted successfully"}
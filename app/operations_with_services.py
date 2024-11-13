from fastapi import Path, Depends, APIRouter

from typing import Annotated, List

from app.schemas import Service, ServiceUpdate, ServiceWithoutId
from app.models import ServicesTable
from app.dependencies import get_service_or_404, get_db

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

router = APIRouter(prefix="/services", tags=["Services"])

#читаем все услуги
@router.get("/", response_model=List[Service])
async def read_services(db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(select(ServicesTable))
    services = result.scalars().all()

    return services

#читаем одну услугу
@router.get("/{service_id}", response_model=Service)
async def read_service(service:Annotated[ServicesTable, Depends(get_service_or_404)]):
    return service

#создаем услугу
@router.post("/", response_model=Service)
async def create_service(service: ServiceWithoutId, db:Annotated[AsyncSession, Depends(get_db)]):
    db_service = ServicesTable(
        name = service.name,
        description = service.description,
        price = service.price,
        duration = service.duration
    )

    db.add(db_service)
    await db.commit()
    await db.refresh(db_service)

    return db_service
    
#редактируем услугу
@router.put("/{service_id}", response_model = Service)
async def edit_service(
    service_id: Annotated[int, Path(example=1)],
    service: ServiceUpdate,
    stored_service: Annotated[ServicesTable, Depends(get_service_or_404)],
    db: Annotated[AsyncSession, Depends(get_db)]
):    
    for key, value in service.dict(exclude_unset=True).items():
        setattr(stored_service, key, value)

    await db.commit()
    await db.refresh(stored_service)

    return stored_service   
    
   
#удаляем услугу
@router.delete("/{service_id}")
async def delete_service(
    service: Annotated[ServicesTable, Depends(get_service_or_404)],
    db: Annotated[AsyncSession, Depends(get_db)]  
):
    await db.delete(service)
    await db.commit()
    
    return {"detail":"service was deleted succesfuly"}
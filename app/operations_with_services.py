from fastapi import Path, Body, Depends, APIRouter
from typing import Annotated, List
from app.schemas import Service, ServiceUpdate, ServiceWithoutId
from app.models import services, ServicesTable
from app.dependencies import get_service_or_404, get_db
from app.queries.orm import SyncOrm
from sqlalchemy.orm import Session

router = APIRouter(prefix="/services", tags=["Services"])

#читаем все услуги
@router.get("/", response_model=List[Service])
async def read_services(db: Annotated[Session, Depends(get_db)]):
    result = db.query(ServicesTable).all()
    return result

#читаем одну услугу
@router.get("/{service_id}", response_model=Service)
async def read_service(service:Annotated[ServicesTable, Depends(get_service_or_404)]):
    return service

#создаем услугу
@router.post("/", response_model=Service)
async def create_service(service: ServiceWithoutId, db:Annotated[Session, Depends(get_db)]):
    db_service = ServicesTable(
        name = service.name,
        description = service.description,
        price = service.price,
        duration = service.duration
    )
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service
    
#редактируем услугу
@router.put("/{service_id}", response_model = Service)
async def edit_service(
    service_id: Annotated[int, Path(example=1)],
    service: Annotated[ServiceUpdate, Body()],
    stored_service: Annotated[ServicesTable, Depends(get_service_or_404)],
    db: Annotated[Session, Depends(get_db)]
):    
    for key, value in service.dict(exclude_unset=True).items():
        setattr(stored_service, key, value)
    db.commit()
    db.refresh(stored_service)
    return stored_service   
    
   
#удаляем услугу
@router.delete("/{service_id}")
async def delete_service(
    service: Annotated[ServicesTable, Depends(get_service_or_404)],
    db: Annotated[Session, Depends(get_db)]  
):
    db.delete(service)
    db.commit()
    return {"detail":"service was deleted succesfuly"}
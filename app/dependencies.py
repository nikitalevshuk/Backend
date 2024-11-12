from app.schemas import Specialist, Service
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from app.models import services, specialists, ServicesTable, SpecialistsTable
from app.schemas import Service
from app.database import session_factory

#создаю сессию
def get_db():
    db = session_factory()
    try:
        yield db
    finally:
        db.close()

#чек существует ли специалист по айди
def get_specialist_or_404(specialist_id: int, db: Annotated[Session, Depends(get_db)]) -> SpecialistsTable:
    specialist = db.query(SpecialistsTable).filter(SpecialistsTable.id == specialist_id).first()
    if specialist is None:
        raise HTTPException(status_code=404, detail="Specialist not found")
    return specialist

#чек существует ли сервис по айди
def get_service_or_404(service_id: int, db: Annotated[Session, Depends(get_db)]) -> ServicesTable:
    service = db.query(ServicesTable).filter(ServicesTable.id == service_id).first()
    if service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return service
from app.schemas import Specialist, Service
from fastapi import HTTPException
from app.models import services, specialists

#чек существует ли специалист по айди
def get_specialist_or_404(specialist_id: int) -> Specialist:
    if specialist_id not in specialists:
        raise HTTPException(status_code=404, detail="Specialist not found")
    return Specialist(**specialists[specialist_id])

#чек существует ли сервис по айди
def get_service_or_404(service_id: int) -> Service:
    if service_id not in services:
        raise HTTPException(status_code=404, detail="Service not found")
    return Service(**services[service_id])
from fastapi import FastAPI, Body, Depends, HTTPException, APIRouter
from typing import Annotated, List
from app.schemas import Specialist
from app.models import specialists
from app.dependencies import get_specialist_or_404

router = APIRouter(prefix="/specialists", tags=["Specialists"])

#смотрим всех специалистов
@router.get("/") 
async def get_allSpecialists() -> List[Specialist]: 
    return list(specialists.values())

#смотрим только одного специалиста
@router.get("/{specialist_id}")
async def get_specialist(specialist:Annotated[Specialist, Depends(get_specialist_or_404)]) -> dict:
    return specialists[specialist.id]

#добавляем нового специалиста
@router.post("/")
async def create_specialist(new_specialist: Annotated[Specialist, Body(description="New specialist fields")]) -> Specialist:
    if new_specialist.id in specialists:
        raise HTTPException(status_code=400, detail="Specialist id is already exists")
    specialists[new_specialist.id] = new_specialist
    return new_specialist

#удаляем специалиста
@router.delete("/{specialist_id}")
async def delete_service(specialist: Annotated[Specialist, Depends(get_specialist_or_404)]) -> dict:
    del specialists[specialist.id]
    return {"detail": "Specialist deleted successfully"}
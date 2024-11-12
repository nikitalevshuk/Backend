from fastapi import FastAPI, Body, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import Annotated, List
from app.schemas import Specialist, SpecialistwithoutId
from app.models import specialists, SpecialistsTable
from app.dependencies import get_specialist_or_404, get_db

router = APIRouter(prefix="/specialists", tags=["Specialists"])

#смотрим всех специалистов
@router.get("/", response_model = List[Specialist]) 
async def get_all_specialists(db: Annotated[Session, Depends(get_db)]): 
    result = db.query(SpecialistsTable).all()
    return result

#смотрим только одного специалиста
@router.get("/{specialist_id}", response_model=Specialist)
async def get_specialist(specialist:Annotated[SpecialistsTable, Depends(get_specialist_or_404)]):
    return specialist 

#добавляем нового специалиста
@router.post("/", response_model=Specialist)
async def create_specialist(specialist:SpecialistwithoutId, db: Annotated[Session, Depends(get_db)]):
    new_specialist = (
        SpecialistsTable(name = specialist.name)
    )
    db.add(new_specialist)
    db.commit()
    db.refresh(new_specialist)
    return new_specialist

#удаляем специалиста
@router.delete("/{specialist_id}")
async def delete_service(specialist: Annotated[SpecialistsTable, Depends(get_specialist_or_404)], db: Annotated[Session, Depends(get_db)]):
    db.delete(specialist)
    db.commit()
    return {"detail":"specialist was deleted succesfuly"}
     
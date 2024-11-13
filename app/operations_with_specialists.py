from fastapi import Depends, APIRouter

from typing import Annotated, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import Specialist, SpecialistwithoutId
from app.models import SpecialistsTable
from app.dependencies import get_specialist_or_404, get_db

router = APIRouter(prefix="/specialists", tags=["Specialists"])

#смотрим всех специалистов
@router.get("/", response_model = List[Specialist]) 
async def get_all_specialists(db: Annotated[AsyncSession, Depends(get_db)]): 
    result = await db.execute(select(SpecialistsTable))
    specialists = result.scalars().all()

    return specialists

#смотрим только одного специалиста
@router.get("/{specialist_id}", response_model=Specialist)
async def get_specialist(specialist:Annotated[SpecialistsTable, Depends(get_specialist_or_404)]):
    return specialist 

#добавляем нового специалиста
@router.post("/", response_model=Specialist)
async def create_specialist(specialist:SpecialistwithoutId, db: Annotated[AsyncSession, Depends(get_db)]):
    new_specialist = (
        SpecialistsTable(name = specialist.name)
    )

    await db.add(new_specialist)
    await db.commit()
    await db.refresh(new_specialist)

    return new_specialist

#удаляем специалиста
@router.delete("/{specialist_id}")
async def delete_service(specialist: Annotated[SpecialistsTable, Depends(get_specialist_or_404)], db: Annotated[AsyncSession, Depends(get_db)]):
    await db.delete(specialist)
    await db.commit()

    return {"detail":"specialist was deleted succesfuly"}
     
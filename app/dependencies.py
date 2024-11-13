from typing import Annotated

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import HTTPException, Depends

from app.models import ServicesTable, SpecialistsTable
from app.database import async_session_factory

#создаю сессию
async def get_db():
    db = async_session_factory()
    try:
        yield db
    finally:
        await db.close()

#чек существует ли специалист по айди
async def get_specialist_or_404(specialist_id: int, db: Annotated[AsyncSession, Depends(get_db)]) -> SpecialistsTable:
    result = await db.execute(select(SpecialistsTable).where(SpecialistsTable.id == specialist_id))
    specialist = result.scalar_one_or_none()

    if specialist is None:
        raise HTTPException(status_code=404, detail="Specialist not found")
    
    return specialist

#чек существует ли сервис по айди
async def get_service_or_404(service_id: int, db: Annotated[AsyncSession, Depends(get_db)]) -> ServicesTable:
    result = await db.execute(select(ServicesTable).where(ServicesTable.id == service_id))
    service = result.scalar_one_or_none()

    if service is None:
        raise HTTPException(status_code = 404, detail = "Service not found")
    
    return service
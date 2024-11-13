from fastapi import FastAPI

from app.operations_with_services import router as services_router 
from app.operations_with_specialists import router as specialists_router
from app.queries.orm import SyncOrm, AsyncOrm

import asyncio
app = FastAPI()

# Подключаем роутеры
app.include_router(services_router)
app.include_router(specialists_router)





from fastapi import FastAPI

from app.dependencies import get_service_or_404, get_specialist_or_404
from app.operations_with_services import router as services_router 
from app.operations_with_specialists import router as specialists_router

app = FastAPI()
app.include_router(services_router)
app.include_router(specialists_router)


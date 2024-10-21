from fastapi import FastAPI, HTTPException, Path, Query, Body
from typing import Annotated, List, Optional

from app.schemas import Service
from app.models import services, specialists

app = FastAPI()

#читаем все услуги
@app.get("/services/", response_model = List[Service])
async def read_services():
    return list(services.values())





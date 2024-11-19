from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.operations_with_services import router as services_router 
from app.operations_with_specialists import router as specialists_router
from app.middleware import RateLimitMiddleware, SizeLimitMiddleware

app = FastAPI()

app.add_middleware(RateLimitMiddleware, max_requests = 10, window_seconds = 60)
app.add_middleware(SizeLimitMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_methods=['GET'],
    allow_headers=[],
    max_age = 600,
)


# Подключаем роутеры
app.include_router(services_router)
app.include_router(specialists_router)







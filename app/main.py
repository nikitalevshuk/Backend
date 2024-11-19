from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError, HTTPException

from app.operations_with_services import router as services_router 
from app.operations_with_specialists import router as specialists_router
from app.middleware import RateLimitMiddleware, SizeLimitMiddleware

app = FastAPI()

# Подключаем обработчики ошибок
app.add_middleware(RateLimitMiddleware, max_requests = 10, window_seconds = 60)
app.add_middleware(SizeLimitMiddleware)

# Подключаем роутеры
app.include_router(services_router)
app.include_router(specialists_router)







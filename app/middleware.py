from fastapi import Request, FastAPI

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from collections import defaultdict

import asyncio

import time

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_requests: int, window_seconds: int):
        super().__init__(app)
        self.max_requests = max_requests  # Максимальное количество запросов
        self.window_seconds = window_seconds  # Окно времени (в секундах)
        self.requests = defaultdict(list)  # Словарь {IP: [метки времени]}
        self.lock = asyncio.Lock()  # Для синхронизации

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host

        async with self.lock:
                current_time = time.time()

                # Очищаем старые запросы
                if client_ip in self.requests:
                    self.requests[client_ip] = [
                        timestamp for timestamp in self.requests[client_ip]
                        if current_time - timestamp < self.window_seconds
                    ]

                # Проверяем лимит запросов
                if len(self.requests[client_ip]) >= self.max_requests:
                    return JSONResponse(
                        status_code=429,
                        content={"detail": "Too many requests"}
                    )

                # Добавляем текущий запрос
                self.requests[client_ip].append(current_time)

        return await call_next(request)

        
    
class SizeLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI, max_size: int = 5*1024*1024):
        super().__init__(app)
        self.max_size = max_size

    async def dispatch(self, request: Request, call_next):
        content_length = request.headers.get("Content-Length")

        if content_length:
            content_length = int(content_length)
            if content_length > self.max_size:
                return JSONResponse(
                    status_code=413, 
                    detail="Request body is too large"
                )
        
        return await call_next(request)


    


    

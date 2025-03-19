"""
Точка входа FastAPI.
"""

from fastapi import FastAPI
from api.routes import expert

app = FastAPI(title="MediaisEcho API")

# Подключаем маршруты
app.include_router(expert.router, prefix="/api", tags=["Experts"])

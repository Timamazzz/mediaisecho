"""
Настройка подключения к базе данных.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from config import settings

# Создаем движок SQLAlchemy
engine = create_engine(settings.database.url, echo=settings.debug)

# Фабрика сессий для работы с БД
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

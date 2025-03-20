from datetime import datetime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, DateTime


class Base(DeclarativeBase):
    """Базовый класс для всех моделей SQLAlchemy"""

    id = Column(Integer, primary_key=True, index=True)
    """Уникальный идентификатор модели (целое число)."""

    created_at = Column(DateTime, default=datetime.now())
    """Дата и время создания записи."""

    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    """Дата и время последнего обновления записи."""

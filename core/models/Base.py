"""
Базовый класс для всех моделей в `core/models`.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Базовый класс для всех моделей SQLAlchemy"""
    pass

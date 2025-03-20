from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from core.models.Base import Base


class Category(Base):
    """Модель категории эксперта в БД"""

    __tablename__ = "categories"

    name = Column(String(200), unique=True, nullable=False)
    """Название категории (строка, обязательное поле, уникальное)."""

    # experts = relationship(
    #     "Expert",
    #     back_populates="categories",
    # )
    # """Связь с моделью Expert через многие ко многим."""

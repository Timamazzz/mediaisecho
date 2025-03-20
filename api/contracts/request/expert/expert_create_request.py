from pydantic import BaseModel
from typing import Optional


class ExpertCreateRequest(BaseModel):
    """Создание эксперта"""
    first_name: str
    """Имя эксперта (обязательное поле, строка)."""

    last_name: str
    """Фамилия эксперта (обязательное поле, строка)."""

    middle_name: Optional[str]
    """Отчество эксперта (необязательное поле, строка)."""

    description: str
    """Описание эксперта (обязательное поле, строка)."""

    class Config:
        json_schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "middle_name": "Smith",
                "description": "Expert in Python",
            }
        }
        from_attributes = True

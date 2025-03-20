from pydantic import BaseModel
from typing import Optional


class ExpertResponse(BaseModel):
    """Ответ при получении данных об эксперте."""

    id: int
    """Уникальный идентификатор эксперта (обязательное поле, целое число)."""

    first_name: str
    """Имя эксперта (обязательное поле, строка)."""

    last_name: str
    """Фамилия эксперта (обязательное поле, строка)."""

    middle_name: Optional[str] = None
    """Отчество эксперта (необязательное поле, строка)."""

    description: str
    """Описание эксперта (обязательное поле, строка)."""

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "first_name": "John",
                "last_name": "Doe",
                "middle_name": "Smith",
                "description": "Expert in Python",
            }
        }
        from_attributes = True

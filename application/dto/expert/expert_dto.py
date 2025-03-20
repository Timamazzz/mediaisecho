from pydantic import BaseModel
from typing import Optional


class ExpertDTO(BaseModel):
    """DTO для создания эксперта"""

    id: Optional[int] = None

    first_name: str
    """Имя эксперта (обязательное поле, строка)."""

    last_name: str
    """Фамилия эксперта (обязательное поле, строка)."""

    middle_name: Optional[str] = None
    """Отчество эксперта (необязательное поле, строка)."""

    description: str
    """Описание эксперта (обязательное поле, строка)."""

    class Config:
        from_attributes = True

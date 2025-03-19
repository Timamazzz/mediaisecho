from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.models.expert import Expert
from typing import List, Optional


class ExpertRepository:
    """Репозиторий для работы с экспертами в БД (асинхронный)"""

    def __init__(self, db: AsyncSession):
        """Принимаем асинхронную сессию БД через DI"""
        self.db = db

    async def get_expert(self, expert_id: int) -> Optional[Expert]:
        """Получает эксперта по ID"""
        result = await self.db.execute(select(Expert).filter(Expert.id == expert_id))
        return result.scalars().first()

    async def create_expert(self, expert_data: Expert) -> Expert:
        """Создает нового эксперта в базе данных"""
        self.db.add(expert_data)
        await self.db.commit()
        await self.db.refresh(expert_data)
        return expert_data

from typing import Optional
from infrastructure.repositories.expert_repo import ExpertRepository
from core.models.expert import Expert
from application.dto.expert.expert_dto import ExpertDTO


class ExpertService:
    """Сервис для работы с экспертами (асинхронный)"""

    def __init__(self, repo: ExpertRepository):
        """Принимаем репозиторий через DI"""
        self.repo = repo

    async def get_expert(self, expert_id: int) -> Optional[ExpertDTO]:
        """Получает эксперта по ID"""
        expert = await self.repo.get_expert(expert_id)
        if expert:
            return ExpertDTO.model_validate(expert)
        return None

    async def create_expert(self, expert_dto: ExpertDTO) -> ExpertDTO:
        """Создает нового эксперта"""
        expert = Expert(
            first_name=expert_dto.first_name,
            last_name=expert_dto.last_name,
            middle_name=expert_dto.middle_name,
            description=expert_dto.description
        )
        created_expert = await self.repo.create_expert(expert)
        return ExpertDTO.model_validate(created_expert)

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.database import AsyncSessionLocal
from infrastructure.repositories.expert_repo import ExpertRepository
from api.contracts.request.expert.expert_create_request import ExpertCreateRequest
from api.contracts.response.expert.expert_response import ExpertResponse
from application.dto.expert.expert_dto import ExpertDTO
from application.services.expert_service import ExpertService

router = APIRouter()


# DI: Создание сессии БД
def get_db():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        db.close()


# DI: Создание сервиса
def get_expert_service(db: AsyncSession = Depends(get_db)):
    repo = ExpertRepository(db)
    return ExpertService(repo)


@router.get("/experts/{expert_id}", response_model=ExpertResponse)
async def get_expert(expert_id: int, service: ExpertService = Depends(get_expert_service)):
    """Получает эксперта по ID"""
    return await service.get_expert(expert_id)


@router.post("/experts/", response_model=ExpertResponse)
async def create_expert(expert_data: ExpertCreateRequest, service: ExpertService = Depends(get_expert_service)):
    """Создает нового эксперта"""
    dto = ExpertDTO(
        first_name=expert_data.first_name,
        last_name=expert_data.last_name,
        middle_name=expert_data.middle_name,
        description=expert_data.description,
    )
    return await service.create_expert(dto)

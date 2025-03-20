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
async def get_db():
    async with AsyncSessionLocal() as db:
        yield db


# DI: Создание сервиса
def get_expert_service(db: AsyncSession = Depends(get_db)):
    repo = ExpertRepository(db)
    return ExpertService(repo)


@router.get("/experts/{expert_id}", response_model=ExpertResponse)
async def get_expert(expert_id: int, service: ExpertService = Depends(get_expert_service)):
    """Получает эксперта по ID"""
    expert_dto = await service.get_expert(expert_id)
    if expert_dto:
        return ExpertResponse.model_validate(expert_dto)
    return None


@router.post("/experts/", response_model=ExpertResponse)
async def create_expert(expert_data: ExpertCreateRequest, service: ExpertService = Depends(get_expert_service)):
    """Создает нового эксперта"""
    dto = ExpertDTO(
        first_name=expert_data.first_name,
        last_name=expert_data.last_name,
        middle_name=expert_data.middle_name,
        description=expert_data.description,
    )
    expert_dto = await service.create_expert(dto)
    return ExpertResponse.model_validate(expert_dto)

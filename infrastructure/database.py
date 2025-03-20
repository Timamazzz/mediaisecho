from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from config import settings

# Создаем асинхронный движок SQLAlchemy
engine = create_async_engine(settings.database.url, echo=settings.debug)

# Фабрика асинхронных сессий для работы с БД
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

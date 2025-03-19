"""
Глобальные настройки проекта, разбитые по модулям (по аналогии с Django).
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    """Настройки реляционной БД (PostgreSQL)"""

    name: str
    user: str
    password: str
    port: int
    host: str

    @property
    def url(self) -> str:
        """Генерация строки подключения к PostgreSQL"""
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class Settings(BaseSettings):
    """Объединенные настройки всего проекта"""

    debug: bool
    database: DatabaseSettings

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        extra="ignore"
    )


# Глобальный объект настроек
settings = Settings()

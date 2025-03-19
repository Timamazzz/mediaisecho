import os
import sys
import time
from alembic.config import Config
from alembic import command
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings  # Импорт настроек базы данных

# Настройка базы данных
DATABASE_URL = settings.database.url
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Путь к конфигурационному файлу alembic.ini
ALCHEMIC_CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'alembic.ini')


# Функция для создания новой миграции с автоматическим сообщением
def create_migration(message: str = None):
    """
    Создает новую миграцию с автоматической генерацией или с заданным сообщением.

    Если сообщение не передано, генерируется сообщение, включающее текущее время.

    :param message: Сообщение для миграции (по умолчанию None).
    """
    if not message:
        # Формируем сообщение, если не передано (используем дату и время)
        message = f"Migration_{time.strftime('%Y%m%d_%H%M%S')}"
    config = Config(ALCHEMIC_CONFIG_PATH)
    command.revision(config, message=message, autogenerate=True)


# Функция для применения всех миграций
def upgrade_migrations():
    """
    Применяет все миграции.
    """
    config = Config(ALCHEMIC_CONFIG_PATH)
    command.upgrade(config, 'head')


# Функция для отката к предыдущей миграции
def downgrade_migrations(version: str = None):
    """
    Откатывает к указанной версии или на одну миграцию назад.

    :param version: Версия для отката (по умолчанию None). Если не передано, откатываем на одну миграцию назад.
    """
    config = Config(ALCHEMIC_CONFIG_PATH)
    if version:
        command.downgrade(config, version)
    else:
        command.downgrade(config, '-1')  # Откатываем на одну миграцию назад


# Функция для получения текущей версии базы данных
def current_version():
    """
    Выводит текущую версию базы данных.
    """
    config = Config(ALCHEMIC_CONFIG_PATH)
    command.current(config)


# Функция для выполнения всех миграций
def run_migrations():
    """
    Выполняет все миграции, т.е. применяет все необработанные миграции.
    """
    print("Применение всех миграций...")
    upgrade_migrations()


if __name__ == "__main__":
    # Проверка на наличие команды, если команды нет, выводим help
    if len(sys.argv) < 2:
        print("Необходимо передать команду: create, upgrade, downgrade, current")
        print("Используйте флаг 'help' для получения информации о командах.")
        sys.exit(1)

    command_input = sys.argv[1].lower()

    # Флаг help для вывода информации о командах
    if command_input == "help":
        print("""
        Доступные команды:

        create [message]  - Создает новую миграцию с автоматическим или переданным сообщением.
                            Пример: python migrations.py create "Add expert table"

        upgrade           - Применяет все миграции к базе данных.

        downgrade [version] - Откатывает миграцию. Если версия не указана, откатывает на одну миграцию назад.
                             Пример: python migrations.py downgrade 1234567890ab

        current           - Выводит текущую версию базы данных.

        Пример использования:
        python migrations.py create
        python migrations.py upgrade
        python migrations.py downgrade
        python migrations.py current
        """)
        sys.exit(0)

    # Выполнение команды в зависимости от переданного аргумента
    if command_input == "create":
        if len(sys.argv) == 3:
            message = sys.argv[2]
            create_migration(message)
        else:
            create_migration()
    elif command_input == "upgrade":
        run_migrations()
    elif command_input == "downgrade":
        if len(sys.argv) == 3:
            version = sys.argv[2]
            downgrade_migrations(version)
        else:
            downgrade_migrations()
    elif command_input == "current":
        current_version()
    else:
        print("Неизвестная команда. Используйте флаг 'help' для получения информации.")

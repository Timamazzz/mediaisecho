# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

# Открываем порт для FastAPI
EXPOSE 8000

# Запускаем приложение
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

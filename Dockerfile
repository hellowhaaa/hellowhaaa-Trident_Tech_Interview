FROM python:3.11-slim

# 安裝 poetry
RUN pip install poetry==2.1.1

# 設定不使用虛擬環境
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

# 複製 pyproject 和 poetry.lock（用來安裝套件）
COPY pyproject.toml poetry.lock* ./

# 安裝依賴
RUN poetry install --no-root

# 複製整個專案
COPY . .

# 預設啟動 FastAPI 應用
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
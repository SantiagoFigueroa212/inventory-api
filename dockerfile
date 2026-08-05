FROM python:3.13-slim
WORKDIR /app
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY backend/ .
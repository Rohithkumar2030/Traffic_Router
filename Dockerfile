FROM python:3.9-alpine

WORKDIR /app

RUN pip install --no-cache-dir fastapi uvicorn

ARG APP_VERSION=v1
ENV VERSION=$APP_VERSION

COPY main.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
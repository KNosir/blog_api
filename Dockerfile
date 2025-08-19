FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    curl gcc libpq-dev build-essential git libffi-dev python3-pip postgresql-client

RUN pip install uv

WORKDIR /app

COPY pyproject.toml ./

RUN uv pip install --system .

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

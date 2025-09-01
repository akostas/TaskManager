FROM python:3.13.2-alpine3.21

WORKDIR /app

# Install system dependencies required for psycopg2
#RUN apt update && apt install -y --no-install-recommends gcc libpq-dev build-essential && rm -rf /var/lib/apt/lists/*
RUN apk add --no-cache \
    postgresql-dev \
    gcc \
    musl-dev \
    libffi-dev \
    python3-dev

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["python", "taskmanager/manage.py", "runserver", "0.0.0.0:8000"]
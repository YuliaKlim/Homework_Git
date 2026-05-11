FROM python:3.11-slim

RUN apt-get update && apt-get install -y libpq-dev gcc

WORKDIR /app

RUN pip install sqlalchemy psycopg2

COPY docker_homework_21_29.py .

CMD ["python", "docker_homework_21_29.py"]

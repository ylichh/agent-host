FROM python:3.11-slim

WORKDIR /app


RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir poetry

COPY pyproject.toml /app/

RUN poetry config virtualenvs.create false \
    && poetry install 


COPY ./app/ /app

CMD ["poetry", "run", "python3", "main.py"]
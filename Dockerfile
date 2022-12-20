FROM python:3.11

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

COPY .env /app/.env

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src /app/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000"]

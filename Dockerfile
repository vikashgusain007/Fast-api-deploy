FROM python:3.9-slim
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app /app

RUN pip install "fastapi[standard]"

EXPOSE 8000

CMD ["fastapi", "dev", "main.py"]

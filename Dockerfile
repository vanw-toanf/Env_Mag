FROM python:3.12-slim

WORKDIR /workspace

COPY requirements.txt .
RUN apt update && apt install -y gcc
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "6"]
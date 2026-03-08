# Dockerfile المعدل
FROM python:3.11-slim AS base

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    libespeak1 \
    espeak \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY run.py .

# Bake model weights into the image so Cloud Run doesn't need a volume
COPY yolov8n-pose.pt .

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

# Use shell form so $PORT is expanded (Cloud Run sets PORT env var)
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
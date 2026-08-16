# Base image
FROM python:3.11-slim

# Runtime environment
ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1 \
	PIP_NO_CACHE_DIR=1

# Set working directory
WORKDIR /app

# Install Python dependencies first for better layer caching
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy application source
COPY backend /app/backend
COPY frontend /app/frontend
COPY models /app/models

# Create and use an unprivileged user
RUN useradd --create-home --shell /usr/sbin/nologin appuser \
	&& chown -R appuser:appuser /app
USER appuser

# FastAPI port
EXPOSE 8000

# Start API
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
# Lightweight official Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Prevent Python from writing .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY hello.py .
COPY test_hello.py .
COPY evidently_monitor.py .

# Expose default port (if serving web API later)
EXPOSE 8000

# Default command: Execute hello.py
CMD ["python", "hello.py"]

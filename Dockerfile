# Lightweight official Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Prevent Python from writing .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy application files (Item 10: Add Hello.py to docker)
COPY hello.py .
COPY test_hello.py .

# Expose default port
EXPOSE 8000

# Default command: Execute hello.py
CMD ["python", "hello.py"]

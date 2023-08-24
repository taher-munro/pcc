
# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/engine/reference/builder/

# Use a specific Python version and the slim version of the base image
ARG PYTHON_VERSION=3.11.4
FROM python:${PYTHON_VERSION}-slim as base
RUN pip install --upgrade pip

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Disable stdout and stderr buffering
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Create a non-privileged user to run the application
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Copy the requirements.txt file and install dependencies
COPY requirements.txt requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

# Switch to the non-privileged user to run the application
USER appuser

# Copy the source code into the container
COPY . .

# Expose the port that the application listens on
EXPOSE 8000

# Run the application with gunicorn
CMD gunicorn 'venv.lib.python3.11.site-packages.fastapi.middleware.wsgi' --bind=0.0.0.0:8000

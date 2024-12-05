# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12.5

FROM python:${PYTHON_VERSION}-slim

# Add label for Fly.io runtime
LABEL fly_launch_runtime="flask"

# Set the working directory
WORKDIR /code

# Install system dependencies (essential for certain Python packages)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port Flask will run on
EXPOSE 8080

# Command to start the Flask app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080" ]

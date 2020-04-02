# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /dumpert

# Install dependencies
RUN pip install pipenv
COPY dumpert/requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY ./dumpert /code/
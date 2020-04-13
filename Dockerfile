# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install pipenv
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY ./dumpert /code/

EXPOSE 8080

CMD bash -c "python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --no-input && gunicorn dumpert.wsgi --bind 8080 --workers=5"
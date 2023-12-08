 # syntax=docker/dockerfile:1
        FROM python:3.8.13-slim-bullseye
        WORKDIR /application
        COPY /app /application
        COPY /blood /application
        COPY ./requirements.txt /application
        COPY /blood/settings /application/blood

        RUN pip install --no-cache-dir -r /application/requirements.txt
        
        EXPOSE 8080
        ENV PORT 8080
        ENV HOST 0.0.0.0
        ENV DJANGO_SETTINGS_MODULE=blood.settings
        CMD ["/bin/bash", "-c", "source blood/Scripts/activate && python manage.py runserver 0.0.0.0:8000"]
        ARG TIMEOUT=1600
        
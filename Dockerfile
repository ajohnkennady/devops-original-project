 # syntax=docker/dockerfile:1
        FROM python:3.8.13-slim-bullseye
        WORKDIR /application
        COPY /app /application
        COPY /blood /application
        COPY ./requirements.txt /application
        COPY ./manage.py /application
        RUN pip install --no-cache-dir -r /application/requirements.txt
        RUN pip install blood
        RUN python ./manage.py runserver
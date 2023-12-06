 # syntax=docker/dockerfile:1
        FROM python:3.8.13-slim-bullseye
        WORKDIR /app
        COPY ./requirements.txt /app
        COPY ./manage.py /app
        RUN pip install --no-cache-dir -r /app/requirements.txt
        RUN python ./app/manage.py runserver
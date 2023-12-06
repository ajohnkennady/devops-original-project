 # syntax=docker/dockerfile:1
        FROM python:3.8.13-slim-bullseye
        WORKDIR /app
        COPY ./requirements.txt /app
        COPY ./py_docker/ /app/py_docker
        RUN pip install --no-cache-dir -r /app/requirements.txt
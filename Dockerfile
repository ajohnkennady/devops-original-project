 # syntax=docker/dockerfile:1
        FROM python:3.8.13-slim-bullseye
        WORKDIR /application
        COPY /app /application
        COPY /blood /application
        COPY ./requirements.txt /application
        COPY ./manage.py /application

        RUN python -m venv venv
        RUN /bin/bash -c "source venv/bin/activate"
        RUN pip install /application/blood
        RUN pip install --no-cache-dir -r /application/requirements.txt
        ENV NAME blood
        EXPOSE 8080
        ENV PORT 8080
        ENV HOST 0.0.0.0
        CMD ["python", "./manage.py", "runserver"]
        ARG TIMEOUT=1600
        
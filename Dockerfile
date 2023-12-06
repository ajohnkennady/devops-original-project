 # syntax=docker/dockerfile:1
        FROM python:3.8.13-slim-bullseye
        WORKDIR /application
        COPY /app /application
        COPY /blood /application
        COPY ./requirements.txt /application
        COPY ./manage.py /application

        RUN python -m venv venv
        RUN /bin/bash -c "source venv/bin/activate"
        RUN pip install --no-cache-dir -r /application/requirements.txt
        ENV NAME blood
       CMD ["python", "./manage.py", "runserver"]
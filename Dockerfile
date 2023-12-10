 # syntax=docker/dockerfile:1
        FROM python:3.8.13-slim-bullseye
        RUN apt-get update \
             && apt-get install -y default-libmysqlclient-dev libmariadb-dev-compat libmariadb-dev pkg-config build-essential libssl-dev libffi-dev

          
        RUN pip install backports.zoneinfo==0.2.1
        WORKDIR /application
       
        COPY /blooddonation /application
        COPY ./requirements.txt /application
        RUN pip install python-dotenv
        RUN pip uninstall mysqlclient
        RUN pip install mysqlclient
        RUN pip install mysql-connector-python
        RUN  pip install --no-cache-dir -r /application/requirements.txt
        
        EXPOSE 8080
        ENV PORT 8080
        ENV HOST 0.0.0.0
        ENV DJANGO_SETTINGS_MODULE=blood.settings
        
        CMD ["/bin/bash", "-c", "source blood/blood/Scripts/activate && python manage.py runserver 0.0.0.0:8080"]
            
        ARG TIMEOUT=1600
        
FROM python:3.11.1-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install flask \
                flask-smorest\
                psycopg2-binary \
                flask-SQLAlchemy \
                marshmallow 

COPY . .

ENV FLASK_APP=app
ENV FLASK_DEBUG=1

EXPOSE 5000

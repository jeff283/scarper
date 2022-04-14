# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /scraper

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .



# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku			
CMD gunicorn --bind 0.0.0.0:$PORT wsgi 
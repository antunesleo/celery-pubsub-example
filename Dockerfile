FROM python:3.8

RUN apt-get update

RUN mkdir /celery-pubsub-example

COPY . /celery-pubsub-example/

WORKDIR /celery-pubsub-example

RUN pip3 install -r requirements.txt

FROM python:3.7-alpine
MAINTAINER Martijn Wip

# tell python to run in unbuffered mode
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# -D means create a user for running applications only
# This is recommended for security reasons. (Do not use the root user)
RUN adduser -D user
USER user

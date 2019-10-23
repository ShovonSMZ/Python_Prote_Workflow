FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /src

WORKDIR /src

RUN apt-get update && apt-get install -y libpq-dev gcc

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN apt-get autoremove -y gcc

COPY . /src/

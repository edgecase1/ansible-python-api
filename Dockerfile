FROM python:2.7

RUN apt-get update && apt-get install -y python-pip

ADD . /work

WORKDIR /work

RUN pip install -r requirements.txt


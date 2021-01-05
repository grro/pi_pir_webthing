FROM python:3.9.1-alpine

ENV port 9544
ENV name pir

RUN apk add build-base

ADD . /tmp/
WORKDIR /tmp/
RUN  python /tmp/setup.py install
WORKDIR /
RUN rm -r /tmp/

CMD pir --command listen --port $port --gpio $gpio --name $name
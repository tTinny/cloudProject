FROM python:3.8

RUN apt-get update

ADD . /home/src

WORKDIR /home/src

RUN pip3 install requests

CMD python3 load_generator.py

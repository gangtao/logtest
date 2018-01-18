FROM python:2.7.12

ENV CODE_HOME /home/test

RUN mkdir $CODE_HOME
COPY ./src $CODE_HOME

WORKDIR $CODE_HOME

ENTRYPOINT ["python","main.py"]
FROM ubuntu
FROM python:3.6.5
ADD . /microverse
WORKDIR /microverse
RUN pip install -r requirements.txt

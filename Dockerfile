FROM python:3.6.5
ADD . /todo
WORKDIR /todo
RUN pip install -r requirements.txt

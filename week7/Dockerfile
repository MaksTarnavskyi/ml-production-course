FROM python:3.8.3

WORKDIR /app

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


ENV PYTHONPATH /app
COPY . . 

CMD [ "bash" ]

FROM python:3.8-slim-buster

# set a directory for the app
WORKDIR /usr/src/app

# copy requirements
COPY requirements.txt requirements.txt

# install dependencies
RUN pip install -r requirements.txt

ENV PYTHONPATH /usr/src/app
COPY . . 

RUN mkdir output/data

CMD ["python", "./app.py"]

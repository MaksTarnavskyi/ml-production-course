FROM python:3.8-slim-buster
RUN useradd --create-home appuser
USER appuser

# set a directory for the app
WORKDIR /usr/src/app

# copy requirements
COPY requirements.txt requirements.txt

# install dependencies
RUN pip install -r requirements.txt --user

ENV PYTHONPATH /usr/src/app
COPY . . 

CMD [ "bash" ]
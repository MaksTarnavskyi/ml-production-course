FROM python:3.8-slim-buster
RUN useradd --create-home appuser
USER appuser

# set a directory for the app
WORKDIR /usr/src/app

# copy requirements
COPY week1/flask-app/requirements.txt requirements.txt

# install dependencies
RUN pip install -r requirements.txt --user

# copy all other files to the container
COPY week1/flask-app .

# tell the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "./app.py"]

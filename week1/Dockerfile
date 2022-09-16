FROM python:3.8-slim-buster
RUN useradd --create-home appuser
USER appuser

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY flask-app .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt --user

# tell the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "./app.py"]

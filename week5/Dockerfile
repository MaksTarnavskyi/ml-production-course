# Base docker image
FROM python:3.8.3 as base

WORKDIR /app

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN pip install pip --upgrade 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV PYTHONPATH /app
COPY . . 

CMD [ "bash" ]

# Streamlit UI docker image
FROM base AS app-streamlit
CMD streamlit run --server.address 0.0.0.0 --server.port 8080 serving/streamlit_app.py

# Fast API docker image
FROM base AS app-fastapi
CMD uvicorn --host 0.0.0.0 --port 8080 --workers 4 serving.fast_api:app

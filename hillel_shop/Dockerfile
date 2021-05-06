FROM python:3-slim as base
WORKDIR /shop
ENV PYTHONUNBUFFERED True
COPY requirements.txt .
RUN pip install -r requirements.txt


FROM base as dev
COPY src/ .


FROM dev
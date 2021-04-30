FROM python:3-slim as base
WORKDIR /shop
COPY hillel_shop/requirements.txt .
RUN pip install -r requirements.txt


FROM base as dev
COPY hillel_shop/src/ .


FROM dev
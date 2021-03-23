# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev \
    musl-dev libffi-dev libc-dev linux-headers openssl-dev cargo

# install dependencies
RUN pip install --upgrade pip
RUN pip install cryptography
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT [ "/usr/src/backend/entrypoint.sh" ]
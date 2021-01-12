[![Build Status](https://travis-ci.com/prog-serhii/MyMoney_v2.svg?branch=main)](https://travis-ci.com/prog-serhii/MyMoney_v2)
# MyMoney
A web application for budget tracking and money management.

## About the Developer
MyMoney was created by Serhii Kazmiruk

## Features
1.
2.
3.

## Built with
* Front-end:
* Back-end: 

## Demo
.....

Build the image:
docker-compose build


Once the image is built, run the container:

docker-compose up -d


or

docker-compose up -d --build


Bring down the development containers (and the associated volumes with the -v flag):

docker-compose down -v

Celery:

celery -A project worker -l info
celery -A project beat -l info
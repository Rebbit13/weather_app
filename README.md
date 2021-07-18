This is a test web service for get weather forecast in diferent towns

Main libraries

Python 3.9.1 (you should use python > 3.9)
Uvicorn as a server
Fast-api as an api module
Pydantic for validation
Sqlalchemi as an ORM for postgresql
Alumbic for migrations
Redis for cash
Jinja2 for templates


Deployment of the app via docker-compose in *nix
Go to the app dir and
run the command:

cp ./example.env ./.env

Change environment vars if you need and then:

sudo docker-compose up

Rebbit13

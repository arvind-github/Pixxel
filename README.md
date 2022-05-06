# Implementation of REST API for Spatial Data

Spatial Data is a application implementing CRUD operation developed using Django Framework. Rabbit Queue is using API provided by Django Application to store the geojson data into the DB.

## Set up Application
### Prerequisite:
Docker and Docker Compose should be installed to run the following - 
### Follow below step to setup and run the application:
- Replace "machine_ip" with the ip address of your machine in publish.py and subscribe.py
- git clone https://github.com/arvind-github/Pixxel.git 
- cd Pixxel
- Run : docker-compose build
- Run : docker-compose run web python manage.py makemigrations crud
- Run : docker-compose run web python manage.py migrate
- Run : docker run -d --rm -it -p 15672:15672 -p 5672:5672 rabbitmq:3-management
- Run : docker-compose up -d


## API's Exposed
- GET : http://127.0.0.1:8000/api/crud/
- POST : http://127.0.0.1:8000/api/crud/
- PUT : http://127.0.0.1:8000/api/crud/India
- DELETE : http://127.0.0.1:8000/api/crud/India
- NON SPATIAL API : http://127.0.0.1:8000/api/nspa/India
- SPATIAL API : http://127.0.0.1:8000/api/spa

## How to test the Application

- pip install pytest
- pip install requests
- pytest tests.py


## License
[MIT](https://choosealicense.com/licenses/mit/)

# Implementation of REST API for Spatial Data

Spatial Data is a application implementing CRUD operation developed using Django Framework. Rabbit Queue is using API provided by Django Application to store the geojson data into the DB.

## Set up Application

Docker and Docker Compose should be installed to run the following - 
docker-compose up


## How to test the CRUD Operation

CREATE
```python
import requests

obj = {
            "country": "India",
            "iso_a3": "ATQ",
            "type": "Polygon",
            "coordinates": [ -70.048736131999931, 12.632147528000104 ]
        }

x = requests.post("http://127.0.0.1:8000/api/crud/", data=obj)
print(x.text)
```

### GET, UPDATE, DELETE :
Run on browser:

http://127.0.0.1:8000/api/crud/India

http://127.0.0.1:8000/api/crud/


## License
[MIT](https://choosealicense.com/licenses/mit/)

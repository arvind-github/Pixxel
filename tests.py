import pytest
import requests
import json

url = "http://machine_ip:8000/api/crud/"
def test_get_request():
   response = requests.get(url)
   assert response.status_code == 200

def test_post_request():
   data = { "type": "Feature", "properties": { "ADMIN": "dummy", "ISO_A3": "ABW" }, "geometry": { "type": "Polygon", "coordinates": [ [ [ -69.996937628999916, 12.577582098000036 ], [ -70.060373501999948, 12.556952216000113 ], [ -70.051096157999893, 12.574042059000064 ], [ -70.048736131999931, 12.583726304000024 ], [ -70.052642381999931, 12.600002346000053 ], [ -70.059641079999921, 12.614243882000054 ], [ -70.061105923999975, 12.625392971000068 ], [ -70.048736131999931, 12.632147528000104 ], [ -70.00715084499987, 12.5855166690001 ], [ -69.996937628999916, 12.577582098000036 ] ] ] } }
   headers = {'Content-type': 'application/json'}
   response = requests.post(url, data=json.dumps(data), headers=headers)
   response_body = response.json()
   assert response_body["message"] == "Record Created Successfully"

def test_put_request():
   data = { "type": "Feature", "properties": { "ADMIN": "dummy", "ISO_A3": "ABW" }, "geometry": { "type": "Polygon", "coordinates": [ [ [ -69.996937628999916, 12.577582098000036 ], [ -70.060373501999948, 12.556952216000113 ], [ -70.051096157999893, 12.574042059000064 ], [ -70.048736131999931, 12.583726304000024 ], [ -70.052642381999931, 12.600002346000053 ], [ -70.059641079999921, 12.614243882000054 ], [ -70.061105923999975, 12.625392971000068 ], [ -70.048736131999931, 12.632147528000104 ], [ -70.00715084499987, 12.5855166690001 ], [ -69.996937628999916, 12.577582098000036 ] ] ] } }
   headers = {'Content-type': 'application/json'}
   response = requests.put(url +"dummy", data=json.dumps(data), headers=headers)
   response_body = response.json()
   assert response_body["message"] == "Record Updated Successfully"

def test_post_duplicate_country():
   data = { "type": "Feature", "properties": { "ADMIN": "dummy", "ISO_A3": "ABW" }, "geometry": { "type": "Polygon", "coordinates": [ [ [ -69.996937628999916, 12.577582098000036 ], [ -70.060373501999948, 12.556952216000113 ], [ -70.051096157999893, 12.574042059000064 ], [ -70.048736131999931, 12.583726304000024 ], [ -70.052642381999931, 12.600002346000053 ], [ -70.059641079999921, 12.614243882000054 ], [ -70.061105923999975, 12.625392971000068 ], [ -70.048736131999931, 12.632147528000104 ], [ -70.00715084499987, 12.5855166690001 ], [ -69.996937628999916, 12.577582098000036 ] ] ] }  }
   headers = {'Content-type': 'application/json'}
   response = requests.post(url, data=json.dumps(data), headers=headers)
   response_body = response.json()
   assert response_body["ADMIN"][0] == "spatial data with this ADMIN already exists."

def test_delete_request():
   response = requests.delete(url + "dummy")
   assert response.status_code == 200


def test_check_content_type_equals_json():
   response = requests.get(url)
   assert response.headers["Content-Type"] == "application/json"

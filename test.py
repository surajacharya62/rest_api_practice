import requests

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'jsonapicbv'

response = requests.get(BASE_URL + ENDPOINT)
responsed_data = response.json()
print('Employe number:',responsed_data["eno"])

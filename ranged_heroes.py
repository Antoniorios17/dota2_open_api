import requests
import json


url = "https://api.opendota.com/api/heroes"

data = requests.get(url).json()

print(data[0])
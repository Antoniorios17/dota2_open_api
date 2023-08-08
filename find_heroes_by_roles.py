import requests
import json


url = "https://api.opendota.com/api/heroes"

data = requests.get(url).json()

# print(data)

for hero in data:
    if "Carry" in hero['roles']:
        print(hero['id'],hero['localized_name'])
        
import requests
import json


url = "https://api.opendota.com/api/heroes"

data = requests.get(url).json()

ranged_heroes = 0
for hero in data:
    if hero['attack_type'] == "Ranged":
        print(hero["id"], hero["attack_type"], hero["localized_name"])
        ranged_heroes +=1
print(f"The number of heroes is {ranged_heroes}")
import requests
import json


url = "https://api.opendota.com/api/heroes"

data = requests.get(url).json()

ranged_heroes = 0
for heroe in data:
    if heroe['attack_type'] == "Ranged":
        print(heroe["id"], heroe["attack_type"], heroe["localized_name"])
        ranged_heroes +=1
print(f"The number of heroes is {ranged_heroes}")
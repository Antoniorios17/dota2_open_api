import requests
import json
import pandas as pd

url = "https://api.opendota.com/api/heroes"

data = requests.get(url).json()

list_of_heroes = []
ranged_heroes = 0
for hero in data:
    if hero['attack_type'] == "Ranged":
        heroes = hero["id"], hero["attack_type"], hero["localized_name"]
        list_of_heroes.append(heroes)
        ranged_heroes +=1
# print(f"The number of heroes is {ranged_heroes}")

# create df for the data

df = pd.DataFrame(list_of_heroes, columns=["id", 'type', 'name']) # add column names

print(df)
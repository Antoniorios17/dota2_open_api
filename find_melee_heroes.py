import requests
import json

url = "https://api.opendota.com/api/heroes"

response = requests.get(url)

data = response.json()

#Find the number of meele heroes dota 2 

melee_counter = 0
for hero in data:
    if hero['attack_type'] == 'Melee':
        print(hero['id'], hero['localized_name'], hero['attack_type'])
        melee_counter +=1

print(f"the number of melee heroes in Dota 2 is {melee_counter}")


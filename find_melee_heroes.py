import requests
import json

url = "https://api.opendota.com/api/heroes"

response = requests.get(url)

data = response.json()

#Find the number of meele heroes dota 2 

melee_counter = 0
for heroe in data:
    if heroe['attack_type'] == 'Melee':
        print(heroe['id'], heroe['localized_name'], heroe['attack_type'])
        melee_counter +=1

print(f"the number of melee heroes in Dota 2 is {melee_counter}")


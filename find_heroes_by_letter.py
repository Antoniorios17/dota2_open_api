import requests
import json

url = "https://api.opendota.com/api/heroes"

response = requests.get(url)

data = response.json()

def hero_by_letter(letter):
    print(f"Heroes that start with {letter} are: ")
    for hero in data:       
        if hero['localized_name'][0].lower() == letter:
            hero_traits = [hero['id'], hero['localized_name'],hero['attack_type'] ]
            print(hero_traits)
     

letter = input("Please enter a letter: ")
print("")
print(hero_by_letter(letter))
    
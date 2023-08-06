import requests
import json


url = "https://api.opendota.com/api/heroes"

list_of_heroes = requests.get(url).json()



total_list = []
melee_list = []


def range_hero(entry):
    ranged_list = []
    if entry[0].lower() == "r":
        for hero in list_of_heroes:
            if hero['attack_type'] == "Ranged":
                new_hero = hero['id'], hero['name'][14:].upper(), hero['attack_type']
                ranged_list.append(new_hero)
    return ranged_list

while True:
    user_input = input('Please enter the type of hero you want: (Range/Melee) ')
    if user_input == "r":
        ranged_list = range_hero(user_input)
        print(ranged_list)
    
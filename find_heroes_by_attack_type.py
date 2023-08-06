import requests
import json


url = "https://api.opendota.com/api/heroes"

list_of_heroes = requests.get(url).json()

# this function will gather the information such as name, id and attack type for all ranged heroes
# it will return a list of list of all heroes that fit in the category

def range_hero(entry):
    ranged_list = []
    if entry[0].lower() == "r":
        for hero in list_of_heroes:
            if hero['attack_type'] == "Ranged":
                new_hero = [hero['id'],hero['name'][14:].upper(), hero['attack_type']]
                ranged_list.append(new_hero)
    return ranged_list

def melee_hero(entry):
    melee_list = []
    if entry[0].lower() == "m":
        for hero in list_of_heroes:
            if hero['attack_type'] == "Melee":
                new_hero = [hero['id'],hero['name'][14:].upper(), hero['attack_type']]
                melee_list.append(new_hero)
    return melee_list

while True:
    user_input = input('Please enter the type of hero you want: (Range/Melee) ')
    if user_input == "r":
        ranged_list = range_hero(user_input)
        print(ranged_list)
    elif user_input == "m":
        melee_list = melee_hero(user_input)
        print(melee_list)
    elif user_input == "exit":
        break



    
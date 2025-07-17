import requests
import json
import pandas as pd

url = "https://api.opendota.com/api"

data = requests.get(url).json()

# print(data["openapi"])
# print(data["info"])

print(data.keys())
print(data["components"].keys())
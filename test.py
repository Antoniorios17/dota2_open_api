import requests
import json
import pandas as pd

url = "https://api.opendota.com/api/heroes"

data = requests.get(url).json()
print(data)
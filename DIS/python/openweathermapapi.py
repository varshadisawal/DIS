#https://openweathermap.org/forecast5#geo5

import requests
import json
import pandas as pd

key = "51de08d7fc9bfbc15136270d5738855f"

data = {"lat": -39.809,
        "lon": -16.787,
        "model": "gfs",
        "parameters": ["wind"],
        "key": key
        }

header = {"Content-Type" :"application/json"}

url = "https://api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99&appid="
print(url+key)
r = requests.get(url+key)
print(r.status_code)
data = r.json()

print(json.dumps(data,indent=2))

f = open("./data/data.json","w")
f.write(json.dumps(data))
f.close
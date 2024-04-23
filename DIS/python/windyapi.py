#https://api.windy.com/point-forecast/docs


import requests
import json

key = "QagKTvhl3kEpGeCFVBFDsDkdYG60VuSy"

data = {"lat": -39.809,
        "lon": -16.787,
        "model": "gfs",
        "parameters": ["wind"],
        "key": key
        }

header = {"Content-Type" :"application/json"}

url = "https://api.windy.com/api/point-forecast/v2"

r = requests.post(url, json=data, headers = header)

data = r.json()
print(json.dumps(data,indent=2))
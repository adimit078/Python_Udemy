# api use

import requests

response = requests.get(url = "http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()["iss_position"]
iss_pos = (data["latitude"], data["longtitude"])
print(iss_pos)


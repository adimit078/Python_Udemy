# api use

import requests
from datetime import datetime

response = requests.get(url = "http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()["iss_position"]
iss_pos = (data["latitude"], data["longitude"])
print(iss_pos)

MY_LAT = 42.440498
MY_LONG = -76.495697

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

responses = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
responses.raise_for_status()
data = responses.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise, sunset)

time_now = datetime.now()

print(time_now.hour)


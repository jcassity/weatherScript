import requests
from twilio.rest import Client
import keys

# url
URL = "http://api.openweathermap.org/data/2.5/weather?"

# params
id = "4076607"
units = "imperial"
PARAMS = {'id':id, 'units':units, 'APPID':keys.key}

# request
r = requests.get(url = URL, params = PARAMS) 
results = r.json()

# get output from json data
temp = results["main"]["feels_like"]
weatherMain = results["weather"][0]["main"]
weatherDescription = results["weather"][0]["description"]

# handle logic for email response
if temp < 60:
    jacket = "It's a bit cold, you may want to grab a jacket!"
else:
    jacket = "Leave the jacket at home!"
if weatherMain == "rain":
    rain = "Looks like rain, you may want an umbrella!"
else:
    rain = "No rain today!"

output = "Weather:  {} --- {} --- {}f --- \n {} \n {}"
msg = output.format(weatherMain, weatherDescription, temp, jacket, rain)

print(msg)

client = Client(keys.sid, keys.tok)

message = client.messages.create(
    to="+12514426537", 
    from_="+12623957799",
    body=msg)

print(message.sid)


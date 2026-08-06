# API : An API is a set of commands,  funtions, protocls and objects which
# can use by programmerto create or interact with an external system

# API ENdpoint :
# International Space Station Current Location
# http://api.open-notify.org/iss-now.json  any link like this is the end point of th API.


# API Request : not preloaded need to install
import requests
respones = requests.get(url="http://api.open-notify.org/iss-now.json")


# Working with Respones : HTTP Codes, Exceptions, & JOSN data

# Respones code :
# 1xx : hold on
# 2xx : here you go
# 3xx : o away
# 4xx : you screwed up Me
# 5xx : i screwed up
print (respones.status_code)
if respones.status_code != 200:
    respones.raise_for_status()

data = respones.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)

# HTTP Codes



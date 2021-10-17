import requests
import json

#https://github.com/javieraviles/covidAPI


data = requests.get("https://coronavirus-19-api.herokuapp.com/countries")
data = data.text
data = json.loads(data)

print(data[1])
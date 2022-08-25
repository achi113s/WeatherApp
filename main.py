import requests
import creds
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

def get_weather(zipcode: str) -> dict:
    APICALL = f'https://api.openweathermap.org/data/2.5/weather'
    # GET method at url, params is the set of extra variables for the api, returns a JSON object
    payload = {'zip': zipcode, 'appid': creds.APIKEY, 'units': 'imperial'}
    resp = requests.get(APICALL, params=payload)

    if resp.status_code != 200:
        # something went wrong
        print(f'Something went wrong. Error code {resp.status_code}.')
    else:
        # success getting weather forecast
        return resp.json()

# zipcode = '23322'
# weather = get_weather(zipcode)
# temperature = weather['main']['temp']
# print(f'The temperature in {zipcode} is {temperature} degrees Fahrenheit.')
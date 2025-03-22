import os
import requests


API_KEY = os.environ['API_KEY']
def get_current_weather(city: str, key=API_KEY):
    base_url = 'http://api.weatherapi.com/v1/current.json'
    params = {
        'key': API_KEY,
        'q': city
    }
    response = requests.get(base_url, params=params)
    data  = response.json()

    if 'error' in data:
        print(data['error']['message'])
    else:
        print(f"Weather in {data['location']['name']} ({data['location']['country']})")
        print(f"Temperature: {data['current']['temp_c']}°C (feels like {data['current']['feelslike_c']})")
        print(f"Condition: {data['current']['condition']['text']}")
        print(f"Humidity: {data['current']['humidity']}%")
        print(f"Wind: {data['current']['wind_kph']}kp/h")
        print(f"Wind direction: {data['current']['wind_dir']}")
        print(f"Atmosphere pressure: {data['current']['pressure_mb']} mb")


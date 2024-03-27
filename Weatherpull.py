import requests
import json

def get_weather(city: str, api_key: str) -> dict:
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
    }
    response = requests.get(base_url, params=params)
    return response.json()

def main():
    city = input("Enter the name of a city: ")
    api_key = input("Enter your OpenWeatherMap API Key: ")
    weather_data = get_weather(city, api_key)
    print(json.dumps(weather_data, indent=4))

if __name__ == "__main__":
    main()

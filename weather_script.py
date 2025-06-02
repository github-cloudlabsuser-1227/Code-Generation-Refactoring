import requests

API_KEY = 'ce833ae874217d52234fd83e38156430'  # Replace with your actual OpenWeatherMap API key
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()

def display_weather(data, city):
    weather_desc = data['weather'][0]['description'].capitalize()
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    print(f"\nWeather in {city}: {weather_desc}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

if __name__ == '__main__':
    city = input("Enter city name: ")
    try:
        weather = get_weather(city)
        display_weather(weather, city)
    except requests.HTTPError as e:
        print("Failed to fetch weather data:", e)
    except KeyError:
        print("Unexpected response format. Please check the city name and try again.")
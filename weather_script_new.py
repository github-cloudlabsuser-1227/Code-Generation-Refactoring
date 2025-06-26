# Fetch weather data from OpenWeatherMap API
import requests

API_KEY = "your_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
def display_weather(data, city):
    if data:
        weather_desc = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        print(f"\nWeather in {city}: {weather_desc}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found or API request failed.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    try:
        weather_data = get_weather(city)
        display_weather(weather_data, city)
    except requests.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"Error fetching weather data: {e}")


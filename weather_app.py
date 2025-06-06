import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            print(f"\nWeather in {data['name']}, {data['sys']['country']}:")
            print(f"🌡 Temperature: {data['main']['temp']}°C")
            print(f"🌥 Description: {data['weather'][0]['description'].title()}")
            print(f"💧 Humidity: {data['main']['humidity']}%")
            print(f"🌬 Wind Speed: {data['wind']['speed']} m/s")
        else:
            print(f"\n❌ Error: {data['message'].capitalize()}")

    except requests.exceptions.RequestException as e:
        print(f"\n❌ Connection Error: {e}")

if __name__ == "__main__":
    print("=== Weather App (OpenWeatherMap) ===")
    city_name = input("Enter city name: ")
    api_key = "030e4321d872dcd110eded59ec659241"  # <--  API key
    get_weather(city_name, api_key)

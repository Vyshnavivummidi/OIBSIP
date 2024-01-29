import requests

def get_weather(api_key, city, country_code=''): 
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': f'{city},{country_code}',
        'appid': api_key
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_info = {
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
            }
            return weather_info
        else:
            print(f"Error: {data['message']}")
            return None

    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def main():
    api_key = 'f4e757f49c02c8b3a694a4c3ca2583ac'
    city = input("Enter the city name: ")
    country_code = input("Enter the country code (optional, press Enter to skip): ")

    weather_data = get_weather(api_key, city, country_code)

    if weather_data:
        print("\nWeather Report:")
        print(f"Temperature: {weather_data['temperature']} K")
        print(f"Description: {weather_data['description']}")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")

if __name__ == "__main__":
    main()

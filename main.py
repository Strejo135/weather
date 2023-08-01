import json
import requests
base_url = "https://api.openweathermap.org/data/2.5/weather"
appid = "2ec79a00339bc6a28e91f8597bf02fec"
def get_weather_data(location):
    try:
        # Check if location is a zip code or a city name
        if location.isdigit() and len(location) == 5:
            url = f"{base_url}?zip={location}&appid={appid}"
        else:
            url = f"{base_url}?q={location}&appid={appid}"
        
        # Send GET request to OpenWeather API and parse response
        response = requests.get(url)
        data = json.loads(response.text)
        # Check if API returned an error message
        if data["cod"] != 200:
            print(f"Error: {data['message']}")
            return None
        
        # Return data
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
def display_data(data):
    if data is None:
        return
    
    location = data["name"]
    description = data["weather"][0]["description"]
    temp_k = data["main"]["temp"]
    temp_c = temp_k - 273.15
    temp_f = (temp_c * 9/5) + 32
    feels_k = data["main"]["feels_like"]
    feels_c = feels_k - 273.15
    feels_f = (feels_c * 9/5) + 32
    
    print(f"Location: {location}")
    print(f"Description: {description}")
    print(f"Temperature: {temp_f:.1f}°F")
    print(f"Feels like: {feels_f:.1f}°F")
# Prompt the user for input
location = input("Enter a zip code or city name: ")
# Call the get_weather_data function with the user-provided location
data = get_weather_data(location)
# Display weather data
display_data(data)
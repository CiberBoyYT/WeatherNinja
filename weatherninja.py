import requests

def get_weather(city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] == "404":
        print("city not found.")
    else:
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        humidity = main["humidity"]
        description = weather["description"]
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")
api_key = input("enter your openweathermap api key: ")
city = input("enter city name: ")
get_weather(city)

import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "68134ac462d814a7f02c20b1f3810ff7"
CITY = "Siliguri, IN"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

def KelvinToCelsius(kelvin):
    celsius = kelvin - 273.15
    return round(celsius, 2)

def GetWheatherReport():
    temp = KelvinToCelsius(response['main']['temp'])
    feelslike = KelvinToCelsius(response['main']['feels_like'])
    temp_min = KelvinToCelsius(response['main']['temp_min'])
    temp_max = KelvinToCelsius(response['main']['temp_max'])
    weather_type = response['weather'][0]['description']

    return temp, feelslike, temp_min, temp_max, weather_type

# print(response)
# print(f"Weather type: {GetWheatherReport()[4]}")
# print(f"Temperatue: {GetWheatherReport()[0]} °C")
# print(f"Feels Like: {GetWheatherReport()[1]} °C")
# print(f"Minimum temperature: {GetWheatherReport()[2]} °C")
# print(f"Maximum temperature: {GetWheatherReport()[3]} °C")
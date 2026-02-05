import requests
from pprint import pprint
import datetime
import csv

# """ Create a function according to weather data

def generate_sustainable_tip(temp, weather, clouds, city):
    is_raining = weather == "Rain"
    is_hot = temp >= 28
    is_warm_no_rain = temp >15 and weather != "Rain"
    is_cold = temp < 15


# Limiting temperature decimal values:
    temp_str = str(temp)[:4]

#  Create message with sustainable tip:
    if is_raining:
        return f"the temperature in {city} is {temp_str}°C. Take this chance to collect some rainwater and use it later to water your plants."
    if is_hot:
        return f"the temperature in {city} is {temp_str}°C. It's a great time to take a cool shower and save on hot water."
    if is_warm_no_rain:
        return f"the temperature in {city} is {temp_str}°C with {clouds}% cloud coverage, and no rain. It's a perfect day to dry your clothes outside and save energy on the dryer."
    if is_cold :
        return f"the temperature in {city} is {temp_str}°C. It's a cold day, so wear layers to stay warm without turning on the heater."
    else:
        return f"the temperature in {city} is {temp_str}°C with {clouds}% cloud coverage. Remember to use energy wisely today!"

#  Define endpoint and APIkey

api_key = # You need to create your API Key as stated in READEME file
endpoint = "http://api.openweathermap.org/data/2.5/weather"
response = requests.get(endpoint)

#  Define city, payload and response request
print ('Enter the name of the city you would like to query, or type "Exit" to quit. ')

while True:
    city = input("City: ")
    if city.lower() == "exit": # compare and transform EXIT or exit variations
        print("Your query has been saved.")
        break # ends the loop

# OpenWeather API request
    payload = {
    "q": city,
    "units": "metric",
    "APPID": api_key,
    }
    response = requests.get(url = endpoint, params=payload)
    data = response.json()

# Query Date and time
    now = datetime.datetime.now()
    hour_date = now.strftime("%d/%m/%Y at %H:%M:%S, ")

# Check if the response was successful and the city was founded
    if response.status_code != 200 or "main" not in data:
        message = f"{city} was not found. Please try again."
    else:
        temp = data["main"]["temp"]
        weather = data["weather"][0]["main"]
        clouds = data["clouds"]["all"]
        message = f"On {hour_date}" + generate_sustainable_tip(temp, weather, clouds, city)

    print(message)

# Create a txt ans csv file with your query:

    with open("cities_data.csv", "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([hour_date, city, temp])

    with open("sustainable_tips.txt", "a", encoding="utf-8") as file:
         file.write(message + "\n")







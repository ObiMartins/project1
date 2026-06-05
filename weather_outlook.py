
#Paris weather API example
import requests

#Search for Paris coordinates
def weather_report():
    url = ("https://api.open-meteo.com/v1/forecast"
        "?latitude=48.85341"
        "&longitude=2.3488"
        "&current=temperature_2m,relative_humidity_2m,wind_speed_10m")


    #Printing the entire response before accessing current
    #response = requests.get(url)
    #data = response.json()
    #print(data)

    response = requests.get(url).json()
    current = response["current"]

    print("=================Paris Weather result========================")
    print(f"Temperature: {current['temperature_2m']} °C")
    print(f"Humidity: {current['relative_humidity_2m']} %")
    print(f"Wind: {current['wind_speed_10m']} m/s")

    #ASABA Weather Temperature
    url = ("https://api.open-meteo.com/v1/forecast"
        "?latitude=6.2214413"
        "&longitude=6.6973243"
        "&current=temperature_2m")

    #Printing the entire response before accessing current
    #response_2 = requests.get(url)
    #data = response_2.json()
    #print(data)

    response_2 = requests.get(url).json()
    current_2 = response_2["current"]
    print("=================ASABA Weather result========================")
    print(f"Temperature: {current_2['temperature_2m']} °C")


weather_report()
weather_report()
weather_report()
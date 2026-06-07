
import requests
from datetime import datetime, timedelta
import pandas
import matplotlib.pyplot as plt
import os

#Calculate date
today = datetime.now()
week_ago = today - timedelta(days=7)

#Format date for from the API: YYYY-MM-DD
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude=6.5244&longitude=3.3792&start_date={start_date}&end_date={end_date}"
        f"&daily=temperature_2m_max,temperature_2m_min,rain_sum,precipitation_sum,sunshine_duration&timezone=auto"
        )

response = requests.get(url)
data = response.json()
print(data)

#Extract the daily temperature, rain and sunshine.
daily_data = data['daily']

#Create a DataFrame
data_frame = pandas.DataFrame({
    "date": daily_data["time"],
    "max_temp": daily_data["temperature_2m_max"],
    "min_temp": daily_data["temperature_2m_min"],
    "rain_sum": daily_data["rain_sum"],
    "precipitation_sum": daily_data["precipitation_sum"],
    "sunshine_duration": daily_data["sunshine_duration"]
})

#Convert date from string to datetime
data_frame["date"] = pandas.to_datetime(data_frame["date"])
print(data_frame)

#Create Visualization format
plt.figure(figsize=(10, 6))
plt.plot(data_frame["date"], data_frame["max_temp"], marker="o", label="Max Temp")
plt.plot(data_frame["date"], data_frame["min_temp"], marker="o", label="Min Temp")
plt.plot(data_frame["date"], data_frame["rain_sum"], marker="o", label="Rain Sum")
#plt.plot(data_frame["date"], data_frame["precipitation_sum"], marker="o", label="Precipitation Sum")
#plt.plot(data_frame["date"], data_frame["sunshine_duration"], marker="o", label="Sunshine Duration")
plt.xlabel("Date")
plt.ylabel("Temperature (°C), Rain (mm)")
plt.title("Lagos Weather - Past 7 Days")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("weather_chart.png")
#plt.show()

if not os.path.exists("data"):
    os.makedirs("data")

    data_frame.to_csv("data/lagos_weather_report.csv")
    print("Data saved successfully")

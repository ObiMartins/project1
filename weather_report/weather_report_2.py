
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
data_frame_2 = pandas.DataFrame({
    "date": daily_data["time"],
    "max_temp": daily_data["temperature_2m_max"],
    "min_temp": daily_data["temperature_2m_min"],
    "rain_sum": daily_data["rain_sum"],
    "precipitation_sum": daily_data["precipitation_sum"],
    "sunshine_duration": daily_data["sunshine_duration"]
})

#Convert date from string to datetime
data_frame_2["date"] = pandas.to_datetime(data_frame_2["date"])
print(data_frame_2)

#Create Visualization format
fig, ax1 = plt.subplots(figsize=(10, 6))

# Temprature line
ax1.plot(data_frame_2["date"], data_frame_2["max_temp"], marker="o", label="Max Temp")
ax1.plot(data_frame_2["date"], data_frame_2["min_temp"], marker="o", label="Min Temp")

plt.xlabel("Date")
ax1.set_ylabel("Temperature (°C)")

# Rainfall bars
ax2 = ax1.twinx()
ax2.bar(data_frame_2["date"], data_frame_2["precipitation_sum"], alpha=0.3, label="Precipitation", color="blue")
ax2.set_ylabel("Precipitation (mm)")

plt.title("Weather Forcast - Past 7 Days")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("weather_chart_2.png")
plt.show()

if not os.path.exists("data_2"):
   os.makedirs("data_2")

   data_frame_2.to_csv("data/lagos_weather_report_2.csv")
   print("Data saved successfully")

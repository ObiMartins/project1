import requests 
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os
# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for the API: YYYY-MM-DD
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Paris weather for the past week
url = (
f"https://api.open-meteo.com/v1/forecast?"
f"latitude=6.2214413&longitude=6.8973243&start_date={start_date}&end_date={end_date}"
f"&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
)

response = requests.get(url)
data = response.json()
print(data)

#extract the daily temperature
daily_temp = data['daily']

#create a Dataframe
data_frame = pd.DataFrame({
    "date": daily_temp["time"],
    "max_temp": daily_temp["temperature_2m_max"],
    "min_temp": daily_temp["temperature_2m_min"]
})

#convert date to string to datetime
data_frame["date"] = pd.to_datetime(data_frame["date"])
print(data_frame)


#Create Visualization format
plt.figure(figsize=(10, 6))
plt.plot(data_frame["date"], data_frame["max_temp"], marker="o", label="Max Temp")
plt.plot(data_frame["date"], data_frame["min_temp"], marker="o", label="Min Temp")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Africa/Lagos Weather - Past 7 Days")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("weather_chart.png")
#plt.show()

#Create data folder if it does not exist
if not os.path.exists("data"):
    os.makedirs("data")

#save to csv
data_frame.to_csv("data/lagos_weather.csv", index=False)
print("Data Saved to. data/lagos_weather.csv")




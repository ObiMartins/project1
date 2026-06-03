import requests
from datetime import datetime, timedelta
# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)
# Format dates for the API: YYYY-MM-DD
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")
# Paris weather for the past week
url = (
f"https://api.open-meteo.com/v1/forecast?"
f"latitude=8.7832&longitude=34.5085&start_date={start_date}&end_date={end_date}"
f"&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
)
response = requests.get(url)
data = response.json()
print(data)
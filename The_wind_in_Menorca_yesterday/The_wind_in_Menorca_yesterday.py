import openmeteo_requests

import pandas as pd
import requests_cache
from retry_requests import retry
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#Save answers in a .cache folder for 1 hour
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
#If the API fails, retry a maximum of 5 times
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
#Create the client that will use all of that to make requests
openmeteo = openmeteo_requests.Client(session = retry_session)


url = "https://api.open-meteo.com/v1/forecast"
#Asks yesterdays wind speed in Menorca Airport
params = {
	"latitude": 39.8626,
	"longitude": 4.2187,
	"daily": "wind_speed_10m_max",
	"hourly": "wind_speed_10m",
	"timezone": "Europe/Madrid",
	"past_days": 1,
	"forecast_days": 1,
}
responses = openmeteo.weather_api(url, params = params)

# Process location
response = responses[0]


# Process hourly data
hourly = response.Hourly()
hourly_wind_speed_10m = hourly.Variables(0).ValuesAsNumpy()

hourly_data = {
	"date": pd.date_range(
		start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
		end =  pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
		freq = pd.Timedelta(seconds = hourly.Interval()),
		inclusive = "left"
	).tz_convert(response.Timezone().decode())
}

hourly_data["wind_speed_10m"] = hourly_wind_speed_10m

hourly_dataframe = pd.DataFrame(data = hourly_data)

# Process daily data
daily = response.Daily()
daily_wind_speed_10m_max = daily.Variables(0).ValuesAsNumpy()

daily_data = {
	"date": pd.date_range(
		start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
		end =  pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
		freq = pd.Timedelta(seconds = daily.Interval()),
		inclusive = "left"
	).tz_convert(response.Timezone().decode())
}

#Save the maximum wind speed value from yesterday
daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max
wind_max = daily_data["wind_speed_10m_max"][0]

daily_dataframe = pd.DataFrame(data = daily_data)

#Saves only yesterday values and corrects the time zone value
yesterday_data = hourly_dataframe[:24]
yesterday_data["date"] = yesterday_data["date"].dt.tz_localize(None)

#Plot
plt.figure(figsize=(10, 5))

plt.plot(
    yesterday_data["date"],
    yesterday_data["wind_speed_10m"],
    color="deepskyblue",
    lw = 2,
    marker = "o",
    markersize=7,
    markerfacecolor="white",
    markeredgecolor="blue",
    label = f"Max wind speed: {wind_max:.1f} (km/h)"
)

ax = plt.gca()
ax.set_xticks(yesterday_data["date"])
ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))

plt.title("Wind Speed in Menorca - Yesterday")
plt.xlabel("Hour")
plt.ylabel("Wind Speed (km/h)")

plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()



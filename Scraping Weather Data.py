import sys
import json
import urllib.parse
import requests

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

WMO_TEXT = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm w/ slight hail",
    99: "Thunderstorm w/ heavy hail",
}


def geocode_city(name: str):
    params = {"name": name, "count": 1}
    r = requests.get(GEOCODE_URL, params=params, timeout=15)
    r.raise_for_status()
    data = r.json()
    if not data.get("results"):
        raise SystemExit(f"Could not find a match for city: {name}")
    top = data["results"][0]
    return {
        "name": top["name"],
        "country": top.get("country", ""),
        "lat": top["latitude"],
        "lon": top["longitude"],
        "timezone": top.get("timezone", "auto"),
    }


def get_current_weather(lat: float, lon: float, timezone: str = "auto", fahrenheit=False, mph=False):
    # Ask explicitly for the “current” variables we want (per docs).
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,apparent_temperature,weather_code,wind_speed_10m,wind_direction_10m,is_day",
        "timezone": timezone if timezone else "auto",
    }
    if fahrenheit:
        params["temperature_unit"] = "fahrenheit"
    if mph:
        params["wind_speed_unit"] = "mph"

    r = requests.get(FORECAST_URL, params=params, timeout=15)
    r.raise_for_status()
    data = r.json()
    cur = data.get("current")
    if not cur:
        raise SystemExit("API returned no 'current' weather block.")
    return cur


def main():
    if len(sys.argv) < 2:
        print("Usage: python current_weather_open_meteo.py \"City Name\"")
        sys.exit(1)

    city = " ".join(sys.argv[1:])
    loc = geocode_city(city)
    cur = get_current_weather(loc["lat"], loc["lon"], timezone=loc["timezone"], fahrenheit=True, mph=True)

    code = cur.get("weather_code", -1)
    desc = WMO_TEXT.get(code, f"Code {code}")
    is_day = "day" if cur.get("is_day", 1) == 1 else "night"

    print(f"Location: {loc['name']}, {loc['country']} ({loc['lat']:.4f}, {loc['lon']:.4f})")
    print(f"Local time: {cur.get('time')}")
    print(f"Conditions: {desc} [{code}], {is_day}")
    print(f"Temperature: {cur.get('temperature_2m')}°F  (feels like {cur.get('apparent_temperature')}°F)")
    print(f"Wind: {cur.get('wind_speed_10m')} mph @ {cur.get('wind_direction_10m')}°")


if __name__ == "__main__":
    main()
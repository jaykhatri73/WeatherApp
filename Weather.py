import urllib.request
import json

# building the url


def get_weather(api_key, city):
    base_url = "http://api.weatherstack.com/current"
    url = base_url + "?access_key=" + api_key + "&query=" + city

    try:
        # catching the json response and parse into python dictionary
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())

            # if user enters incorrect city name
            if "error" in data:
                return "City not found. Please try again."

            # choosing 6 keys from the response
            else:
                weather_info = {
                    "Temperature": data["current"]["temperature"],
                    "Feels Like": data["current"]["feelslike"],
                    "Weather": data["current"]["weather_descriptions"][0],
                    "Humidity": data["current"]["humidity"],
                    "Wind Speed": data["current"]["wind_speed"],
                    "Wind Direction": data["current"]["wind_dir"],
                }
                return weather_info

    # catching url error
    except urllib.error.URLError as e:
        return "Error occurred:", e.reason

# main function


def main():
    api_key = "25a85809d07730e8d950ffaa5ea19658"
    city = input("Enter a city name: ")
    weather = get_weather(api_key, city)

    # catching any error from the wweather website
    if isinstance(weather, str):
        print(weather)

    # printing the weather inforamtion
    else:
        print(f"Weather in {city}: ")
        for key, value in weather.items():
            print(key + ":", value)


main()

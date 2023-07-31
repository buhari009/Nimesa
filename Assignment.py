import requests

base_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
def get_weather_data(date):
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        for entry in data["list"]:
            if entry["dt_txt"] == date:
                return entry["main"]["temp"]
        return None
    else:
        print("Failed to retrieve weather data.")
        return None

def get_wind_speed_data(date):
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        for entry in data["list"]:
            if entry["dt_txt"] == date:
                return entry["wind"]["speed"]
        return None
    else:
        print("Failed to retrieve wind speed data.")
        return None

def get_pressure_data(date):
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        for entry in data["list"]:
            if entry["dt_txt"] == date:
                return entry["main"]["pressure"]
        return None
    else:
        print("Failed to retrieve pressure data.")
        return None

while True:
    print("\nOptions:")
    print("1. Get weather")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        date = input("Enter the date (YYYY-MM-DD HH:mm:ss format): ")
        temp = get_weather_data(date)
        if temp is not None:
            print(f"Temperature on {date}: {temp} K")
        else:
            print("Data not available for the given date.")

    elif choice == 2:
        date = input("Enter the date (YYYY-MM-DD HH:mm:ss format): ")
        wind_speed = get_wind_speed_data(date)
        if wind_speed is not None:
            print(f"Wind speed on {date}: {wind_speed} m/s")
        else:
            print("Data not available for the given date.")

    elif choice == 3:
        date = input("Enter the date (YYYY-MM-DD HH:mm:ss format): ")
        pressure = get_pressure_data(date)
        if pressure is not None:
            print(f"Pressure on {date}: {pressure} hPa")
        else:
            print("Data not available for the given date.")

    elif choice == 0:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")

import requests
from os import name, system
import time
from datetime import datetime


def clear():
    if name == "nt":  # for windows
        _ = system("cls")
    else:  # for mac and linux
        _ = system("clear")


API_ENDPOINT = "https://api.netatmo.com"
CLIENT_ID = "619e509d7d385338290919e7"
CLIENT_SECRET = "6SAsW2Jj4mG8gfIKUJreUc27EpLT8vhRfVb"
REDIRECT_URI = "https://google.com"


def exchange_code():
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "password",
        "username": "*****************",
        "password": "***********",
        "redirect_uri": REDIRECT_URI,
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
    r = requests.post(API_ENDPOINT + "/oauth2/token", data=data, headers=headers)
    r.raise_for_status()
    return r.json()


def get_data(auth_token):
    hed = {"Authorization": "Bearer " + auth_token}
    data = {"": ""}
    url = "https://api.netatmo.com/api/getstationsdata?device_id=70%3Aee%3A50%3A73%3Af1%3Aa4&get_favorites=true"
    return requests.get(url, data, headers=hed)


def main():
    current_time = time.time()
    expires_in = 0

    loop = True
    while loop:
        current_datetime = datetime.now()
        date_str = current_datetime.strftime("%d/%m/%Y            %H:%M:%S")
        checktime = current_time + expires_in

        if checktime < time.time():
            autorization_data = exchange_code()
            expires_in = autorization_data["expires_in"]
            authorization_token = autorization_data["access_token"]
            response = get_data(authorization_token)
        else:
            response = get_data(authorization_token)

        # data collection
        name_livingroom = response.json()["body"]["devices"][0]["module_name"]
        temp_livingroom = response.json()["body"]["devices"][0]["dashboard_data"]["Temperature"]
        co2_livingroom = response.json()["body"]["devices"][0]["dashboard_data"]["CO2"]
        humidity_livingroom = response.json()["body"]["devices"][0]["dashboard_data"]["Humidity"]
        noise_livingroom = response.json()["body"]["devices"][0]["dashboard_data"]["Noise"]
        pressure = response.json()["body"]["devices"][0]["dashboard_data"]["Pressure"]

        name_bedroom = response.json()["body"]["devices"][0]["modules"][1]["module_name"]
        temp_bedroom = response.json()["body"]["devices"][0]["modules"][1]["dashboard_data"]["Temperature"]
        humidity_bedroom = response.json()["body"]["devices"][0]["modules"][1]["dashboard_data"]["Humidity"]
        temptrend_bedroom = response.json()["body"]["devices"][0]["modules"][1]["dashboard_data"]["temp_trend"]

        name_outside = response.json()["body"]["devices"][0]["modules"][0]["module_name"]
        temp_outside = response.json()["body"]["devices"][0]["modules"][0]["dashboard_data"]["Temperature"]
        humidity_outside = response.json()["body"]["devices"][0]["modules"][0]["dashboard_data"]["Humidity"]
        temptrend_outside = response.json()["body"]["devices"][0]["modules"][0]["dashboard_data"]["temp_trend"]

        clear()
        print("               V Æ R E T   N Å")
        print("------------------------------")
        print("U T E\n")
        print("Lufttrykk:", pressure, "mbar")
        print("Temperatur:", temp_outside, "°c")
        print("Luftfuktighet:", humidity_outside, "%")
        print("Temperaturtrend:", temptrend_outside)
        print("------------------------------")
        print("S T U A\n")
        print("Temp:", temp_livingroom, "°c")
        print("CO2:", co2_livingroom, "ppm")
        print("Luftfuktighet:", humidity_livingroom, "%")
        print("Bråk:", noise_livingroom, "db")
        print("------------------------------")
        print("S O V E R O M M E T\n")
        print("Temp:", temp_bedroom, "°c")
        print("Luftfuktighet:", humidity_bedroom, "%")
        print("------------------------------")
        print(date_str)

        time.sleep(80)


if __name__ == "__main__":
    main()

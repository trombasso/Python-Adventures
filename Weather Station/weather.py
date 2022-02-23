import requests
import os
import time
import configparser


class Netatmo:
    def __init__(self, netatmo_output={}):

        SETTING_FILE_PATH = os.path.join(os.path.dirname(__file__), "settings.ini")
        self.config = configparser.ConfigParser()
        self.config.read(SETTING_FILE_PATH)
        self.API_ENDPOINT = "https://api.netatmo.com"
        self.CLIENT_ID = self.config["CODES"]["client_id"]
        self.CLIENT_SECRET = self.config["CODES"]["client_secret"]
        self.REDIRECT_URI = "https://google.com"

        current_time = time.time()
        expires_in = 0
        self.__netatmo_output = netatmo_output

        loop = True
        while loop:
            checktime = current_time + expires_in

            can_get_info = False
            while can_get_info is not True:
                try:
                    if checktime < time.time():
                        autorization_data = self.exchange_code()
                        expires_in = autorization_data["expires_in"]
                        authorization_token = autorization_data["access_token"]
                        response = self.get_data(authorization_token)

                        # data collection
                        self.__netatmo_output["name_livingroom"] = response.json()["body"]["devices"][0]["module_name"]
                        self.__netatmo_output["temp_livingroom"] = response.json()["body"]["devices"][0]["dashboard_data"]["Temperature"]
                        self.__netatmo_output["co2_livingroom"] = response.json()["body"]["devices"][0]["dashboard_data"]["CO2"]
                        self.__netatmo_output["humidity_livingroom"] = response.json()["body"]["devices"][0]["dashboard_data"]["Humidity"]
                        self.__netatmo_output["noise_livingroom"] = response.json()["body"]["devices"][0]["dashboard_data"]["Noise"]
                        self.__netatmo_output["pressure"] = response.json()["body"]["devices"][0]["dashboard_data"]["Pressure"]

                        self.__netatmo_output["name_bedroom"] = response.json()["body"]["devices"][0]["modules"][1]["module_name"]
                        self.__netatmo_output["temp_bedroom"] = response.json()["body"]["devices"][0]["modules"][1]["dashboard_data"][
                            "Temperature"
                        ]
                        self.__netatmo_output["humidity_bedroom"] = response.json()["body"]["devices"][0]["modules"][1]["dashboard_data"][
                            "Humidity"
                        ]
                        self.__netatmo_output["temptrend_bedroom"] = response.json()["body"]["devices"][0]["modules"][1]["dashboard_data"][
                            "temp_trend"
                        ]

                        self.__netatmo_output["name_outside"] = response.json()["body"]["devices"][0]["modules"][0]["module_name"]
                        self.__netatmo_output["temp_outside"] = response.json()["body"]["devices"][0]["modules"][0]["dashboard_data"][
                            "Temperature"
                        ]
                        self.__netatmo_output["humidity_outside"] = response.json()["body"]["devices"][0]["modules"][0]["dashboard_data"][
                            "Humidity"
                        ]
                        self.__netatmo_output["temptrend_outside"] = response.json()["body"]["devices"][0]["modules"][0]["dashboard_data"][
                            "temp_trend"
                        ]

                        self.__netatmo_output["online"] = True

                    else:
                        response = self.get_data(authorization_token)
                    can_get_info = True

                except Exception:
                    self.__netatmo_output["online"] = False
                    # time.sleep(int(self.config["TIMERS"]["noconnection"]))

    @property
    def netatmo_output(self):
        return self.__netatmo_output

    def exchange_code(self):

        data = {
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
            "grant_type": "password",
            "username": self.config["USERINFO"]["Username"],
            "password": self.config["USERINFO"]["Password"],
            "redirect_uri": self.REDIRECT_URI,
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
        r = requests.post(self.API_ENDPOINT + "/oauth2/token", data=data, headers=headers)
        r.raise_for_status()
        return r.json()

    def get_data(self, auth_token):
        hed = {"Authorization": "Bearer " + auth_token}
        data = {"": ""}
        url = "https://api.netatmo.com/api/getstationsdata?device_id=70%3Aee%3A50%3A73%3Af1%3Aa4&get_favorites=true"
        return requests.get(url, data, headers=hed)


def main():
    netatmo = Netatmo()
    print(netatmo)


if __name__ == "__main__":
    main()

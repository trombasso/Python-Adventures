import tkinter as tk
import requests
from os import name, system
import os
import time
from datetime import datetime
import configparser


def clear():
    if name == "nt":  # for windows
        _ = system("cls")
    else:  # for mac and linux
        _ = system("clear")


class Weather:
    def __init__(self):
        window = tk.Tk()
        window.title("Weather Station")
        window.geometry("200x300")
        window.resizable(False, False)

        SETTING_FILE_PATH = os.path.join(os.path.dirname(__file__), "settings.ini")
        self.config = configparser.ConfigParser()
        self.config.read(SETTING_FILE_PATH)
        self.API_ENDPOINT = "https://api.netatmo.com"
        self.CLIENT_ID = self.config["CODES"]["client_id"]
        self.CLIENT_SECRET = self.config["CODES"]["client_secret"]
        self.REDIRECT_URI = "https://google.com"

        window.mainloop()

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

    def get_data(auth_token):
        hed = {"Authorization": "Bearer " + auth_token}
        data = {"": ""}
        url = "https://api.netatmo.com/api/getstationsdata?device_id=70%3Aee%3A50%3A73%3Af1%3Aa4&get_favorites=true"
        return requests.get(url, data, headers=hed)


if __name__ == "__main__":
    Weather()

from os import name, system
from datetime import datetime
from time import sleep
import rich


def clear():
    if name == "nt":  # for windows
        _ = system("cls")
    else:  # for mac and linux
        _ = system("clear")


class Calc_sal:
    def __init__(self, name="", sal=0, start_time="00:00", current_sal=0):
        self.__name = name
        self.__sal = sal
        self.__start_time = start_time
        self.__current_sal = current_sal

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def sal(self):
        return self.__sal

    @sal.setter
    def sal(self, sal):
        self.__sal = sal / 3600  # compute salary pr second
        print(self.__sal)

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, start_time):
        self._start_time = start_time

    @property
    def current_sal(self):
        return self.__current_sal

    @current_sal.setter
    def current_sal(self, current_sal):
        self.__current_sal = current_sal

    def calculate(self):
        nowtime = datetime.now()
        duration = nowtime - self.start_time
        secondssince = duration.total_seconds()
        self.__current_sal = self.sal * secondssince

    def __str__(self):
        return f"Name: {self.name} Sal pr. hour: {self.sal * 3600} Started working: {self.start_time} Current: {self.current_sal}"


def main():
    clear()
    person = Calc_sal
    print(person())
    person.name = "Anders"
    person.sal = 221
    person.start_time = "20200704 11:00"

    print(person())
    # person.calculate()
    # print(person())

    # person.name = input("What is your name? ")
    # person.sal = input("How much do you make pr. hour? ")
    # person.start_time = input("When did you start your shift? ")

    # clear()
    # print("Hei, hva heter du?")
    # name = input()
    # print("Når startet du å jobbe? (ÅÅÅÅMMDD TT:MM)")
    # starttime = datetime.strptime(input(), "%Y%m%d %H:%M")
    # sal = int(input("Hva er din timelønn? ")) / 3600

    # while True:
    #     clear()
    #     print(f"{name} har tjent:")
    #     print
    #     print(f"{calculate(starttime, sal):.2f} NOK")
    #     sleep(1)


if __name__ == "__main__":
    main()

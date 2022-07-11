from os import name, system
from datetime import datetime
from time import sleep
from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from getkey import getkey, keys


BOX_STYLE = "white on black"

console = Console()
persons = []


def clear():
    if name == "nt":  # for windows
        _ = system("cls")
    else:  # for mac and linux
        _ = system("clear")


class Calc_sal:
    def __init__(self, name="", sal=0, start_time=datetime.strptime("20200101 00:00", "%Y%m%d %H:%M"), current_sal=0):
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

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, start_time):
        self.__start_time = start_time

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
        return f"Name: {self.name} Sal pr. hour: {self.sal * 3600} Started working: {self.start_time} Current: {self.current_sal:.2f}"


def make_layout() -> Layout:
    layout = Layout(name="root", size=100)
    layout.split(Layout(name="header", size=3), Layout(name="main", size=25), Layout(name="menu", size=3))
    return layout


class Salary_List:
    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left", ratio=1)
        if len(persons) == 0:
            grid.add_row("Please add peoples....")
        for x in range(0, len(persons)):
            persons[x].calculate()
            grid.add_row(f"{x+1}) {persons[x]}")
        return Panel(grid, style=BOX_STYLE)


class Header:
    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left", ratio=1)
        grid.add_column(justify="right")
        grid.add_row("Mr. Money today!", "2022 © BASSO")
        return Panel(grid, style=BOX_STYLE)


class Menu:
    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left", ratio=1)
        grid.add_row("F1) Add person   F2) List all   F3) Clear list")
        return Panel(grid, style=BOX_STYLE)


def adduser():
    person = Calc_sal()
    person.name = input("What is you name, dear sir/madam? ")
    person.sal = int(input("What is your salary pr. hour? "))
    person.start_time = datetime.strptime(input("When did your shift start? (YYYYMMDD HH:MM)"), "%Y%m%d %H:%M")
    persons.append(person)
    main()


# def create_user():
#     person = Calc_sal()
#     person.name = "Anders"
#     person.sal = 231
#     person.start_time = datetime.strptime("20220704 11:00", "%Y%m%d %H:%M")
#     person2 = Calc_sal()
#     person2.name = "Erik"
#     person2.sal = 201
#     person2.start_time = datetime.strptime("20220704 11:00", "%Y%m%d %H:%M")
#     persons.append(person)
#     persons.append(person2)


def main():
    # create_user()
    layout = make_layout()
    layout["header"].update(Header())
    layout["main"].update(Salary_List())
    layout["menu"].update(Menu())

    with Live(layout, refresh_per_second=25, screen=True) as live:
        while True:
            a = getkey()
            if a == "q" or a == "Q":
                exit()
            else:
                break

    clear()
    if a == "\x1bOP":  # F1 key
        adduser()
    elif a == "\x1bOQ":
        input("Wither....")
        main()
    elif a == "\x1bOR":
        persons.clear()
        main()
    else:
        main()


if __name__ == "__main__":
    main()

from datetime import datetime
from tkinter import N
from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from time import sleep
from weather import Netatmo
from getkey import getkey

# import time
# from rich import print


"""
# from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
# from rich.syntax import Syntax
# from rich.text import Text
# import configparser
# import requests
# from os import name, system
# import os
"""

BOX_STYLE = "white on black"

console = Console()
try:
    netatmo_data = Netatmo()
except Exception as e:
    print(e)


class NetatmoLayout:
    def __rich__(self) -> Panel:
        n_line = Table.grid(padding=0)
        n_line.add_column(style="cyan", justify="left", width=18)
        n_line.add_column(style="white", justify="right", width=10)
        n_line.add_column(style="cyan", justify="left", width=6)

        n_line.add_row(f"{netatmo_data()['name_outside']}", style="u b")
        n_line.add_row("Luftrykk:", str(netatmo_data()["pressure"]), " mbar")
        n_line.add_row("Temperatur:", str(netatmo_data()["temp_outside"]), " °c")
        n_line.add_row("Luftfuktighet", str(netatmo_data()["humidity_outside"]), " %")
        n_line.add_row("Temperaturtrend", str(netatmo_data()["temptrend_outside"]))

        n_line.add_row("")
        n_line.add_row(netatmo_data()["name_livingroom"], style="u b")
        n_line.add_row("Temp: ", str(netatmo_data()["temp_livingroom"]), " °c")
        n_line.add_row("CO2: ", str(netatmo_data()["co2_livingroom"]), " ppm")
        n_line.add_row("Fuktighet: ", str(netatmo_data()["humidity_livingroom"]), " %")
        n_line.add_row("Støy: ", str(netatmo_data()["noise_livingroom"]), " dB")
        # n_line.add_row(datetime.now().ctime().replace(":", "[blink]:[/]"))

        n_line.add_row("")
        n_line.add_row(netatmo_data()["name_bedroom"], style="u b")
        n_line.add_row("Temp", str(netatmo_data()["temp_bedroom"]), " °c")
        n_line.add_row("Luftfuktighet", str(netatmo_data()["humidity_bedroom"]), " %")
        n_line.add_row("Temp trend", str(netatmo_data()["temptrend_bedroom"]))
        n_line.add_row("")
        n_line.add_row("")
        # n_line.add_row("Online: ", str(netatmo_data()["online"]), style="grey37")

        return Panel(
            Align.center(Group(n_line), vertical="top"),
            box=box.ROUNDED,
            padding=(1, 3),
            title="Netatmo",
            title_align="left",
            style=BOX_STYLE,
        )


def yr_layout() -> Panel:
    nye_meldinger = Table.grid(padding=1)
    nye_meldinger.add_column(style="white", justify="center", width=40)
    nye_meldinger.add_row("Under construction...")
    nye_meldinger.add_row("(u u)\n( y )")

    meldinger = Panel(
        Align.center(Group(nye_meldinger), vertical="top"),
        box=box.ROUNDED,
        padding=(3, 0),
        title="YR",
        title_align="left",
        style=BOX_STYLE,
    )

    return meldinger


def make_layout() -> Layout:
    layout = Layout(name="root", size=100)

    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", size=25),
        Layout(name="footer", size=3),
    )
    layout["main"].split_row(
        Layout(name="side", ratio=1),
        Layout(name="body", ratio=1),
    )

    # layout["side"].split(Layout(name="box1"), Layout(name="box2"))
    return layout


class Header:
    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[b]Været i Bodø[/b]",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style=BOX_STYLE)


class Footer:
    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left")
        grid.add_column(justify="right")
        # grid.add_row(str(netatmo_data()["counter"]), "[b]Sist oppdatert:[/b]", datetime.now().ctime())
        grid.add_row(f"Online: {str(netatmo_data()['online'])}", f"Reloads: {str(netatmo_data()['counter'])}", style="grey37")
        return Panel(grid, style=BOX_STYLE)


layout = make_layout()
layout["header"].update(Header())
layout["side"].update(NetatmoLayout())
layout["body"].update(yr_layout())
layout["footer"].update(Footer())

with Live(layout, refresh_per_second=1, screen=True) as live:
    while True:
        a = getkey()
        if a == "q":
            # sleep(300)
            exit()

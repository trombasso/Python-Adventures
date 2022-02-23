from datetime import datetime
from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from time import sleep

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

console = Console()
BOX_STYLE = "white on black"


def netatmo_layout() -> Panel:
    beskjed = "Her er en beskjed fra som e så mange elementa lang sånn at vi kan sjekke om det e nåkka i veien for dettan..."
    nye_meldinger = Table.grid(padding=2)
    nye_meldinger.add_column(style="red", justify="left", width=20)
    nye_meldinger.add_row(beskjed)
    nye_meldinger.add_row(datetime.now().ctime().replace(":", "[blink]:[/]"))
    flere_ting = f"Litt mere tekst!"

    meldinger = Panel(
        Align.center(Group(nye_meldinger, "\n", Align.right(flere_ting)), vertical="top"),
        box=box.ROUNDED,
        padding=(1, 3),
        title="Netatmo",
        title_align="left",
        style=BOX_STYLE,
    )

    return meldinger


def yr_layout() -> Panel:
    nye_meldinger = Table.grid(padding=1)
    nye_meldinger.add_column(style="red", justify="left", width=20)
    nye_meldinger.add_row("Nytt Mas")
    nye_meldinger.add_row("Og mere mas")
    flere_ting = "Håpe det går!"

    meldinger = Panel(
        Align.center(Group(nye_meldinger, "\n", Align.right(flere_ting)), vertical="top"),
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
        Layout(name="main", size=20),
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


def Footer():
    # def __rich__(self) -> Panel:
    grid = Table.grid(expand=True)
    grid.add_column(justify="right", ratio=1)
    grid.add_column(justify="right")
    grid.add_row("[b]Sist oppdatert:[/b]", datetime.now().ctime())

    return Panel(grid, style=BOX_STYLE)


layout = make_layout()
layout["header"].update(Header())
layout["side"].update(netatmo_layout())
layout["body"].update(yr_layout())
layout["footer"].update(Footer())

with Live(layout, refresh_per_second=5, screen=True) as live:
    while True:
        sleep(1000)

from bs4 import BeautifulSoup
from rich import print
import os
import urllib.request

PATH = os.path.dirname(__file__)
URL = urllib.request.urlopen("https://www.vg.no")
FILE = "index.html"

with open(os.path.join(PATH, FILE)) as file:
    soup = BeautifulSoup(file, "html5lib")

vg = BeautifulSoup(URL, "html5lib", from_encoding=URL.info().get_param("charset"))

# print(soup.prettify())

for elem in vg.find_all("a", href=True):
    print(elem.contents, "->", elem["href"])

# print(soup.getText())

import os

path = os.path.dirname(__file__)

with open(os.path.join(path, "input.txt")) as file:
    file = [x.split() for x in file.readlines()]

xpos = 0
ypos = 0

for elem in file:
    if elem[0] == "forward":
        xpos += int(elem[1])
    elif elem[0] == "up":
        ypos -= int(elem[1])
    elif elem[0] == "down":
        ypos += int(elem[1])

print(xpos * ypos)

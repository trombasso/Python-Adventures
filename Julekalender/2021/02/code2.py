import os

path = os.path.dirname(__file__)

with open(os.path.join(path, "input.txt")) as file:
    file = [x.split() for x in file.readlines()]

xpos, ypos, aim = 0, 0, 0

for elem in file:
    if elem[0] == "forward":
        xpos += int(elem[1])
        ypos += int(elem[1]) * aim
    elif elem[0] == "up":
        aim -= int(elem[1])
    elif elem[0] == "down":
        aim += int(elem[1])

print(xpos * ypos)

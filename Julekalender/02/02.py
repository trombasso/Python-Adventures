import os

lines = []
hor_pos = 0
aim = 0
depth = 0

file_dir = os.path.dirname(__file__)
with open(file=os.path.join(file_dir, "input.txt")) as file:
    for line in file:
        line = line.strip()
        lines.append(line)
    lines = [x.split() for x in lines]

for elem in lines:
    if elem[0] == "forward":
        hor_pos += int(elem[1])
        depth = depth + (aim * int(elem[1]))

    elif elem[0] == "down":
        aim += int(elem[1])
    elif elem[0] == "up":
        aim -= int(elem[1])

sum = hor_pos * depth
print(sum)

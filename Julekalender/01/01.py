import os

counter = -1
lines = []
prev = [0]
addlist = []

file_dir = os.path.dirname(__file__)
with open(file=os.path.join(file_dir, "input.txt")) as file:
    for line in file:
        line = line.strip()
        lines.append(line)
lines = [int(x) for x in lines]


for elem in range(len(lines) - 2):
    for x in range(0, 3):
        addlist.append(lines[elem + x])
    if sum(addlist) > sum(prev):
        print(f"{sum(addlist)} ( + increased)")
        counter += 1
        prev = addlist
        addlist = []
    else:
        print(f"{sum(addlist)} ( - decreased)")
        prev = addlist
        addlist = []

print(counter)

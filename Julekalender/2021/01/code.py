import os

path = os.path.dirname(__file__)
counter = 0

with open(os.path.join(path, "input.txt")) as file:
    file = [int(x) for x in file.readlines()]

prev_x = 100000
for x in file:
    if x > prev_x:
        counter += 1
    prev_x = x

print(counter)

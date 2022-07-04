import os

path = os.path.dirname(__file__)
counter = 0

with open(os.path.join(path, "input.txt")) as file:
    file = [int(x) for x in file.readlines()]

prev_sum = 100000000

for x in range(0, len(file) - 2):
    trisum = file[x] + file[x + 1] + file[x + 2]
    if trisum > prev_sum:
        counter += 1
    prev_sum = trisum

print(counter)

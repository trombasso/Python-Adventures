import os

file_dir = os.path.dirname(__file__)
with open(file=os.path.join(file_dir, "input.txt")) as file:
    binary_list = file.readlines()


def most_common(list, position):
    zero_count = 0
    for x in range(len(list)):
        if list[x][position] == "0":
            zero_count += 1

    if zero_count > len(list) / 2:
        return "0"
    else:
        return "1"


def least_common(list, position):
    zero_count = 0
    for x in range(len(list)):
        if list[x][position] == "0":
            zero_count += 1

    if zero_count > len(list) / 2:
        return "1"
    else:
        return "0"


def prune_list(list, position, value):
    newlist = []
    for x in range(len(list)):
        if list[x][position] == value:
            newlist.append(list[x])

    return newlist


def oxygen_rating(list):
    x = 0
    while len(list) > 1:
        list = prune_list(list, x, most_common(list, x))
        x += 1
    return int(list[0], 2)


def co2_scrubber_rating(list):
    x = 0
    while len(list) > 1:
        list = prune_list(list, x, least_common(list, x))
        x += 1
    return int(list[0], 2)


def main():
    ox = oxygen_rating(binary_list)
    co2 = co2_scrubber_rating(binary_list)
    print(ox, co2)
    print(ox * co2)


if __name__ == "__main__":
    main()

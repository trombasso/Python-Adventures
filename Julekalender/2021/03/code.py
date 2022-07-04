import os

path = os.path.dirname(__file__)

with open(os.path.join(path, "input.txt")) as file:
    file = [x.split() for x in file.readlines()]


def check_mostcommon_bit(bit, list):
    zeroes = 0
    for byte in list:
        if byte[0][bit] == "0":
            zeroes += 1

    if zeroes > len(list) / 2:
        return 0
    return 1


def traverse_list(list):
    mostcommon = ""
    leastcommon = ""
    for bit in range(0, 12):
        common_bit = str(check_mostcommon_bit(bit, list))
        mostcommon = mostcommon + common_bit
    for x in mostcommon:
        if x == "1":
            leastcommon = leastcommon + "0"
        else:
            leastcommon = leastcommon + "1"

    print(mostcommon, leastcommon)
    return (int(mostcommon, 2), int(leastcommon, 2))


def main():
    gamma_rate, epsillon_rate = traverse_list(file)
    print(gamma_rate, epsillon_rate)
    print(gamma_rate * epsillon_rate)


main()

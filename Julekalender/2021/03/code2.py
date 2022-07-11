import os

path = os.path.dirname(__file__)

with open(os.path.join(path, "input.txt")) as file:
    file = [x.strip("\n") for x in file.readlines()]


def find_common(value, lst, pos=0):  # 1 most common, 0 least common
    while len(lst) > 1:
        ones = []
        zeros = []
        for line in lst:
            if line[pos] == "0":
                zeros.append(line)
            else:
                ones.append(line)

        if len(ones) >= len(lst) / 2:
            if value == 1:
                lst = ones
            else:
                lst = zeros

        elif len(ones) < len(lst) / 2:
            if value == 1:
                lst = zeros
            else:
                lst = ones

        pos += 1

    return lst[0]


def main():
    oxygen_gen_rate = find_common(1, file)
    print(int(oxygen_gen_rate, 2))
    print(oxygen_gen_rate)

    CO2_scrub_rating = find_common(0, file)
    print(int(CO2_scrub_rating, 2))
    print(CO2_scrub_rating)

    print(int(oxygen_gen_rate, 2) * int(CO2_scrub_rating, 2))


if __name__ == "__main__":
    main()

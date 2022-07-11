import os


def create_vent_map(vent_lst):

    vent_map = {}

    for xy in vent_lst:
        x1 = xy[0][0]
        x2 = xy[1][0]
        y1 = xy[0][1]
        y2 = xy[1][1]

        if x1 == x2 or y1 == y2:  # Only horisontals or verticals
            if x1 == x2:  # Equal X (Y is moving)
                if y2 < y1:
                    y2, y1 = y1, y2

                y = y1
                while y <= y2:
                    if (x1, y) in vent_map:
                        vent_map[x1, y] += 1
                    else:
                        vent_map[x1, y] = 1
                    y += 1

            elif y1 == y2:  # Equal Y (X is moving)
                if x2 < x1:
                    x2, x1 = x1, x2

                x = x1
                while x <= x2:
                    if (x, y1) in vent_map:
                        vent_map[x, y1] += 1
                    else:
                        vent_map[x, y1] = 1
                    x += 1

        else:  # Considering diagonals
            if y1 > y2:
                x1, y1, x2, y2 = x2, y2, x1, y1
                
            if x1 - x2 < 0 # Negative direction
            
            
    return vent_map


def count_points(vent_map):
    counter = 0
    for elem in vent_map:
        if vent_map[elem] >= 2:
            counter += 1
    return counter


def main():

    path = os.path.dirname(__file__)

    with open(os.path.join(path, "input_short.txt")) as file:
        file = [x.strip("\n") for x in file.readlines()]
    file = [x.split("->") for x in file]
    vent_lst = [[x.strip(" ") for x in y] for y in file]
    vent_lst = [[x.split(",") for x in y] for y in vent_lst]
    vent_lst = [[[int(x) for x in y] for y in j] for j in vent_lst]

    vent_map = create_vent_map(vent_lst)
    print(count_points(vent_map))


if __name__ == "__main__":
    main()

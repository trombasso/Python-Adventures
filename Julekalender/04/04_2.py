import os


def open_file(filename):
    data_list = []
    file_dir = os.path.dirname(__file__)
    with open(file=os.path.join(file_dir, "input.txt")) as file:
        for line in file:
            line = line.replace("\n", "")
            if line != "":
                data_list.append(line)

    return data_list


def convert_list(input):
    bingo_numbers = input[:1]
    bingo_numbers = bingo_numbers[0].split(",")
    bingo_numbers = [int(x) for x in bingo_numbers]
    board_numbers = input[1:]
    num_of_boards = int(len(board_numbers) / 5)
    boards = {x: [] for x in range(0, num_of_boards)}

    for x in range(len(boards)):
        for y in range(5 * x, 5 * (x + 1)):
            board_numbers[y] = board_numbers[y].split()
            boards[x].append([int(z) for z in board_numbers[y]])
    # print(bingo_numbers[1])
    return bingo_numbers, boards


def check_If_Bingo(bingo_numbers, boards):
    for bingo_number in range(len(bingo_numbers)):
        for board in range(len(boards)):
            for row in range(len(boards[board])):
                for x in range(len(boards[board][row])):
                    if boards[board][row][x] == bingo_numbers[bingo_number]:
                        boards[board][row][x] = "X"

                        board = control_rows_cols(boards)
                        if board is not False:
                            return board, bingo_numbers[bingo_number]
                        else:
                            return -1, -1

    # print(boards)


def control_rows_cols(boards):
    # rows
    for board in range(len(boards)):
        for row in range(len(boards[board])):
            if boards[board][row] == ["X", "X", "X", "X", "X"]:
                return board
    # cols
    for board in boards:
        for x in range(5):
            column = [c_row[x] for c_row in boards[board]]
            if column == ["X", "X", "X", "X", "X"]:
                return board
    return False


def main():
    data_list = open_file("input.txt")
    bingo_numbers, boards = convert_list(data_list)
    while len(boards) > 1:
        winner, bingo_number = check_If_Bingo(bingo_numbers, boards)
        if winner != -1:
            boards.pop(winner)
            boards_length = [x for x in range(len(boards))]
            boards = dict(zip(boards_length, list(boards.values())))

    print(boards, bingo_number, "\n\n\n")

    sum = 0
    for x in range(len(boards[0])):
        for y in boards[0][x]:
            if y != "X":
                sum = sum + y
    print(sum, bingo_number)
    print(sum * bingo_number)


if __name__ == "__main__":
    main()

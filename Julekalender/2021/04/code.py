import os

path = os.path.dirname(__file__)


class Boards:
    def __init__(self, board=[], bingo_lst=[], bingo_status=[0, False]):
        self.board = board
        self.bingo_lst = bingo_lst
        self.bingo_status = bingo_status

    def check_bingo(self):
        for x in range(0, len(self.board)):
            if sum(self.board[x]) == 500:
                self.bingo_status[1] = True
                return True
            elif self.board[0][x] + self.board[1][x] + self.board[2][x] + self.board[3][x] + self.board[4][x] == 500:
                self.bingo_status[1] = True
                return True
        return False

    def check_if_num_exist(self):
        if self.bingo_status[1] is not True:
            for number in self.bingo_lst:
                self.bingo_status[0] += 1
                for x in range(0, len(self.board)):
                    if number in self.board[x]:
                        self.board[x][self.board[x].index(number)] = 100
                        if self.check_bingo():
                            return


def create_boards(file, bingo_lst):
    boards = []
    while len(file) > 1:
        board = None
        board_contents = []
        for _ in range(0, 5):
            board_contents.append([int(x) for x in file[0].split()])
            if len(file) > 1:
                file.pop(0)
        board = Boards(board_contents, bingo_lst, bingo_status=[0, False])
        boards.append(board)
        board.check_if_num_exist()

    return boards


def check_winners(boards):
    current_board = None
    current_board_rotations = 10000

    for x in range(0, len(boards)):
        if boards[x].bingo_status[0] < current_board_rotations and boards[x].bingo_status[1] is True:
            current_board = x
            current_board_rotations = boards[x].bingo_status[0]

    sum_winner = sum([y for x in boards[current_board].board for y in x if y != 100])

    print(sum_winner * boards[current_board].bingo_lst[current_board_rotations - 1])


def check_last_winners(boards):
    current_board = None
    current_board_rotations = 0

    for x in range(0, len(boards)):
        if boards[x].bingo_status[0] > current_board_rotations and boards[x].bingo_status[1] is True:
            current_board = x
            current_board_rotations = boards[x].bingo_status[0]

    sum_winner = sum([y for x in boards[current_board].board for y in x if y != 100])

    print(sum_winner * boards[current_board].bingo_lst[current_board_rotations - 1])


def main():
    with open(os.path.join(path, "input.txt")) as file:
        file = [x.strip("\n") for x in file.readlines()]

    file = [x for x in file if x != ""]
    bingo_lst = [int(x) for x in file[0].split(",")]
    file.pop(0)

    boards = create_boards(file, bingo_lst)

    check_winners(boards)
    check_last_winners(boards)


if __name__ == "__main__":
    main()

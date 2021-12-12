import numpy as np
import numpy.ma as ma

numbers = np.loadtxt('days/day_04/input.txt', max_rows=1, dtype=int, delimiter=',')

boards = np.loadtxt('days/day_04/input.txt', skiprows=1, dtype=int)
boards = np.reshape(boards, (-1, 5, 5))

def check_bingo(marks):
    return np.any([
        np.all(marks[0, :]),
        np.all(marks[1, :]),
        np.all(marks[2, :]),
        np.all(marks[3, :]),
        np.all(marks[4, :]),
        np.all(marks[:, 0]),
        np.all(marks[:, 1]),
        np.all(marks[:, 2]),
        np.all(marks[:, 3]),
        np.all(marks[:, 4]),
        # np.all([marks[0, 0], marks[1, 1], marks[2, 2], marks[3, 3], marks[4, 4]]),
        # np.all([marks[4, 0], marks[3, 1], marks[2, 2], marks[1, 3], marks[0, 4]]),
    ])

def get_winning_board():
    marks = np.zeros(boards.shape, dtype=int)

    for number in numbers:
        for n, board in enumerate(boards):
            indices = np.where(board == number)
            if len(indices[0]) > 0:
                i = indices[0][0]
                j = indices[1][0]
                marks[n][i][j] = 1
                if check_bingo(marks[n]):
                    numbers_left = ma.masked_array(board, mask=marks[n])
                    print(numbers_left)
                    print(number, np.sum(numbers_left))
                    print(np.sum(numbers_left) * number)
                    return

get_winning_board()

def get_losing_board():
    marks = np.zeros(boards.shape, dtype=int)

    boards_left = [n for n in range(len(boards))]

    for number in numbers:
        for n in list(boards_left):
            indices = np.where(boards[n] == number)
            if len(indices[0]) > 0:
                i = indices[0][0]
                j = indices[1][0]
                marks[n][i][j] = 1
                if check_bingo(marks[n]):
                    if len(boards_left) == 1:
                        numbers_left = ma.masked_array(boards[n], mask=marks[n])
                        print(numbers_left)
                        print(number, np.sum(numbers_left))
                        print(np.sum(numbers_left) * number)
                        return
                    else:
                        boards_left.remove(n)

get_losing_board()
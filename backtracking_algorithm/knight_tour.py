#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]


def validate_move(bo, row, column):
    if row < 8 and row >= 0 and column < 8 and column >= 0 and bo[row, column] == 0:
        return True


def solve(bo, row, column, n, counter):

    for i in range(8):
        if counter >= 65:
            return True
        new_x = row + move_x[i]
        new_y = column + move_y[i]
        if validate_move(bo, new_x, new_y):
            bo[new_x, new_y] = counter
            if solve(bo, new_x, new_y, n, counter + 1):
                return True
            bo[new_x, new_y] = 0
    return False


board = np.zeros([8, 8])

board[3, 2] = 1
solve(board, 3, 2, 8, 2)
print(board.sum())
print(board)

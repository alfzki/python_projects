#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def validate(board, n):

    for row in range(0, n):
        if sum(board[row, :]) > 1:
            return False

    for column in range(0, n):
        if sum(board[:, column]) > 1:
            return False

    diags = [board[::-1, :].diagonal(i) for i in range(-n, 1, n)]
    diags.extend(board.diagonal(i) for i in range(n - 1, -n, -1))

    for x in diags:
        if len(x) > 1:
            if sum(x) > 1:
                return False

    return True


def solve(board, row, n):

    if validate(board, n):
        if board.sum() == n:
            return True

    for column in range(0, n):
        board[row, column] = 1
        if validate(board, n):
            if solve(board, row + 1, n):
                return True
            board[row, column] = 0
        else:
            board[row, column] = 0

    return False


board = np.zeros([8, 8])

if solve(board, 0, 8):
    print(board)

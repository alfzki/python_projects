#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def computer_guess():
    """Let the computer guess the number you choose"""
    low = 1
    high = 100
    feedback = ''
    while feedback != ('c' or 'C'):
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"is {guess} too low(L), too high(H), or correct(C) ")
        if feedback == ('h' or 'H'):
            high = guess - 1
        elif feedback == ('l' or 'L'):
            low = guess + 1

    print(f"Your number is {guess}.")


computer_guess()

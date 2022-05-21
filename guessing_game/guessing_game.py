#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys


def guess_the_number(x):
    number = random.randint(1, x)
    guess = 0
    while guess != number:
        if x <= 100:
            guess = int(input(f"Please input a number from 1 to {x}: "))
        else:
            guess = int(input("Please input a number from 1 to infinity: "))

        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")

    print("You are correct!")


def select_difficulty():
    print("1.Easy\n2.Medium\n3.Impossible")
    difficulty = int(input("Select difficulty: "))
    if difficulty == 1:
        return 10
    elif difficulty == 2:
        return 100
    elif difficulty == 3:
        return sys.maxsize
    else:
        print("Invalid number, defaulting to medium")
        return 100


guess_the_number(select_difficulty())

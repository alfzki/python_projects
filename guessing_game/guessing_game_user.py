#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys


def guess_the_number():
    print("1.Easy\n2.Medium\n3.Impossible")
    difficulty = int(input("Select difficulty: "))
    if difficulty == 1:
        x = 10
    elif difficulty == 2:
        x = 100
    elif difficulty == 3:
        x = sys.maxsize
    else:
        print("Invalid number, defaulting to medium")
        x = 100

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


guess_the_number()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def play():
    """Start a rock paper scissor game"""
    print("rock(r), paper(p), or scissor(s)?")
    user = input("Choice:")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return "You win!"

    return "You lost!"


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or \
           (player == 's' and opponent == 'p') :

        return True


print(play())

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import math
from math import acos


# 1. Calculate pi using the Leibniz's formula
"""
    1.Initialize denominator=1 // this variable will be used as the denominator
      of leibniz’s formula, it will be incremented by 2
    2.Initialize sum=0 // sum will add all the elements of the series
    3.Run a for loop from 0 to 1000000 //at this value, we get the most
      accurate value of Pi
    4.Inside for loop, check if i%2==0 then do sum=sum+4/denominator
    5.Else, do sum=sum-4/denominator
    6.Increment denominator by 2, go to step 3
"""


def pi_leibniz():
    denominator = 1
    accuracy = 10000

    # initialize sum
    sum = 0

    for i in range(accuracy):

        if i % 2 == 0:
            sum += 4 / denominator
        else:
            sum -= 4 / denominator

        denominator += 2

    print(sum)


pi_leibniz()

# 2.Calculate pi using acos method
"""
    1.The value of Π is calculated using acos() function which returns a
      numeric value between [-Π, Π].
    2.Since using acos(0.0) will return the value for 2*Π. Therefore to get the
      value of Π:
"""


def pi_acos():
    pi = round(2 * acos(0.0), 3)
    print(pi)


pi_acos()

# 3.Using numpy
print(numpy.pi)

# 4.Using math
print(math.pi)

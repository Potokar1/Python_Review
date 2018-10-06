#!/bin/python3      I COMMENTED OUT THE WEBSITE SPECIFIC CODE SO IT CAN RUN ON MY LOCAL MACHINE :-)

import math
import os
import random
import re
import sys

# Complete the countSwaps function below. This is also a bubble sort implementation


def countSwaps(a):
    unsorted = True
    decreasing_length = len(a) - 1
    swap_count = 0
    # This is the bubble sort implementation in python3
    while unsorted:
        unsorted = False
        for i in range(decreasing_length):
            if a[i] > a[i+1]:
                swap_count += 1
                # HOW TO SWAP IN PYTHON YA FOOL:
                a[i], a[i+1] = a[i+1], a[i]
                unsorted = True
        decreasing_length -= 1
    print('Array is sorted in {} swaps.'.format(swap_count))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[len(a)-1]))


# if __name__ == '__main__':
print('Please enter the number of elements in your list.')
n = int(input())
print('Please enter in {} values, seperated by spaces.'.format(n))
a = list(map(int, input().rstrip().split()))

countSwaps(a)

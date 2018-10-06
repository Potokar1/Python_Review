#!/bin/python3
# Note that I commented out the platform specific code so this runs on its own and not in the specific website where I coded this originally

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.

# This function takes in the 6x6 2d array and then outputs the largest hourglass sum


def hourglassSum(arr):
    # -1000 just in case we only get negative values for our matrix
    highest_sum = -1000
    # This looks at the 4 rows where the top left of the hourglass will start
    for starting_row in range(4):
        # This looks at the 4 columns where the top left of the hourglass will start
        for starting_col in range(4):
            sum_of_hour = 0
            # this looks at the three top values and three bottom values of the hourglass
            for col in range(3):
                sum_of_hour += arr[starting_row][starting_col + col]
                sum_of_hour += arr[starting_row + 2][starting_col + col]
            # this looks at the middle value of the hourglass
            sum_of_hour += arr[starting_row + 1][starting_col + 1]
            if sum_of_hour > highest_sum:
                highest_sum = sum_of_hour
    return highest_sum

    return sum_of_arr

# if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')


arr = []
print('Please enter 6 values (0-9) seperated by a space, ended by pressing enter.')
print('You will do this 6 times to create a 6x6 matrix')
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
result = hourglassSum(arr)

print(str(result))
#    fptr.write(str(result) + '\n')

#    fptr.close()

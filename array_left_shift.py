#!/bin/python3 I COMMENTED OUT THE WEBSITE SPECIFIC CODE

import math
import os
import random
import re
import sys

# Complete the rotLeft function below. This is a lot like the swap method yuh
# JK, the swap implementation didn't work. Now we got the two lists approach


def rotLeft(a, d):

    #    for i in range(d):
    # this    temp = a[i]
    # don't   a[i] = a[ ( len(a) - d) + i]
    # work    a[ ( len(a) - d) + i] = temp

    for i in range(d):
        a_new = []
        a_temp = a[1:len(a)]
        a_append = a[:1]
        # Note: we are using extend instead of append because extend adds directly onto the array
        #   from an iterable whereas append just slaps the lists together :/ not cool!
        a_new.extend(a_temp)
        a_new.extend(a_append)
        a = a_new
    return a

# if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

print('Please enter two values (# #) seperated by spaced. 1st = length of array, 2nd = number of left shifts')
nd = input().split()

n = int(nd[0])

d = int(nd[1])

print('please enter the values, seperated by spaces, of the array of length {}'.format(n))
a = list(map(int, input().rstrip().split()))

result = rotLeft(a, d)

print(str(result))
#    fptr.write(' '.join(map(str, result)))
#    fptr.write('\n')

#    fptr.close()

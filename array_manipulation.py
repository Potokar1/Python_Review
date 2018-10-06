#!/bin/python3      I COMMENTED OUT THE WEBSITE SPECIFIC CODE IN ORDER TO RUN IT THROUGH MY PERSONAL MACHINE :)

import math
import os
import random
import re
import sys

# Takes in an int and a 2d matrix. Does opperations on the created n-length array depending on the elements in queries
# Returns the max in the created array, array is changed based on the elements in queries


def arrayManipulation(n, queries):
    array = []
    max_in_array = 0
    for i in range(n):
        array.append(0)
    # For every row of the 2d matriz queries
    for row in range(len(queries)):
        # for every range of the indicies that we are increasing by queries[row][2]
        for i in range(queries[row][0], queries[row][1] + 1):
            array[i-1] += queries[row][2]
    for i in range(n):
        if array[i] > max_in_array:
            max_in_array = array[i]
    return max_in_array

# if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')


print('Please enter two values seperated by a space. The 1st value = length of array, the 2nd = the 2d matrix')
nm = input().split()

n = int(nm[0])

m = int(nm[1])

queries = []
print('Please enter the 2d matrix, values seperated by spaces, and get to the next row of the matrix by pressing enter')
for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

result = arrayManipulation(n, queries)

print(result)

#    fptr.write(str(result) + '\n')
#    fptr.close()

#!/bin/python3 I ALTERED THIS CODE IN ORDER TO MAKE IT RUN ON MY LOCAL MACHINE AND NOT JUST THE WEBSITE I DID IT ON.


import math
import os
import random
import re
import sys


# Complete the makeAnagram function below.
# The best way to remove a character is to replace it with nothing!
def makeAnagram(a, b):
    remove_count = 0
    a_in_b = ''
    b_in_a = ''
    temp_copy_a = a
    temp_copy_b = b
    for letter in range(len(a)):
        if a[letter] in temp_copy_b:
            a_in_b = a_in_b + a[letter]
            # self.replace(a,b) by default changed all occurences of the first and changes with with the second
            temp_copy_b = temp_copy_b.replace(a[letter], '', 1)
        else:
            # The third argument can override this, so 1 means only one occurence is changed and not all of them in the string
            temp_copy_a = temp_copy_a.replace(a[letter], '', 1)
            remove_count += 1
    return(remove_count + len(temp_copy_b))


# if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
print('Please enter two words that you wish to make anagrams out of, seperated by a return:')
a = input()

b = input()
print('Printing the total amount of character to remove in order to make both strings anagrams of each other.')
res = makeAnagram(a, b)
print(res)

#    fptr.write(str(res) + '\n')

#    fptr.close()

'''
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting.
He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note.
The words in his note are case-sensitive and he must use only whole words available in the magazine.
He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note,
print Yes if he can replicate his ransom note exactly using whole words from the magazine;
otherwise, print No.
'''

#!/bin/python3  I COMMENTED OUT THE WEBSITE SPECIFIC CODE SO IT CAN RUN ON MY OWN LOCAL MACHINE

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.


def checkMagazine(magazine, note):
    list_of_words_to_remove = []
    for word in note:
        list_of_words_to_remove.append(word)
        if word not in magazine:
            break
        else:
            magazine.remove(word)
    for word in list_of_words_to_remove:
        if word in note:
            note.remove(word)
        else:
            break
    if len(note) == 0:
        print('Yes')
    else:
        print('No')


# if __name__ == '__main__':
print('Please enter two values, seperated by a space, which 1st = words in magazine and 2nd = words in note')
mn = input().split()

m = int(mn[0])

n = int(mn[1])
print('Please enter {} words, sepereated by spaces, which is the words in the magazine'.format(m))
magazine = input().rstrip().split()
print('Please enter {} words, sepereated by spaces, which is the words in the note'.format(n))
note = input().rstrip().split()

checkMagazine(magazine, note)

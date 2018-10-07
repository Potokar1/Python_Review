'''
Use a stack data structure to convert integer values to binary

Example: 242 (I learned this in class!) (bottom up of remainder is bin of 242)
                remainder
242 / 2     -> 0
141 / 2     -> 1
60 / 2      -> 0
30 / 2      -> 0
15 / 2      -> 1
7 / 2       -> 1
3 / 2       -> 1
1 / 2       -> 1
'''

from stack import Stack


def div_by_2(dec_num):
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_num = ''
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num


print(div_by_2(242))

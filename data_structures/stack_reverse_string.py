# The pyton one liner for printing the reverse of a string is :
# print(input_str[::-1])
# But that's no fun

from stack import Stack

# Takes in a string and returns the reverse of that string
def reverse_string(input_str):
    s = Stack()
    rev_string = ''
    # Iterate over the chars in the string
    for i in range(len(input_str)):
        s.push(input_str[i])

    # Pop from the stack to get the reverse of the string
    while not s.is_empty():
        rev_string += s.pop()

    return rev_string


input = 'Hello i am input string'
print(input)
print(reverse_string(input))

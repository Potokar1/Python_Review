# Logic: We push onto the stack for each oppening brace ([{ and then pop for each closing brace )]}
# If they match they are balanced and properly nested!


# If stack has stuff left in it when there is no more input, then it is not balanced -> (()
# If stack has no stuff in it, and there is still input left, then not balanced -> ))

from stack import Stack

# Determines if two parethesis are a match
def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    else:
        return False

# Determines if a given string of parens is balanced or legal using a stack
def is_paren_balanced(paren_string):
    # Creating a stack
    s = Stack()
    is_balanced = True
    index = 0

    # put all of the oppening parens in the stack and the closing will remain for checking
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        # If it is an oppening parens push it on the stack
        if paren in '({[':
            s.push(paren)
        # It's a closing paren
        else:
            # If the stack is empty and we still have closing parens then obvi not balanced
            if s.is_empty():
                is_balanced = False
            # We need to check if the top (of stack) parens and the closing parens match
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1
    # If we go through the entire stack and string and no balancing errors occur then we have balance!
    if s.is_empty() and is_balanced:
        return True
    else:
        return False


print(is_paren_balanced('()'))
print(is_paren_balanced('()()'))
print(is_paren_balanced('()[()]()'))
print(is_paren_balanced('())'))
print(is_paren_balanced('(()'))

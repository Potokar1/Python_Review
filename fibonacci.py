# This is an example of the very basic recursive program implementing the fibonacci sequence
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print('Enter the index of the list that contains the fibonacci sequence')
n = int(input())
print('Calculating...')
print(fibonacci(n))


n = int(input())
if n % 2 != 0:
    print('Weird')
else:
    if n in [2, 3, 4, 5]:
        print('Not Weird')
    elif n > 5 and n <= 20:
        print('Weird')
    elif n > 20:
        print('Not Weird')

# Parameter a is a list
def bubble_sort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


def bubble_sort_better(a):
    unsorted = True
    decreasing_length = len(a) - 1
    while unsorted:
        unsorted = False
        for i in range(decreasing_length):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                unsorted = True
        decreasing_length -= 1
    return a


list = ['f', 'g', 'b', 'd', 'i', 'c', 'e', 'j', 'h', 'a']
print(bubble_sort(list))
list = ['f', 'g', 'b', 'd', 'i', 'c', 'e', 'j', 'h', 'a']
print(bubble_sort_better(list))
list = [9, 6, 2, 4, 8, 3, 5, 10, 7, 1]
print(bubble_sort(list))
list = [9, 6, 2, 4, 8, 3, 5, 10, 7, 1]
print(bubble_sort_better(list))

# O(n^2)


# Parameter a is a list
def insertion_sort_for(a):
    # Covers a range from the SECOND item of the list to the VERY END of the list
    for i in range(1, len(a)):
        # Covers a range of i's immediate left, all the way to the very beginning of the list (-1 is 'i - 1 = 0')
        # Step of negative one, which means we are moving left through the list
        for j in range(i-1, -1, -1):
            # If an item to the right is less than the item on it's left, then it will be swapped
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            # Item is in it's correct position
            else:
                break
    return a


def insertion_sort_while(a):
    for i in range(1, len(a)):
        j = i-1
        while a[j] > a[j+1] and j >= 0:
            a[j], a[j+1] = a[j+1], a[j]
            j -= 1
    return a


def insertion_sort_shift_not_swap(a):
    for i in range(1, len(a)):
        # Copies the current i value into this variable
        cur_num = a[i]
        j = i-1
        # Compare to cur_num and swap with the element on it's right if it needs to be swapped
        while a[j] > cur_num and j >= 0:
            a[j+1] = a[j]
            j -= 1
        # Put cur_num back into the sorted part of the list where it belongs
        a[j+1] = cur_num
    return a


list = ['f', 'g', 'b', 'd', 'i', 'c', 'e', 'j', 'h', 'a']
print(insertion_sort_for(list))
list = ['f', 'g', 'b', 'd', 'i', 'c', 'e', 'j', 'h', 'a']
print(insertion_sort_while(list))
list = ['f', 'g', 'b', 'd', 'i', 'c', 'e', 'j', 'h', 'a']
print(insertion_sort_shift_not_swap(list))
list = [9, 6, 2, 4, 8, 3, 5, 10, 7, 1]
print(insertion_sort_for(list))
list = [9, 6, 2, 4, 8, 3, 5, 10, 7, 1]
print(insertion_sort_while(list))
list = [9, 6, 2, 4, 8, 3, 5, 10, 7, 1]
print(insertion_sort_shift_not_swap(list))

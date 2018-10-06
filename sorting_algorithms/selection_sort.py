# O(n^2)


# Parameter a is a list
def selection_sort(a):
    # Iterate over the start of the list to the second last part of the list
    for i in range(0, len(a)-1):
        # This is how we keep track of the minimum value of the unsorted part of the list
        min_index = i
        # Iterate over the entire unsorted part of the list. aka i to the last element of a
        for j in range(i+1, len(a)):
            # Compare to find the min Item
            if a[j] < a[min_index]:
                # save the index of the min item
                min_index = j
        # Then we swap the min item into place when the min is not already in place (next min is already 'sorted')
        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
    return a


list = ['f', 'g', 'b', 'd', 'i', 'c', 'e', 'j', 'h', 'a']
print(selection_sort(list))
list = [9, 6, 2, 4, 8, 3, 5, 10, 7, 1]
print(selection_sort(list))

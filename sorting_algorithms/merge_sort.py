# O(nlogn)


# Divide into smaller lists
# Sort those smaller lists
# Merge those smaller lists together

# Parameter a is a list
def merge_sort_helper(a):
    # All you have to pass in is the list a :) user friendly
    merge_sort(a, 0, len(a)-1)
    return a

# Parameter: a is the list, first is the position of the starting index,
#                           last is the position of the last index


def merge_sort(a, first, last):
    # if there is more than one item in the list
    if first < last:
        # // = 'blast' this is the floor of division (truncated down for both positive and negative)
        middle = (first + last) // 2
        merge_sort(a, first, middle)
        merge_sort(a, middle+1, last)
        merge(a, first, middle, last)

# Parameter: a is the list, first is the position of the starting index,
#                           middle is the position of the middle index,
#                           last is the position of the last index


def merge(a, first, middle, last):
    left = a[first:middle + 1]
    right = a[middle + 1:last+1]
    # We will know when we reach the end of the index when we get these very large numbers
    left.append(9999999999)
    right.append(9999999999)
    # index for both split lists
    i = 0
    j = 0
    # Go through the full range of the elements in the list a
    for k in range(first, last+1):
        # if the left item is smaller, copy the left element to a, and increment the left index by one
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        # if the right item is smaller, copy the right element to a, and increment the right index by one
        else:
            a[k] = right[j]
            j += 1


list = [9, 6, 2, 4, 8, 3, 5, 10, 7, 1]
print(merge_sort_helper(list))

# Select a pivot, which we will use to split the list in half by comparing every other number to the pivot
# We will end up with a left partition and a right partition. Best splits list in half
# This can be better if there is less than a certain amount of values, then we can use selection sort


# Helps the user by just letting them pass in the list to be sorted.
# Parameter a is a list
def quick_sort_helper(a):
    quick_sort(a, 0, len(a)-1)
    return a

# The recursive method
# Parameter a is a list
#           low is the low index
#           high is the high index


def quick_sort(a, low, high):
    # If there is more than one item to be sorted
    if low < high:
        # Most of the work, returns the pivot
        pivot = partition(a, low, high)
        # All items left of the pivot
        quick_sort(a, low, pivot-1)
        # All items right of the pivot
        quick_sort(a, pivot+1, high)

# Parameter a is a list
#           low is the low index
#           high is the high index


def partition(a, low, high):
    # We get out pivot, which returns the pivot index
    pivot_index = get_pivot(a, low, high)
    # Get the pivot value which we are going to use to make out comparisons
    pivot_value = a[pivot_index]
    # Swap the pivot value into the left most position of our list
    a[pivot_index], a[low] = a[low], a[pivot_index]
    # Set a border which is where we replace any items in the list that is less than the pivot_value
    border = low
    # Iterate through our list from low to high
    for i in range(low, high+1):
        # If the item is less than the pivot-value, we swap it with out border value,
        # so border is the control point where left of border is < pivot_value
        if a[i] < pivot_value:
            border += 1
            a[i], a[border] = a[border], a[i]
    # When we are done, we swap out low value, which is the pivot_value, into the border position.
    a[low], a[border] = a[border], a[low]
    # Return border which is the index for the pivot
    return border

# Parameter a is a list
#           low is the low index
#           high is the high index


def get_pivot(a, low, high):
    # Get the middle index
    mid = (high + low) // 2
    pivot = high
    # These if elif does comparisons to choose the middle (median not mean) of the three indecies
    if a[low] < a[mid]:
        if a[mid] < a[high]:
            pivot = mid
    elif a[low] < a[high]:
        pivot = low
    return pivot


list = [9, 6, 2, 4, 8, 3, 5, 10, 7, 1]
print(quick_sort_helper(list))

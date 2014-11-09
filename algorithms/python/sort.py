import heapq

def insertion_sort(x):
    """
    Sorts an array x in non-decreasing order using the insertion sort
    algorithm.

    @type  x: array
    @param x: the array to sort

    @rtype: array
    @return: the sorted array
    """
    if len(x) <= 1:
        return x 

    for i, v in enumerate(x):
        j = i

        while j > 0 and x[j] < x[j - 1]:
            # Nice python idiom for swapping array elements
            x[j - 1], x[j] = x[j], x[j - 1]
            j -= 1
    
    return x

def merge_sort(x):
    """
    Sorts an array x in non-decreasing order using the merge sort algorithm.

    @type  x: array
    @param x: the array to sort

    @rtype: array
    @return: the sorted array
    """
    # Base case
    if len(x) <= 1:
        return x

    # Do the first division
    mid = len(x) / 2
    left = x[:mid]
    right = x[mid:]

    # Recursively sub-divide until base case reached
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

# Note: This function is implemented by heapq.merge() in Python 2.6+
def merge(left, right):
    """
    Merges two arrays in non-decreasing order.

    @type   left: array
    @param  left: one of the arrays to merge
    @type  right: array
    @param right: the other array to merge

    @rtype: array
    @return: the merged array
    """

    # Initialize merged array
    merged = []

    # Indices to keep track of position in left and right
    i, j = 0, 0

    # Loop until reached end of left or right
    while i < len(left) and j < len(right):
        # Add smaller element to merged (left element if equal)
        if left[i] <= right[j]:
            merged.append(left[i])
            # Move on to next element in left
            i += 1
        else:
            merged.append(right[j])
            # Move on to next element in right
            j += 1

    # Add leftover elements from either left or right to merged
    if left:
        merged.extend(left[i:])
    if right:
        merged.extend(right[j:])

    return merged

def selection_sort(x):
    """
    Sorts an array x in non-decreasing order using the selection sort
    algorithm.

    @type  x: array
    @param x: the array to sort

    @rtype: array
    @return: the sorted array
    """
    n = len(x)

    for i in range(n):
        min_idx = i;
        for j in range(i + 1, n):
            if x[j] < x[min_idx]:
                min_idx = j
        x[i], x[min_idx] = x[min_idx], x[i]

    return x

def bubble_sort(x):
    """
    Sorts an array x in non-decreasing order using the bubble sort algorithm.

    @type  x: array
    @param x: the array to sort

    @rtype: array
    @return: the sorted array
    """
    n = len(x)

    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if x[j] < x[j - 1]:
                x[j], x[j - 1] = x[j - 1], x[j]

    return x

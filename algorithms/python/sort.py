import math

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

def heap_sort(x):
    """
    Sorts an array x in non-decreasing order using the heap sort algorithm.

    @type  x: array
    @param x: the array to sort

    @rtype: array
    @return: the sorted array
    """
    n = len(x)

    # Build the heap by repeatedly sifting down the root
    start = int(math.floor((n - 2) / 2))
    while start >= 0:
        x = sift_down(x, start, n - 1)
        start -= 1

    end = n - 1
    while end > 0:
        x[0], x[end] = x[end], x[0]
        end -= 1
        x = sift_down(x, 0, end)

    return x

def sift_down(x, root, end):
    while 2 * root + 1 <= end:
        child = 2 * root + 1
        swap = root

        if x[swap] < x[child]:
            swap = child
        if child + 1 <= end and x[child] < x[child + 1]:
            child += 1
        if x[root] < x[child]:
            x[root], x[child] = x[child], x[root]
            root = child
        else:
            break

    return x

def quick_sort(x):
    return quick_sort_rec(x, 0, len(x) - 1)

def quick_sort_rec(x, m, n):
    if m < n:
        x, i, j = partition(x, m, n)
        x = quick_sort_rec(x, m, j)
        x = quick_sort_rec(x, i, n)

    return x

def partition(x, i, j):
    pivot = x[(i + j) / 2]

    while True:
        while x[i] < pivot:
            i += 1
        while x[j] > pivot:
            j -= 1

        if i <= j:
            x[i], x[j] = x[j], x[i]
            i += 1
            j -= 1

        if i > j:
            break

    return x, i, j

def quick_sort_v2(x):
    if len(x) <= 1:
        return x

    # Use first element as pivot
    pivot = x[0]
    first = quick_sort_v2([elem for elem in x[1:] if elem < pivot])
    second = quick_sort_v2([elem for elem in x[1:] if elem > pivot])

    # Include repeated pivots
    return first + x.count(pivot) * pivot + second

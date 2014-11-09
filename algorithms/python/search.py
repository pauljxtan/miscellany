def binary_search(x, v):
    """
    Searches for the value v in the sorted array x using a binary search
    algorithm. (Not stable, i.e. does not return the first occurrence of v.)

    @type  x: array
    @param x: the (sorted) array to search
    @type  v: number
    @param v: the number to search for
    
    @rtype: number
    @return: if found, the index of the value; otherwise, -1
    """
    low = 0
    high = len(x) - 1

    while low <= high:
        mid = (low + high) / 2
        if v < x[mid]:
            high = mid - 1
        elif v > x[mid]:
            low = mid + 1
        else:
            return mid

    return -1

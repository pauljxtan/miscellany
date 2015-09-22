def sum_rec_one(x):
    """
    Sums an array using down-by-one recursion.

    @type  x: iterable
    @param x: the array to sum

    @rtype: int
    @return: the sum of all array values
    """
    if len(x) == 0:
        return 0
    return x[0] + sum_rec_one(x[1:])

def sum_rec_halves(x):
    """
    Sums a list using division-in-halves recursion.

    @type  x: iterable
    @param x: the array to sum

    @rtype: int
    @return: the sum of all array values
    """
    n = len(x)
    if n == 0:
        return 0
    if n == 1:
        return x[0]
    # sum of 1st half plus sum of 2nd half
    return sum_rec_halves(x[:n/2]) + sum_rec_halves(x[n/2:])

def sum_rec_goingup_idx(x, i, j):
    """
    """
    if i < j:
        return x[i] + sum_rec_goingup_idx(x, i + 1, j)
    if i == j:
        return x[i]
    return 0

def sum_rec_goingup(x):
    return sum_rec_goingup_idx(x, 0, len(x) - 1)

def sum_rec_goingdown_idx(x, i, j):
    """
    """
    if i < j:
        return x[j] + sum_rec_goingup_idx(x, i, j - 1)
    if i == j:
        return x[i]
    return 0

def sum_rec_goingdown(x):
    return sum_rec_goingdown_idx(x, 0, len(x) - 1)

def sum_rec_edgecenter_idx(x, i, j):
    """
    """
    if i < j:
        return x[i] + x[j] + sum_rec_edgecenter_idx(x, i + 1, j - 1)
    if i == j:
        return x[i]
    return 0

def sum_rec_edgecenter(x):
    return sum_rec_edgecenter_idx(x, 0, len(x) - 1)

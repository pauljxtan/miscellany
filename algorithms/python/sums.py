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

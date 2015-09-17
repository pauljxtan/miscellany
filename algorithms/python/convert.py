def base10_to_basen(x, n):
    """
    Converts a number from base-10 (decimal) to base-n, where 2 <= n <= 9.

    @type  x: integer
    @param x: number in base-10
    @type  n: integer
    @param n: base to convert to
    
    @rtype: string
    @return: number in base-n
    """
    result = ""

    while x > 0:
        # Prepend remainder to result
        result = str(x % n) + result
        # Move to next position
        x /= n

    return result

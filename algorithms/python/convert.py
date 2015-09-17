SYMBOLS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c',
           'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def base10_to_basen(x, n):
    """
    Converts a number from base-10 (decimal) to base-n, where 1 <= n <= 36.

    @type  x: integer
    @param x: number in base-10
    @type  n: integer
    @param n: base to convert to (1 <= n <= 36)
    
    @rtype: string
    @return: number in base-n
    """
    result = ""

    # Base-1 is trivial
    if n == 1:
        return '1' * x

    while x > 0:
        # Prepend remainder to result
        result = SYMBOLS[x % n] + result
        # Move to next digit
        x /= n

    return result

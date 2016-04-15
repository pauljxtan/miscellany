def decimal_to_binary(d, n_bits=0):
    """
    Converts a decimal number to a binary number, represented as an array of
    bits.

    @type       x: integer
    @param      x: decimal number
    @type  n_bits: integer
    @param n_bits: number of bits (defaults to minimum multiple of 4)

    @rtype: int array
    @return: binary number
    """
    d = int(d)
    b = []

    while d > 0:
        b = [d % 2] + b
        d /= 2

    if n_bits < len(b):
        print "Setting bit length to minimum multiple of 4"
        while n_bits < len(b) or n_bits % 4 != 0:
            n_bits += 1

    # Pad with zeros as necessary
    while len(b) < n_bits:
        b = [0] + b

    return b

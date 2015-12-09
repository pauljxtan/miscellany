"""
Miscellaneous pieces of Python code.
"""

#==== DECORATORS

def get_call_str(func):
    """
    Returns a string representation of a function call and return value.
    """
    return lambda *args: "%s(%s, %s) = %s" % (func.func_name,
                                              " ,".join(map(str, args[:-1])),
                                              args[-1], func(*args))

#====
#==== FUNCTIONAL STUFF

def make_exponentiator(power):
    return lambda x: x**power

#---- Implementing standard functions using reduce()

def sum2(a):
    return reduce(lambda x, y: x + y, a)

def product(a):
    return reduce(lambda x, y: x * y, a)

def max2(a):
    return reduce(lambda x, y: x if x > y else y, a)

def min2(a):
    return reduce(lambda x, y: x if x < y else y, a)

def map2(f, a):
    return reduce(lambda x, y: x + [f(y)], a, [])

def filter2(f, a):
    return reduce(lambda x, y: x + ([y] if f(y) else []), a, [])

def union(sets):
    """
    Returns the union of multiple sets.
    """
    return reduce(lambda x, y: x | y, sets)

def intersection(sets):
    """
    Returns the intersection of multiple sets.
    """
    return reduce(lambda x, y: x & y, sets)

def reduce2(f, a):
    """
    My implementation of the reduce() function itself.
    """
    if len(a) == 0:
        raise ValueError("Reducing an empty list")
    if len(a) == 1:
        return a[0]
    if len(a) == 2:
        return f(a[0], a[1])
    return f(a[0], reduce2(f, a[1:]))

#---- Higher-order functions (Haskell-inspired)

def zip_with(f, a, b):
    if len(a) != len(b):
        raise ValueError("Lists have unequal lengths")
    if len(a) == 0:
        return a
    if len(a) == 1:
        return [f(a[0], b[0])]
    return [f(a[0], b[0])] + zip_with(f, a[1:], b[1:])

#====

def test():
    
    @get_call_str
    def add(*args):
        return sum(args)

    print add(1, 2, 3)
    print

    print make_exponentiator(0)(2)
    print make_exponentiator(1)(2)
    print make_exponentiator(2)(2)
    print make_exponentiator(3)(2)
    print make_exponentiator(4)(2)
    print

    a = [1, 2, 3, 4, 5]
    print sum2(a)
    print product(a)
    print max2(a)
    print min2(a)
    print map2(lambda x: x**2, a)
    print filter2(lambda x: x >= 3, a)
    print

    X = set(range(5))
    Y = set(range(1, 6))
    Z = set(range(3, 8))
    print union([X, Y, Z])
    print intersection([X, Y, Z])
    print

    b = [1, 3, 5, 7, 9]
    print zip_with(lambda x, y: x + y, a, b)
    print reduce(lambda x, y: x + y, a)
    print reduce2(lambda x, y: x + y, a)

if __name__ == '__main__':
    test()

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

#----

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

if __name__ == '__main__':
    test()

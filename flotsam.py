"""
Miscellaneous pieces of Python code.
"""

def get_call_str(func):
    """
    Returns a string representation of a function call and return value.
    """
    return lambda *args: "%s(%s, %s) = %s" % (func.func_name,
                                              " ,".join(map(str, args[:-1])),
                                              args[-1], func(*args))

def test():
    
    @get_call_str
    def add(x, y, z):
        return x + y + z

    print add(1, 2, 3)

if __name__ == '__main__':
    test()

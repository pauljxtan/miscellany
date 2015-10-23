"""
Some of these are clearly trivial, but included for completeness and
notational consistency.
"""

def AND(A, B):
    return int(A and B)

def OR(A, B):
    return int(A or B)

def NOT(A):
    return int(not A)

def NAND(A, B):
    return int(not (A and B))

def NOR(A, B):
    return int(not (A or B))

def XOR(A, B):
    return int((not A and B) or (A and not B))

def XNOR(A, B):
    return int((not A and not B) or (A and B))

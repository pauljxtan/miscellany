#!/usr/bin/env python

"""
Generates a Wolfram cellular automaton of a given rule.

Usage: python wolfram_automaton.py [rule number] [width] [height]
"""

import sys

def decimal_to_binary(d, n_bits):
    b = []
    while d > 0:
        b.append(d % 2)
        d /= 2
    while len(b) < n_bits:
        b.append(0)
    return list(reversed(b))

def binary_to_decimal(b):
    d = 0
    for i, v in enumerate(reversed(b)):
        d += v * 2**i
    return d

def display_rule_table(rule_num):
    print "---------------- WOLFRAM RULE %d ----------------" % rule_num

    # Print states
    s = "| "
    for i in range(7, -1, -1):
        state = decimal_to_binary(i, 3)
        s += "".join(map(str, state)) + " | "
    print s

    # Print outcomes
    s = "| "
    outcomes = decimal_to_binary(rule_num, 8)
    for outcome in outcomes:
        s += " %d  | " % outcome
    print s

    print "-------------------------------------------------"

def get_automaton(rule_num, width, height, first=None):
    rule_table = list(reversed(decimal_to_binary(rule_num, 8)))

    rows = []
    if not first:
        row0 = [0] * width
        row0[width / 2] = 1
    else:
        if len(first) != width:
            raise ValueError("First row does not match width")
        else:
            row0 = first
    rows.append(row0)

    for i in range(1, height):
        prev = rows[-1]
        new = [0] * width
        for j in range(1, width - 1):
            new[j] = rule_table[binary_to_decimal(prev[j - 1: j + 2])]
        rows.append(new)

    return rows

def display_automaton(rows):
    for row in rows:
        s = ""
        for elem in row:
            if elem == 0:
                s += " "
            else:
                s += "*"
        print s

def main():
    if len(sys.argv) < 4:
        print "Insufficient arguments"
        print "Usage: python wolfram_automaton.py [rule number] [width] [height]"
        sys.exit()

    rule_num = int(sys.argv[1])
    width = int(sys.argv[2])
    height = int(sys.argv[3])

    display_rule_table(rule_num)
    print "Generating automaton of width=%d and height=%d..." % (width, height)
    print
    rows = get_automaton(rule_num, width, height)
    display_automaton(rows)

if __name__ == '__main__':
    main()

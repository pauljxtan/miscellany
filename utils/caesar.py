#!/usr/bin/env python

"""
Encrypts or decrypts an input string using the Caesar cipher.
"""

import optparse
import os
import sys

def caesar_encrypt(instring, shift):
    """Encrypt with specified shift."""
    outstring = ''
    shift = shift % 26
    for char in instring:
        if char.isalpha():
            # UPPER-CASE
            if ord(char) in xrange(65, 91):
                if ord(char) + shift > 90:
                    outstring += chr(ord(char) - 26 + shift)
                else:
                    outstring += chr(ord(char) + shift)
            # lower-case
            elif ord(char) in xrange(97, 123):
                if ord(char) + shift > 122:
                    outstring += chr(ord(char) - 26 + shift)
                else:
                    outstring += chr(ord(char) + shift)
        else:
            outstring += char
    return outstring

def caesar_decrypt(instring, shift):
    """Decrypt with specified shift."""
    outstring = ''
    shift = shift % 26
    for char in instring:
        if char.isalpha():
            # UPPER-CASE
            if ord(char) in xrange(65, 91):
                if ord(char) - shift < 65:
                    outstring += chr(ord(char) + 26 - shift)
                else:
                    outstring += chr(ord(char) - shift)
            # lower-case
            elif ord(char) in xrange(97, 123):
                if ord(char) - shift < 97:
                    outstring += chr(ord(char) + 26 - shift)
                else:
                    outstring += chr(ord(char) - shift)
        else:
            outstring += char
    return outstring

def main():
    parser = optparse.OptionParser(usage="%prog [options]")
    parser.add_option("-e", "--encrypt", action="store_true", help="encrypt")
    parser.add_option("-d", "--decrypt", action="store_true", help="decrypt")
    parser.add_option("-s", "--shift", type="string", help="shift")
    parser.add_option("-i", "--input", type="string", help="input string")
    opts, args = parser.parse_args()

    if ((not opts.encrypt and not opts.decrypt)
        or (opts.encrypt and opts.decrypt)):
        print >> sys.stderr, "ERROR: please choose encrypt or decrypt mode"
        sys.exit(1)

    if opts.encrypt:
        result = caesar_encrypt(opts.input, int(opts.shift))
    elif opts.decrypt:
        result = caesar_decrypt(opts.input, int(opts.shift))

    print opts.input, "--->", result
    return 0

if __name__ == "__main__":
    main()

'''Advent of Code 2015 day 8: Matchsticks
   https://adventofcode.com/2015/day/8'''


import re


HEX_PATTERN = re.compile(r'\\x[0-9a-f]{2}')


def literal_storage(s):
    '''Return counts of (literal, memory) characters for string

    literal: #characters used to represent the string in code
    memory: #characters used in memory, using the following
            escapes after a backslash : backslash, ", x<code>
    where code is two hexadecimal characters.
    '''
    xform = s.replace(r'\\', '.')
    xform = xform.replace(r'\"', '.')
    xform = HEX_PATTERN.sub('.', xform)

    return len(s), len(xform) - 2


def encode_storage(s):
    '''Return counts of (encoded, literal) characters for string

    Note order is reversed compared to literal_storage because of
    how we're diffing.

    literal: #characters used to represent the string in code
    encoded: #characters used in an encoded repr where we escape
             all special characters (see literal_storage above)
    '''
    xform = s.replace('\x5c', r'\\')  # r'\' is not a thing!
    xform = xform.replace(r'"', r'\"')

    return len(xform) + 2, len(s)


def diff(lines, fn):
    '''Return diff of #characters in output of fn over lines'''
    total_a, total_b = 0, 0
    for l in lines:
        a, b = fn(l)
        total_a += a
        total_b += b
    return total_a - total_b


def run(args):  # pragma: no cover
    filename = args[0]
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    l = diff(lines, literal_storage)
    print(f'Difference in #characters for string literals vs. memory: {l}')

    e = diff(lines, encode_storage)
    print(f'Difference in #characters for string literals vs. encoded: {e}')

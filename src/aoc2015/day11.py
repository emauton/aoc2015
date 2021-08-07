'''Advent of Code 2015 day 11: Corporate Policy
   https://adventofcode.com/2015/day/11'''


def increment(password):
    '''"increment" a string of lowercase characters
    Just like counting up in base-26: xz + 1 = ya
    '''
    # Wraparound on overflow
    if password == 'z' * 8:
        return 'a' * 8

    # Go via ordinal reps of lowercase chars - probably not the most efficient
    # thing available but it'll do
    numeric = list(reversed([ord(c) for c in password]))
    zero = ord('a')
    wrap = ord('z')

    carry = 1
    for i in range(0, len(numeric)):
        numeric[i] += carry
        if numeric[i] > wrap:
            numeric[i] = zero
            carry = 1
        else:
            carry = 0

        if not carry:
            break

    if carry:
        numeric.append(zero)

    return ''.join(reversed([chr(n) for n in numeric]))


def contains_straight(password):
    '''Check whether password contains a 'straight' like abc or xyz'''
    numeric = list([ord(c) for c in password])
    for i in range(0, len(numeric) - 2):
        if (numeric[i+1] == numeric[i] + 1 and
                numeric[i+2] == numeric[i] + 2):
            return True
    return False


def contains_doubles(password):
    '''Check whether password contains two different 'doubles' like aa or xx
    They cannot overlap'''
    numeric = list([ord(c) for c in password])

    found = None
    index = 0
    for i in range(0, len(numeric) - 1):
        if (found and
                numeric[i+1] == numeric[i] and
                numeric[i] != found and
                index != i - 1):
            return True
        elif numeric[i+1] == numeric[i]:
            index = i
            found = numeric[i]
    return False


def is_valid(password):
    '''Check a password's validity by the new Security Elf's policy'''

    return ('i' not in password and
            'o' not in password and
            'l' not in password and
            contains_doubles(password) and
            contains_straight(password))


def next_valid(password):
    '''Return the next valid password by incrementing and testing'''
    while True:
        password = increment(password)
        if is_valid(password):
            return password


def run(args):  # pragma: no cover
    password = args[0]
    new = next_valid(password)
    print(f"Santa's next valid password is: {new}")

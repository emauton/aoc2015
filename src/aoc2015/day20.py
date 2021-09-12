'''Advent of Code 2015 day 20: Infinite Elves and Infinite Houses
   https://adventofcode.com/2015/day/20'''


import collections
import sympy.ntheory
import sys


def house_number(target, per_elf=10, max_deliveries=sys.maxsize):
    '''Return the number of the house that gets at least 'target' presents.
    Given that each elf delivers 'per_elf' presents, and finishes delivering
    after 'max_deliveries'.'''
    deliveries = collections.defaultdict(int)
    finished = set()
    n = 0
    while True:
        n += 1
        elves = set(sympy.ntheory.divisors(n))
        active = elves.difference(finished)

        presents = sum([d * per_elf for d in active])
        if presents >= target:
            return n

        for d in active:
            deliveries[d] += 1
            if deliveries[d] == max_deliveries:
                finished.add(d)


def run(args):  # pragma: no cover
    target = int(args[0])

    number = house_number(target)
    print(f'lowest house number: {number}')

    number = house_number(target, 11, 50)
    print(f'lowest house number for "limited" elves: {number}')

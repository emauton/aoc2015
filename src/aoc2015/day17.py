'''Advent of Code 2015 day 17: No Such Thing as Too Much
   https://adventofcode.com/2015/day/17'''


import itertools
import sys


def combinations(items):
    '''Generate all combinations of all lengths for combinations'''
    for length in range(0, len(items) + 1):
        yield from itertools.combinations(items, length)


def packings(containers, target):
    '''Generate all combinations of containers that fit target liters'''
    for c in combinations(containers):
        if sum(c) == target:
            yield c


def minimal_packings(solutions):
    '''Generate all solutions of minimal length'''
    minimal = sys.maxsize
    for s in solutions:
        minimal = min(len(s), minimal)
    for s in solutions:
        if len(s) == minimal:
            yield s


def run(args):  # pragma: no cover
    filename = args[0]
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    sizes = [int(line) for line in lines]
    solutions = list(packings(sizes, 150))
    minimal = list(minimal_packings(solutions))
    print(f'Number of solutions: {len(solutions)}')
    print(f'Number of minimal solutions: {len(minimal)}')

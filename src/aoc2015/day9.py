'''Advent of Code 2015 day 9: All in a Single Night
   https://adventofcode.com/2015/day/9'''

import collections
import itertools
import re
import sys


ROUTE_PATTERN = re.compile(r'^(.+) to (.+) = (\d+)$')


def parse(route):
    '''Parse a route pattern of the form "London to Dublin = 464"'''
    m = ROUTE_PATTERN.match(route)
    return m.group(1), m.group(2), int(m.group(3))


def make_lookup(routes):
    '''Make up a two-way distance lookup table from a list of routes'''
    table = collections.defaultdict(dict)
    for r in routes:
        start, end, distance = parse(r)
        table[start][end] = distance
        table[end][start] = distance
    return table


def maximal_routes(table):
    '''Compute the shortest and longest routes from a distance lookup table'''
    nodes = table.keys()
    routes = itertools.permutations(nodes, len(nodes))

    shortest = sys.maxsize * 2 + 1  # Not really max Python int, but huge
    longest = 0

    for r in routes:
        distance = 0
        prev, *tail = r
        for node in tail:
            distance += table[prev][node]
            prev = node
        shortest = min(distance, shortest)
        longest = max(distance, longest)

    return shortest, longest


def run(args):  # pragma: no cover
    filename = args[0]
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    lookup = make_lookup(lines)
    shortest, longest = maximal_routes(lookup)
    print(f'The shortest distance Santa can travel is {shortest}')
    print(f'The longest distance Santa can travel is {longest}')

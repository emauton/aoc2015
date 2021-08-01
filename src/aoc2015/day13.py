'''Advent of Code 2015 day 13: Knights of the Dinner Table
   https://adventofcode.com/2015/day/13'''


import collections
import itertools
import re


# E.g. Alice would lose 75 happiness units by sitting next to David.
SEATING_PATTERN = re.compile(r'^(.+) would (.+) (\d+) happiness units '
                             r'by sitting next to (.+)\.$')


def parse(seating):
    '''Return (name1, name2, happiness) for a seating pattern as above'''
    m = SEATING_PATTERN.match(seating)
    if m.group(2) == 'gain':
        happiness = int(m.group(3))
    else:
        happiness = -int(m.group(3))
    return m.group(1), m.group(4), happiness


def make_lookup(seatings):
    '''Make a two-way happiness lookup table from a list of seatings'''
    table = collections.defaultdict(dict)
    for s in seatings:
        name1, name2, happiness = parse(s)
        table[name1][name2] = happiness
    return table


def maximal_happiness(table):
    '''Compute the maximal happiness from happiness lookup table'''
    people = table.keys()
    seatings = itertools.permutations(people, len(people))

    maximal_happiness = 0
    for s in seatings:
        happiness = 0
        seating = list(s)
        prev = seating[-1]  # Make a "ring" of happiness lookups
        for person in seating:
            happiness += table[prev][person]
            happiness += table[person][prev]
            prev = person
        maximal_happiness = max(happiness, maximal_happiness)
    return maximal_happiness


def run(args):  # pragma: no cover
    filename = args[0]
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    lookup = make_lookup(lines)
    happiness = maximal_happiness(lookup)
    print(f'The maximal happiness from a seating arrangement is {happiness}')

    people = list(lookup.keys())
    for p in people:
        lookup[p]['Cian'] = 0
        lookup['Cian'][p] = 0
    new_happiness = maximal_happiness(lookup)
    print(f'The maximal happiness after I join in is {new_happiness}')

'''Advent of Code 2015 day 16: Aunt Sue
   https://adventofcode.com/2015/day/16'''


import re


# E.g.
# Sue 1: cars: 9, akitas: 3, goldfish: 0
AUNT_PATTERN = re.compile(r'^Sue (\d+): (.*)$')


def parse(line):
    '''Return number, dict for an Aunt Sue'''
    m = AUNT_PATTERN.match(line)
    number = int(m.group(1))
    fields = m.group(2).split(', ')
    values = {}
    for f in fields:
        key, val = f.split(': ')
        values[key] = int(val)
    return number, values


def parse_all(lines):
    '''Return a dict of {number: values} for all Aunt Sue notes in lines'''
    aunts = {}
    for line in lines:
        number, values = parse(line)
        aunts[number] = values
    return aunts


def match(aunts, evidence):
    '''Return a list of aunts whose notes match the evidence'''
    matches = []
    for number, values in aunts.items():
        matching = True
        for k, v in values.items():
            if v != evidence[k]:
                matching = False
                break
        if matching:
            matches.append(number)
    return matches


def match_ranges(aunts, evidence):
    '''Return a list of aunts whose notes match the evidence
    Handle ranges for specific values due to the outdated retroencabulator'''
    matches = []
    for number, values in aunts.items():
        matching = True
        for k, v in values.items():
            if k in ['cats', 'trees']:
                if v <= evidence[k]:
                    matching = False
                    break
            elif k in ['pomeranians', 'goldfish']:
                if v >= evidence[k]:
                    matching = False
                    break
            elif v != evidence[k]:
                matching = False
                break
        if matching:
            matches.append(number)
    return matches


def run(args):  # pragma: no cover
    filename = args[0]
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    aunts = parse_all(lines)
    evidence = {'children': 3,
                'cats': 7,
                'samoyeds': 2,
                'pomeranians': 3,
                'akitas': 0,
                'vizslas': 0,
                'goldfish': 5,
                'trees': 3,
                'cars': 2,
                'perfumes': 1}
    possible = match(aunts, evidence)
    print(f'Possible aunts: {possible}')

    possible = match_ranges(aunts, evidence)
    print(f'Possible aunts given outdated retroencabulator: {possible}')

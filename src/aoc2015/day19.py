'''Advent of Code 2015 day 19: Medicine for Rudolph
   https://adventofcode.com/2015/day/19'''


import random


def parse(lines):
    '''Get a list of replacements from lines'''
    return [tuple(line.split(' => ')) for line in lines]


def find(sub, s):
    '''Generate all indices of sub in s'''
    index = s.find(sub)
    while index != -1:
        yield index
        index = s.find(sub, index + 1)


def sub(key, index, new, s):
    '''Replace an instance of 'key' at 'index' with 'new' in s'''
    return f'{s[:index]}{new}{s[index + len(key):]}'


def possibilities(molecule, replacements):
    '''Generate single-step replacements possible in molecule given table'''
    for key, replace in replacements:
        for index in find(key, molecule):
            yield sub(key, index, replace, molecule)


def steps(molecule, replacements):
    '''Count the number of steps we need to get to 'molecule'''
    count = 0
    working = molecule

    while working != 'e':
        start = working
        for key, replace in replacements:
            while replace in working:
                count += working.count(replace)
                working = working.replace(replace, key)

        # If we stop making progress, try a new order of replacements
        if start == working:
            random.shuffle(replacements)
            working = molecule
            count = 0

    return count


def run(args):  # pragma: no cover
    filename = args[0]
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    molecule = lines[-1]
    replacements = parse(lines[:-2])
    distinct = set(possibilities(molecule, replacements))
    print(f'#distinct molecules given table of substitutions: {len(distinct)}')

    count = steps(molecule, replacements)
    print(f'#steps to produce the medicine molecule: {count}')

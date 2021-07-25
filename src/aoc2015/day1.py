'''Advent of Code 2015 day 1: Not Quite Lisp
   https://adventofcode.com/2015/day/1'''


def process(instructions):
    '''Generate a sequence of (position, floor) for the given instructions.

    Start at floor 0; go up a floor for each '(' and down a floor for each ')'

    The position counts from 1.
    '''
    floor = 0
    for pos, instr in enumerate(instructions):
        if instr == '(':
            floor += 1
        else:
            floor -= 1
        yield pos + 1, floor


def find_floor(instructions):
    '''Find the floor Santa ends up on after following the instructions'''
    *_, (_pos, floor) = process(instructions)  # Unpacking per PEP 448!
    return floor


def first_basement_entry(instructions):
    '''Find the first instruction where we enter the basement
    Return 0 if we never do.'''
    for pos, floor in process(instructions):
        if floor < 0:
            return pos
    return 0


def run(args):  # pragma: no cover
    filename = args[0]

    with open(filename) as f:
        data = f.read()

    floor = find_floor(data)
    pos = first_basement_entry(data)

    print(f"Santa's floor: {floor}")
    print(f"Santa's first entry to basement: {pos}")

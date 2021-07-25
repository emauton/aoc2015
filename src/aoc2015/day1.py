'''Advent of Code 2015 day 1: Not Quite Lisp
   https://adventofcode.com/2015/day/1'''

from aoc2015 import __version__


def find_floor(instructions):
    '''Find the floor Santa ends up on after following the instructions

    Start at floor 0; go up a floor for each ( and down a floor for each )

    Returns the resulting floor.
    '''
    floor = 0
    for instr in instructions:
        if instr == '(':
            floor += 1
        else:
            floor -= 1
    return floor


def first_basement_entry(instructions):
    '''Find the position of the instruction where we first enter the basement

    Following the same rules as find_floor. The position counts from 1.
    '''
    floor = 0
    for pos, instr in enumerate(instructions):
        if instr == '(':
            floor += 1
        else:
            floor -= 1
        if floor < 0:
            return pos + 1
    return 0


def run(args):  # pragma: no cover
    filename = args[0]

    with open(filename) as f:
        data = f.read()

    floor = find_floor(data)
    pos = first_basement_entry(data)

    print(f"Santa's floor: {floor}")
    print(f"Santa's first entry to basement: {pos}")

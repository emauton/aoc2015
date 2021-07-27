'''Advent of Code 2015 day 6: Probably a Fire Hazard
   https://adventofcode.com/2015/day/6'''


import re
import collections


Instruction = collections.namedtuple('Operation', ['op', 'start', 'end'])


INSTRUCTION_PATTERN = re.compile(r'^(.*) (\d+),(\d+) through (\d+),(\d+)$')


def parse(instruction):
    '''Parse an instruction of the form 'operation x1,y1 through x2,y2'
    Returns an Instruction namedtuple
    '''
    m = INSTRUCTION_PATTERN.match(instruction)
    start = int(m.group(2)), int(m.group(3))
    end = int(m.group(4)), int(m.group(5))
    return Instruction(m.group(1), start, end)


def indices_1000x1000(start, end):
    '''Generate all indices in the block delineated by start and end

    E.g. with start (0,0) and end (2,2), the block would be these 9 coords:
    (0,0) (1,0) (2,0)
    (0,1) (1,1) (2,1)
    (0,2) (1,2) (2,2)

    We treat a flat array of 1000000 elements as a 1000x1000 grid,
    where e.g. row y=1 is indices 1000 to 1999.

    So the indices returned for the above would be:
    0     1     2
    1000  1001  1002
    2000  2001  2002
    '''
    (x1, y1) = start
    (x2, y2) = end

    for y in range(y1, y2 + 1):
        for index in range(y*1000 + x1, y*1000 + x2 + 1):
            yield index


def apply_discrete_instr(lights, instr):
    '''Apply a single instruction for "discrete" lights
    That is, where the lights can be on or off - part one of the puzzle
    '''
    indices = indices_1000x1000(instr.start, instr.end)
    if instr.op == 'turn on':
        for i in indices:
            lights[i] = 1
    elif instr.op == 'turn off':
        for i in indices:
            lights[i] = 0
    else:  # toggle
        for i in indices:
            lights[i] = 1 if lights[i] == 0 else 0


def apply_variable_instr(lights, instr):
    '''Apply a single instruction for "variable" lights
    Here the lights have a brightness value - part two of the puzzle
    '''
    indices = indices_1000x1000(instr.start, instr.end)
    if instr.op == 'turn on':
        for i in indices:
            lights[i] += 1
    elif instr.op == 'turn off':
        for i in indices:
            lights[i] = max(0, lights[i] - 1)
    else:  # toggle
        for i in indices:
            lights[i] += 2


def compute_lights(instructions, apply_fn):
    '''Return lights grid after applying each instruction using apply_fn
    The grid is an array indexed as described in 'indices_1000x1000' above'''
    lights = [0] * 1000 * 1000
    for i in instructions:
        apply_fn(lights, i)
    return lights


def run(args):  # pragma: no cover
    filename = args[0]
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    instructions = [parse(line) for line in lines]

    discrete = compute_lights(instructions, apply_discrete_instr)
    count = sum(discrete)
    print(f'Discrete lights turned on after instruction processing: {count}')

    variable = compute_lights(instructions, apply_variable_instr)
    total = sum(variable)
    print(f'Total brightness of variable lights after instruction processing: {total}')

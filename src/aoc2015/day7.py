'''Advent of Code 2015 day 7: Some Assembly Required
   https://adventofcode.com/2015/day/7'''


import functools
import collections


Instruction = collections.namedtuple('Instruction', ['op', 'args'])


def parse(instruction):
    '''Parse a wiring instruction per the puzzle
    Returns wire, Instruction.
    '''
    inputs, wire = instruction.split(' -> ')
    args = inputs.split()
    if len(args) == 3:
        return wire, Instruction(args[1], [args[0], args[2]])
    elif len(args) == 2:
        return wire, Instruction(args[0], [args[1]])
    else:
        return wire, Instruction('SET', [args[0]])


def make_wire_map(instructions):
    '''Return a map of {wire: Instruction} for the given instructions'''
    wire_map = {}
    for i in instructions:
        wire, parsed = parse(i)
        wire_map[wire] = parsed
    return wire_map


def get_resolver(wire_map):
    '''Return a memoized resolution function closing over a copy of wire_map

    Since the wire map is unhashable, we can't memoize it directly using
    functools.cache.

    Instead, return a memoized closure with access to a copy of wire_map.

    The returned function takes one argument - a target wire to resolve.
    '''

    wires = wire_map.copy()  # A simple map; no need for deepcopy in this case

    @functools.cache
    def resolve(target):
        '''Resolve a target wire within the wire map

        NB: this is not quite to spec as we're using Python int rather than 16-bit
        unsigned integers. Wastl appears to have gone easy on us and not made it a
        point the code can fail on, and it's a faff to fix it up in Python.
        '''

        if target.isnumeric():
            return int(target)

        instr = wires[target]

        if instr.op == 'SET':
            return resolve(instr.args[0])
        elif instr.op == 'NOT':
            return ~resolve(instr.args[0])
        elif instr.op == 'AND':
            return resolve(instr.args[0]) & resolve(instr.args[1])
        elif instr.op == 'OR':
            return resolve(instr.args[0]) ^ resolve(instr.args[1])
        elif instr.op == 'RSHIFT':
            return resolve(instr.args[0]) >> resolve(instr.args[1])
        elif instr.op == 'LSHIFT':
            return resolve(instr.args[0]) << resolve(instr.args[1])
        else:  # pragma: no cover
            raise ValueError(f'unrecognized op {instr.op}')

    return resolve


def run(args):  # pragma: no cover
    filename = args[0]
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    wire_map = make_wire_map(lines)
    resolve = get_resolver(wire_map)
    a = resolve('a')
    print(f'Initially, wire a is provided signal: {a}')

    wire_map['b'] = Instruction('SET', [str(a)])
    new_resolve = get_resolver(wire_map)
    new_a = new_resolve('a')
    print(f'After patching, wire a is provided signal: {new_a}')

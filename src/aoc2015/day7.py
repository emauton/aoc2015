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


def memoize_first_arg(f):
    '''memoize a wrapped function by first argument only

    This is built specifically to wrap resolve() below, which has an unhashable
    second argument and so cannot use functools.cache directly.

    Since the wire map is "immutable" once built, this is a reasonable
    workaround.

    There are alternatives like closing over the wire map and other ideas, but
    a recursive, memoized approach feels natural here.
    '''
    cache = {}

    @functools.wraps(f)
    def wrapper(*args, **kwds):
        if args[0] in cache:
            return cache[args[0]]
        else:
            result = f(*args, **kwds)
            cache[args[0]] = result
            return result

    # Provide a method to clear the wrapper's cache per functools' lru_cache
    def cache_clear():
        cache.clear()

    wrapper.cache_clear = cache_clear
    return wrapper


@memoize_first_arg
def resolve(target, wires):
    '''Resolve a target wire within the wire map

    NB: this is not quite to spec as we're using Python int rather than 16-bit
    unsigned integers. Wastl appears to have gone easy on us and not made it a
    point the code can fail on, and it's a faff to fix it up in Python.
    '''

    if target.isnumeric():
        return int(target)

    instr = wires[target]

    if instr.op == 'SET':
        return resolve(instr.args[0], wires)
    elif instr.op == 'NOT':
        return ~resolve(instr.args[0], wires)
    elif instr.op == 'AND':
        return resolve(instr.args[0], wires) & resolve(instr.args[1], wires)
    elif instr.op == 'OR':
        return resolve(instr.args[0], wires) ^ resolve(instr.args[1], wires)
    elif instr.op == 'RSHIFT':
        return resolve(instr.args[0], wires) >> resolve(instr.args[1], wires)
    elif instr.op == 'LSHIFT':
        return resolve(instr.args[0], wires) << resolve(instr.args[1], wires)
    else:  # pragma: no cover
        raise ValueError(f'unrecognized op {instr.op}')


def run(args):  # pragma: no cover
    filename = args[0]
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    wire_map = make_wire_map(lines)
    a = resolve('a', wire_map)
    print(f'Initially, wire a is provided signal: {a}')

    resolve.cache_clear()
    wire_map['b'] = Instruction('SET', [str(a)])
    new_a = resolve('a', wire_map)
    print(f'After patching, wire a is provided signal: {new_a}')

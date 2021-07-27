from aoc2015.day7 import (Instruction, parse, make_wire_map, resolve)


def test_parse():
    assert parse('1 -> a') == ('a', Instruction('SET', ['1']))
    assert parse('NOT b -> a') == ('a', Instruction('NOT', ['b']))
    assert parse('b AND c -> a') == ('a', Instruction('AND', ['b', 'c']))


def test_make_wire_map():
    instructions = ['1 -> a', 'NOT a -> b']
    assert make_wire_map(instructions) == {'a': Instruction('SET', ['1']),
                                           'b': Instruction('NOT', ['a'])}


def test_resolve():
    instructions = ['123 -> x',
                    '456 -> y',
                    'x AND y -> d',
                    'x OR y -> e',
                    'x LSHIFT 2 -> f',
                    'y RSHIFT 2 -> g',
                    'NOT x -> h',
                    'NOT y -> i']

    wire_map = make_wire_map(instructions)

    assert resolve('d', wire_map) == 72
    assert resolve('e', wire_map) == 435
    assert resolve('f', wire_map) == 492
    assert resolve('g', wire_map) == 114

'''Advent of Code 2015 day 12: JSAbacusFramework.io
   https://adventofcode.com/2015/day/12'''


from pygments.lexers.data import JsonLexer
from pygments.token import Token


import json


def extract_numbers(data):
    '''Given JSON data, extract all numbers without respect for structure'''
    lexer = JsonLexer()
    for tokentype, value in lexer.get_tokens(data):
        if tokentype == Token.Literal.Number.Integer:
            yield int(value)


def extract_non_red_numbers(data):
    '''Given JSON data, extract all numbers from objects that are not "red"
    "red" objects have a value in them that is simply the string "red"'''

    structure = json.loads(data)

    def extract(obj):
        if isinstance(obj, int):
            yield obj
        elif isinstance(obj, list):
            for item in obj:
                yield from extract(item)
        elif isinstance(obj, dict):
            if 'red' not in obj.values():
                for item in obj.values():
                    yield from extract(item)

    return extract(structure)


def run(args):  # pragma: no cover
    filename = args[0]
    with open(filename) as f:
        data = f.read()

    total = sum(extract_numbers(data))
    print(f"Sum of all numbers in the Elves' document: {total}")

    non_red = sum(extract_non_red_numbers(data))
    print(f"Sum of all 'non-red' numbers in the Elves' document: {non_red}")

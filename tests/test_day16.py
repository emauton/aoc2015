from aoc2015.day16 import parse, parse_all, match, match_ranges


def test_parse():
    s = 'Sue 1: cars: 9, akitas: 3, goldfish: 0'
    assert parse(s) == (1, {'cars': 9, 'akitas': 3, 'goldfish': 0})


def test_parse_all():
    lines = ['Sue 1: cars: 9, akitas: 3, goldfish: 0',
             'Sue 2: akitas: 9, children: 3, samoyeds: 9']

    assert parse_all(lines) == {1: {'cars': 9, 'akitas': 3, 'goldfish': 0},
                                2: {'akitas': 9, 'children': 3, 'samoyeds': 9}}


def test_match():
    aunts = {1: {'cars': 9, 'akitas': 3, 'goldfish': 0},
             2: {'akitas': 9, 'children': 3, 'samoyeds': 9}}
    evidence = {'cars': 9, 'akitas': 3, 'goldfish': 0, 'children': 3,
                'samoyeds': 8}

    assert match(aunts, evidence) == [1]


def test_match_ranges():
    # cats: 5 in evidence means "cats > 5"
    # goldfish: 3 in evidence means "goldfish < 3"
    aunts = {1: {'cats': 9, 'akitas': 3, 'goldfish': 0},
             2: {'akitas': 9, 'children': 3, 'samoyeds': 9}}
    evidence = {'cats': 5, 'akitas': 3, 'goldfish': 3, 'children': 3,
                'samoyeds': 8}

    assert match_ranges(aunts, evidence) == [1]

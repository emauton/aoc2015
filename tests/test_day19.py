from aoc2015.day19 import (parse, find, sub, possibilities, steps)


def test_parse():
    lines = ['B => TiB',
             'B => TiRnFAr',
             'Ca => CaCa',
             'Ca => PB']
    replacements = parse(lines)
    assert replacements == [('B', 'TiB'),
                            ('B', 'TiRnFAr'),
                            ('Ca', 'CaCa'),
                            ('Ca', 'PB')]


def test_find():
    assert list(find('HO', 'HOHOHO')) == [0, 2, 4]
    assert list(find('HO', 'ahHOahHO')) == [2, 6]


def test_sub():
    assert sub('wor', 8, 'go', 'working world') == 'working gold'
    assert sub('Hell', 0, 'G', 'Hello world') == 'Go world'
    assert sub('ld', 9, 'k', 'Hello world') == 'Hello work'


def test_possibilities():
    lines = ['H => HO',
             'H => OH',
             'O => HH']
    replacements = parse(lines)
    molecules = set(possibilities('HOH', replacements))
    assert molecules == set(['HOOH', 'HOHO', 'OHOH', 'HHHH'])


def test_steps():
    lines = ['e => H',
             'e => O',
             'H => HO',
             'H => OH',
             'O => HH']
    replacements = parse(lines)
    assert steps('HOH', replacements) == 3
    assert steps('HOHOHO', replacements) == 6

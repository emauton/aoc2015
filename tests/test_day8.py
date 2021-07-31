from aoc2015.day8 import literal_storage, diff, encode_storage


def test_literal_storage():
    assert literal_storage(r'""') == (2, 0)
    assert literal_storage(r'"abc"') == (5, 3)
    assert literal_storage(r'"aaa\"aaa"') == (10, 7)
    assert literal_storage(r'"\x27"') == (6, 1)


def test_diff():
    lines = [r'""',
             r'"abc"',
             r'"aaa\"aaa"',
             r'"\x27"']
    assert diff(lines, literal_storage) == 12


def test_encode_storage():
    assert encode_storage(r'""') == (6, 2)
    assert encode_storage(r'"abc"') == (9, 5)
    assert encode_storage(r'"aaa\"aaa"') == (16, 10)
    assert encode_storage(r'"\x27"') == (11, 6)

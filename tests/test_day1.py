from aoc2015.day1 import find_floor, first_basement_entry


def test_find_floor():
    '''find_floor passes examples from the problem description'''
    assert find_floor('(())') == 0
    assert find_floor('()()') == 0

    assert find_floor('(((') == 3
    assert find_floor('(()(()(') == 3
    assert find_floor('))(((((') == 3

    assert find_floor(')))') == -3
    assert find_floor(')())())') == -3


def test_first_basement_entry():
    '''first_basement_entry passes examples from the problem description'''
    assert first_basement_entry(')') == 1
    assert first_basement_entry('()())') == 5

    # plus when we never enter the basement
    assert first_basement_entry('(((') == 0

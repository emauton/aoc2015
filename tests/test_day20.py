from aoc2015.day20 import house_number


def test_house_number():
    assert house_number(30) == 2
    assert house_number(70) == 4
    assert house_number(80) == 6
    assert house_number(120) == 6
    assert house_number(150) == 8


def test_house_number_limited():
    assert house_number(30, 10, 1) == 3
    assert house_number(80, 10, 1) == 8
    assert house_number(80, 10, 2) == 6

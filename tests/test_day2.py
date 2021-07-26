from aoc2015.day2 import parse, paper_size, ribbon_size, calculate_wrapping


def test_parse():
    assert parse('20x3x11') == [3, 11, 20]


def test_paper_size():
    assert paper_size([2, 3, 4]) == 58
    assert paper_size([1, 1, 10]) == 43


def test_ribbon_size():
    assert ribbon_size([2, 3, 4]) == 34
    assert ribbon_size([1, 1, 10]) == 14


def test_calculate_wrapping():
    dimensions = ['2x3x4', '1x1x10']
    assert calculate_wrapping(dimensions) == (58 + 43, 34 + 14)

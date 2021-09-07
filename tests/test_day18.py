from aoc2015.day18 import (parse, sum_coords, in_grid, neighbours, iteration,
                           lights_on, light_corners)

import time


def test_parse():
    text = ['.#.',
            '...',
            '#..']
    assert parse(text) == [['.', '#', '.'],
                           ['.', '.', '.'],
                           ['#', '.', '.']]


def test_sum_coords():
    assert sum_coords((0, 0), (3, 4)) == (3, 4)
    assert sum_coords((-1, 3), (8, 4)) == (7, 7)


def test_in_grid():
    text = ['.#.',
            '...',
            '#..']
    grid = parse(text)
    assert in_grid((0, 0), grid)
    assert in_grid((1, 2), grid)
    assert not in_grid((1, 3), grid)
    assert not in_grid((-1, 2), grid)


def test_neighbours():
    text = ['.#.',
            '...',
            '#..']
    grid = parse(text)
    assert neighbours((0, 0), grid) == sorted(['#', '.', '.'])
    assert neighbours((0, 1), grid) == ['.', '.', '.', '.', '.']
    assert neighbours((1, 1), grid) == sorted(['.', '#', '.',
                                               '.', '.',
                                               '#', '.', '.'])
    assert neighbours((2, 2), grid) == ['.', '.', '.']


def test_iteration():
    text = ['.#.#.#',
            '...##.',
            '#....#',
            '..#...',
            '#.#..#',
            '####..']
    expected = ['......',
                '......',
                '..##..',
                '..##..',
                '......',
                '......']
    grid = parse(text)
    outcome = parse(expected)

    for _ in range(4):
        grid = iteration(grid)
        print(grid)

    assert grid == outcome


def test_lights_on():
    text = ['.#.',
            '...',
            '#..']
    grid = parse(text)
    assert lights_on(grid) == 2


def test_light_corners():
    text = ['.#.',
            '...',
            '#..']
    grid = parse(text)
    light_corners(grid)
    assert lights_on(grid) == 5


def test_omg_so_slow():
    time.sleep(10)

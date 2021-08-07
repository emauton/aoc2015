from aoc2015.day15 import (Ingredient, parse, cookie_vals, partition,
                           highest_score)


def test_parse():
    a = ('Butterscotch: capacity -1, durability -2, flavor 6, '
         'texture 3, calories 8')

    assert parse(a) == Ingredient('Butterscotch', -1, -2, 6, 3, 8)


def test_cookie_vals():
    ingredients = [Ingredient('Butterscotch', -1, -2, 6, 3, 8),
                   Ingredient('Butterscotch', 2, 3, -2, -1, 3)]
    quantities = (44, 56)

    assert cookie_vals(ingredients, quantities) == (62842880, 520)


def test_partition():
    p2_2 = list(partition(2, 2))
    assert p2_2 == [(1, 1)]

    p10_2 = list(partition(10, 2))
    assert p10_2 == [(9, 1),
                     (8, 2),
                     (7, 3),
                     (6, 4),
                     (5, 5)]

    p10_2_7 = list(partition(10, 2, maximum=7))
    assert p10_2_7 == [(7, 3),
                       (6, 4),
                       (5, 5)]

    p4_2 = list(partition(4, 2))
    assert p4_2 == [(3, 1), (2, 2)]

    p5_2 = list(partition(5, 2))
    assert p5_2 == [(4, 1), (3, 2)]

    p3_3 = list(partition(3, 3))
    assert p3_3 == [(1, 1, 1)]

    p4_3 = list(partition(4, 3))
    assert p4_3 == [(2, 1, 1)]

    p5_3 = list(partition(5, 3))
    assert p5_3 == [(3, 1, 1), (2, 2, 1)]

    p10_4 = list(partition(10, 4))
    assert p10_4 == [(7, 1, 1, 1),
                     (6, 2, 1, 1),
                     (5, 3, 1, 1),
                     (5, 2, 2, 1),
                     (4, 4, 1, 1),
                     (4, 3, 2, 1),
                     (4, 2, 2, 2),
                     (3, 3, 3, 1),
                     (3, 3, 2, 2)]


def test_highest_score():
    ingredients = [Ingredient('Butterscotch', -1, -2, 6, 3, 8),
                   Ingredient('Butterscotch', 2, 3, -2, -1, 3)]

    assert highest_score(ingredients, 100) == 62842880
    assert highest_score(ingredients, 100, target=500) == 57600000

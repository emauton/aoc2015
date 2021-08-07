from aoc2015.day17 import packings, minimal_packings


def test_packings():
    containers = [20, 15, 10, 5, 5]

    solutions = list(packings(containers, 25))

    assert sorted(solutions) == sorted([(15, 10),
                                        (20, 5),
                                        (20, 5),
                                        (15, 5, 5)])


def test_minimal_packings():
    containers = [20, 15, 10, 5, 5]
    solutions = list(packings(containers, 25))
    minimal = list(minimal_packings(solutions))

    assert sorted(minimal) == sorted([(15, 10),
                                      (20, 5),
                                      (20, 5)])

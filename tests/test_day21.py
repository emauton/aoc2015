from aoc2015.day21 import (WEAPONS, ARMOUR, RINGS, Fighter,
                           base_builds, ring_builds, all_builds,
                           player_wins)


def test_base_builds():
    builds = list(base_builds())

    assert [WEAPONS[0]] in builds
    assert [WEAPONS[2], ARMOUR[3]] in builds


def test_ring_builds():
    builds = list(ring_builds())

    assert [] in builds
    assert [RINGS[0]] in builds
    assert [RINGS[0], RINGS[-1]] in builds


def test_all_builds():
    builds = list(all_builds())

    assert [WEAPONS[0]] in builds
    assert [WEAPONS[0], ARMOUR[-1]] in builds
    assert [WEAPONS[-1], ARMOUR[0], RINGS[0], RINGS[-1]] in builds


def test_player_wins():
    assert player_wins(Fighter(8, 5, 5), Fighter(12, 7, 2))
    assert not player_wins(Fighter(8, 4, 5), Fighter(12, 7, 2))

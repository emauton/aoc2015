from aoc2015.day3 import delivery_locations, unique_locations, partition


def test_locations():
    assert len(unique_locations('^v')) == 2
    assert len(unique_locations('^v^v^v^v^v')) == 2
    assert len(unique_locations('^>v<')) == 4
    *_, last = delivery_locations('^>v<')
    assert last == (0, 0)


def test_partition():
    instructions = '^>v<'
    even, odd = partition(instructions)
    assert list(even) == ['^', 'v']
    assert list(odd) == ['>', '<']

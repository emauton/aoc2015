from aoc2015.day14 import Reindeer, parse, race


def test_parse():
    a = ('Comet can fly 14 km/s for 10 seconds, '
         'but then must rest for 127 seconds.')

    assert parse(a) == Reindeer('Comet', 14, 10, 127)


def test_tick():
    r = Reindeer('Comet', 14, 1, 1)
    r.tick()
    assert r.distance == 14
    r.tick()
    assert r.distance == 14
    r.tick()
    assert r.distance == 28
    r.tick()
    assert r.distance == 28


def test_race():
    lines = [('Comet can fly 14 km/s for 10 seconds, '
              'but then must rest for 127 seconds.'),
             ('Dancer can fly 16 km/s for 11 seconds, '
              'but then must rest for 162 seconds.')]

    reindeer = race(lines, 1000)
    assert reindeer[0].distance == 1120
    assert reindeer[1].distance == 1056

    assert reindeer[0].points == 312
    assert reindeer[1].points == 689

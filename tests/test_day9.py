from aoc2015.day9 import parse, make_lookup, maximal_routes


def test_parse():
    assert parse('London to Dublin = 464') == ('London', 'Dublin', 464)


ROUTES = ['London to Dublin = 464',
          'London to Belfast = 518',
          'Belfast to Dublin = 141']


def test_make_lookup():
    assert make_lookup(ROUTES) == {'London': {'Dublin': 464,
                                              'Belfast': 518},
                                   'Dublin': {'London': 464,
                                              'Belfast': 141},
                                   'Belfast': {'London': 518,
                                               'Dublin': 141}}


def test_maximal_routes():
    table = make_lookup(ROUTES)
    assert maximal_routes(table) == (605, 982)

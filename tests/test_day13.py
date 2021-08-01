from aoc2015.day13 import parse, make_lookup, maximal_happiness


def test_parse():
    a = 'Alice would lose 75 happiness units by sitting next to David.'
    b = 'Alice would gain 71 happiness units by sitting next to Eric.'

    assert parse(a) == ('Alice', 'David', -75)
    assert parse(b) == ('Alice', 'Eric', 71)


def test_make_lookup():
    s = ['Alice would lose 75 happiness units by sitting next to David.',
         'Alice would gain 71 happiness units by sitting next to Eric.',
         'David would lose 51 happiness units by sitting next to Alice.',
         'David would gain 91 happiness units by sitting next to Eric.',
         'Eric would gain 23 happiness units by sitting next to Alice.',
         'Eric would lose 47 happiness units by sitting next to David.']

    assert make_lookup(s) == {'Alice': {'David': -75, 'Eric': 71},
                              'David': {'Alice': -51, 'Eric': 91},
                              'Eric': {'Alice': 23, 'David': -47}}


def test_maximal_happiness():
    s = ['Alice would gain 54 happiness units by sitting next to Bob.',
         'Alice would lose 79 happiness units by sitting next to Carol.',
         'Alice would lose 2 happiness units by sitting next to David.',
         'Bob would gain 83 happiness units by sitting next to Alice.',
         'Bob would lose 7 happiness units by sitting next to Carol.',
         'Bob would lose 63 happiness units by sitting next to David.',
         'Carol would lose 62 happiness units by sitting next to Alice.',
         'Carol would gain 60 happiness units by sitting next to Bob.',
         'Carol would gain 55 happiness units by sitting next to David.',
         'David would gain 46 happiness units by sitting next to Alice.',
         'David would lose 7 happiness units by sitting next to Bob.',
         'David would gain 41 happiness units by sitting next to Carol.']
    lookup = make_lookup(s)

    assert maximal_happiness(lookup) == 330

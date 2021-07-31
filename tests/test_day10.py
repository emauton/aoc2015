from aoc2015.day10 import look_say, iterate


def test_look_say():
    assert look_say('1') == '11'
    assert look_say('11') == '21'
    assert look_say('21') == '1211'
    assert look_say('1211') == '111221'
    assert look_say('111221') == '312211'


def test_iterate():
    assert iterate('1', 5) == '312211'

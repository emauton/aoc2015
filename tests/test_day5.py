from aoc2015.day5 import is_nice1, is_nice2


def test_is_nice1():
    assert is_nice1('ugknbfddgicrmopn')
    assert is_nice1('aaa')
    assert not is_nice1('jchzalrnumimnmhp')
    assert not is_nice1('haegwjzuvuyypxyu')
    assert not is_nice1('dvszwmarrgswjxmb')


def test_is_nice2():
    assert is_nice2('qjhvhtzxzqqjkmpb')
    assert is_nice2('xxyxx')
    assert not is_nice2('uurcxstgmygtbstg')
    assert not is_nice2('ieodomkazucvgmuy')

from aoc2015.day11 import (increment, contains_straight, contains_doubles,
                           is_valid, next_valid)


def test_increment():
    assert increment('a') == 'b'
    assert increment('z') == 'aa'
    assert increment('xx') == 'xy'
    assert increment('xz') == 'ya'
    assert increment('abz') == 'aca'
    assert increment('zzzzzzzz') == 'aaaaaaaa'


def test_contains_straight():
    assert contains_straight('abc')
    assert contains_straight('xyz')
    assert contains_straight('aabbcxyz')
    assert contains_straight('abcddeef')
    assert contains_straight('aabcdeef')
    assert not contains_straight('aabbccdd')


def test_contains_doubles():
    assert not contains_doubles('aabc')
    assert not contains_doubles('abcde')
    assert contains_doubles('aabb')


def test_is_valid():
    assert not is_valid('hijklmmn')  # because it contains i and l
    assert not is_valid('abbceffg')  # because it has no increasing straight
    assert not is_valid('abbcegjk')  # because it only has one double letter
    assert is_valid('abcdffaa')
    assert is_valid('ghjaabcc')


def test_next_valid():
    assert next_valid('abcdefgh') == 'abcdffaa'

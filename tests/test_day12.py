from aoc2015.day12 import extract_numbers, extract_non_red_numbers


def test_extract_numbers():
    list(extract_numbers('[1,2,3]')) == [1, 2, 3]
    list(extract_numbers('{"a":2,"b":4}')) == [2, 4]
    list(extract_numbers('[[[3]]]')) == [3]
    list(extract_numbers('{"a":{"b":4},"c":-1}')) == [4, -1]
    list(extract_numbers('{"a":[-1,1]}')) == [-1, 1]
    list(extract_numbers('[-1,{"a":1}]')) == [-1, 1]


def test_extract_non_red_numbers():
    list(extract_non_red_numbers('[1,2,3]')) == [1, 2, 3]
    list(extract_non_red_numbers('[1,{"c":"red","b":2},3]')) == [1, 3]
    list(extract_non_red_numbers('{"d":"red","e":[1,2,3,4],"f":5}')) == []
    list(extract_non_red_numbers('[1,"red",5]')) == [1, 5]

'''Advent of Code 2015 day 5: Doesn't He Have Intern-Elves For This?
   https://adventofcode.com/2015/day/5'''


import re


def contains_any(string, subs):
    any([s in string for s in subs])


DOUBLE_PATTERN = re.compile(r'(.)\1')
PAIR_REPEAT_PATTERN = re.compile(r'(..).*\1')
SANDWICH_PATTERN = re.compile(r'(.).\1')


def is_nice1(string):
    '''nice: contains three vowels (not necessarily different) AND
       nice: contains at least one letter that appears twice in a row

       naughty: contains ab cd pq or xy
    '''
    return (len([c for c in string if c in 'aeiou']) >= 3
            and DOUBLE_PATTERN.search(string)
            and not any([s in string for s in ['ab', 'cd', 'pq', 'xy']]))


def is_nice2(string):
    '''nice: any pair of characters appears twice (not overlapping) AND
       nice: at least one letter repeats with exactly one letter between.
    '''
    return (PAIR_REPEAT_PATTERN.search(string)
            and SANDWICH_PATTERN.search(string))


def run(args):  # pragma: no cover
    filename = args[0]
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    nice1 = list(filter(is_nice1, lines))
    nice2 = list(filter(is_nice2, lines))
    print(f'Number of strings nice by first set of rules: {len(nice1)}')
    print(f'Number of strings nice by second set of rules: {len(nice2)}')

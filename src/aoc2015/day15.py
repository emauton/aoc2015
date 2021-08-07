'''Advent of Code 2015 day 15: Science for Hungry People
   https://adventofcode.com/2015/day/15'''


import collections
import itertools
import re
import sys


# E.g.
# Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
INGREDIENT_PATTERN = re.compile(r'^(.+): capacity ([0-9-]+), '
                                r'durability ([0-9-]+), flavor ([0-9-]+), '
                                r'texture ([0-9-]+), calories ([0-9-]+)$')


Ingredient = collections.namedtuple('Ingredient',
                                    ['name', 'capacity', 'durability',
                                     'flavor', 'texture', 'calories'])


def parse(ingredient):
    '''Return Ingredient tuple for an entry as above'''
    m = INGREDIENT_PATTERN.match(ingredient)
    return Ingredient(m.group(1), int(m.group(2)),
                      int(m.group(3)), int(m.group(4)),
                      int(m.group(5)), int(m.group(6)))


def cookie_vals(ingredients, quantities):
    '''Return (score, calories) for the ingredients, quantities passed'''
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0

    for n, i in enumerate(ingredients):
        capacity += i.capacity * quantities[n]
        durability += i.durability * quantities[n]
        flavor += i.flavor * quantities[n]
        texture += i.texture * quantities[n]
        calories += i.calories * quantities[n]

    # "Clamp" to a natural number - negatives are 0
    capacity = capacity if capacity > 0 else 0
    durability = durability if durability > 0 else 0
    flavor = flavor if flavor > 0 else 0
    texture = texture if texture > 0 else 0

    score = capacity * durability * flavor * texture
    return score, calories


def partition(n, p, maximum=sys.maxsize):
    '''Generate unique, sorted p-partitions of n
    'maximum' serves our recursive definition - we want to be able to restrict
    partitions to those with a max value in any "column"'''

    start = min(n - (p - 1), maximum)
    remainder = n - start
    n = start
    m = remainder

    if p == 2:  # base case
        while n >= m:
            yield (n, m)
            n, m = n - 1, m + 1
        return

    while n > 0:
        for sub in partition(m, p - 1, maximum=n):
            yield (n,) + sub
        n, m = n - 1, m + 1


def highest_score(ingredients, teaspoons, target=None):
    '''Highest score for ingredients using this many teaspoons
    Optionally, specify a target calorie value to score only cookies
    that exactly match it'''
    orders = list(itertools.permutations(ingredients))
    quantities = list(partition(teaspoons, len(ingredients)))
    highest = 0
    for o in orders:
        for q in quantities:
            score, calories = cookie_vals(o, q)

            if target:
                if calories == target:
                    highest = max(score, highest)
            else:
                highest = max(score, highest)
    return highest


def run(args):  # pragma: no cover
    filename = args[0]
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    ingredients = [parse(line) for line in lines]
    score = highest_score(ingredients, 100)
    print(f'The highest-scoring cookie scores {score}')

    score = highest_score(ingredients, 100, target=500)
    print(f'The highest-scoring cookie with 500 cals scores {score}')

'''Advent of Code 2015 day 21: RPG Simulator 20XX
   https://adventofcode.com/2015/day/21'''

import dataclasses
import operator


@dataclasses.dataclass
class Item:
    '''An inventory item'''
    name: str
    cost: int
    damage: int
    armour: int


@dataclasses.dataclass
class Fighter:
    '''A simulated fighter'''
    health: int
    damage: int
    armour: int


WEAPONS = [Item('Dagger', 8, 4, 0),
           Item('Shortsword', 10, 5, 0),
           Item('Warhammer', 25, 6, 0),
           Item('Longsword', 40, 7, 0),
           Item('Greataxe', 74, 8, 0)]


ARMOUR = [Item('Leather', 13, 0, 1),
          Item('Chainmail', 31, 0, 2),
          Item('Splintmail', 53, 0, 3),
          Item('Bandedmail', 75, 0, 4),
          Item('Platemail', 102, 0, 5)]


RINGS = [Item('Damage +1', 25, 1, 0),
         Item('Damage +2', 50, 2, 0),
         Item('Damage +3', 100, 3, 0),
         Item('Defense +1', 20, 0, 1),
         Item('Defense +2', 40, 0, 2),
         Item('Defense +3', 80, 0, 3)]


def base_builds():
    '''Generate all possible "base" builds of weapons and armour'''
    for w in WEAPONS:
        yield [w]

    for w in WEAPONS:
        for a in ARMOUR:
            yield [w, a]


def ring_builds():
    '''Generate all possible ring builds of 0-2 rings'''
    yield []

    for r in RINGS:
        yield [r]

    working = RINGS.copy()

    while working:
        r = working[0]
        for s in working[1:]:
            yield [r, s]
        working = working[1:]


def all_builds():
    '''Generate all possible item builds as lists of items'''
    for b in base_builds():
        for r in ring_builds():
            yield b + r


def resolve_build(items):
    '''Compile all items in a build into a pseudo-item representing them'''
    cost = damage = armour = 0
    for i in items:
        cost += i.cost
        damage += i.damage
        armour += i.armour
    return Item(str(items), cost, damage, armour)


def player_wins(player, boss):
    '''Given a player and a boss as 'Fighter' objects, does the player win?'''
    attacker, defender = player, boss
    while attacker.health > 0 and defender.health > 0:
        defender.health -= max(1, attacker.damage - defender.armour)
        attacker, defender = defender, attacker
    return player.health > 0


def minimal_winning_build(boss, health, builds):
    '''Return lowest-cost build that can defeat 'boss' given 'health'.'''
    winning = []
    for build in builds:
        boss_copy = dataclasses.replace(boss)
        resolved = resolve_build(build)
        player = Fighter(health, resolved.damage, resolved.armour)
        if player_wins(player, boss_copy):
            winning.append(resolved)

    winning = sorted(winning, key=operator.attrgetter('cost'))
    return winning[0]


def maximal_losing_build(boss, health, builds):
    '''Return highest-cost build that can lose against 'boss' given 'health'.'''
    losing = []
    for build in builds:
        boss_copy = dataclasses.replace(boss)
        resolved = resolve_build(build)
        player = Fighter(health, resolved.damage, resolved.armour)
        if not player_wins(player, boss_copy):
            losing.append(resolved)

    losing = sorted(losing, key=operator.attrgetter('cost'), reverse=True)
    return losing[0]


def run(args):  # pragma: no cover
    build = minimal_winning_build(Fighter(103, 9, 2), 100, all_builds())
    print(f'minimal cost build to defeat boss: {build.cost}; {build.name}')

    build = maximal_losing_build(Fighter(103, 9, 2), 100, all_builds())
    print(f'maximal cost build to lose to boss: {build.cost}; {build.name}')

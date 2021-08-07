'''Advent of Code 2015 day 14: Reindeer Olympics
   https://adventofcode.com/2015/day/14'''


import re


class Reindeer(object):
    def __init__(self, name, speed, duration, rest):
        self.name = name
        self.speed = speed
        self.duration = duration
        self.rest = rest

        self.distance = 0
        self.time = 0
        self.traveling = duration
        self.resting = 0
        self.points = 0

    def __eq__(self, other):
        return (self.name == other.name and
                self.speed == other.speed and
                self.duration == other.duration and
                self.rest == other.rest)

    def tick(self):
        # On each tick, we are either traveling or resting.

        # We decrement the appropriate counter, and "flip" to the other state
        # when we hit zero. Using fewer state variables here would be fine but
        # not more readable, I think.
        self.time += 1

        if self.traveling:
            self.distance += self.speed
            self.traveling -= 1
            if self.traveling == 0:
                self.resting = self.rest
        else:
            self.resting -= 1
            if self.resting == 0:
                self.traveling = self.duration

    def score(self):
        self.points += 1


# E.g. 'Comet can fly 14 km/s for 10 seconds, but then must rest for 127
#       seconds.'
REINDEER_PATTERN = re.compile(r'^(.+) can fly (\d+) km/s for (\d+) seconds, '
                              r'but then must rest for (\d+) seconds\.$')


def parse(reindeer):
    '''Return Reindeer tuple for a reindeer entry as above'''
    m = REINDEER_PATTERN.match(reindeer)
    return Reindeer(m.group(1), int(m.group(2)),
                    int(m.group(3)), int(m.group(4)))


def race(lines, seconds):
    '''Run a race for the reindeer defined by lines over seconds'''
    reindeer = [parse(line) for line in lines]

    for i in range(0, seconds):
        for r in reindeer:
            r.tick()

        distance = 0
        for r in reindeer:
            if r.distance > distance:
                distance = r.distance

        for r in reindeer:
            if r.distance == distance:
                r.score()

    return reindeer


def run(args):  # pragma: no cover
    filename = args[0]
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    reindeer = race(lines, 2503)

    distance = 0
    for r in reindeer:
        distance = max(distance, r.distance)
    print(f'The winning reindeer travels {distance} km')

    points = 0
    for r in reindeer:
        points = max(points, r.points)
    print(f'After changing the rules, the winner has {points} points')

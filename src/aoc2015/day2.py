'''Advent of Code 2015 day 2: I Was Told There Would Be No Math
   https://adventofcode.com/2015/day/2'''


def parse(dimensions_string):
    '''Parse a dimensions string like 20x3x11

    We re-sort because for calculating paper and ribbon sizes we don't need to
    care which is length, width and height - in fact, the sorted rep makes
    calculations easier.

    Return a sorted triple of integers e.g. [3, 11, 20]
    '''
    return sorted([int(i) for i in dimensions_string.split('x')])


def paper_size(dimensions):
    '''Return required wrapping paper for the box with these dimensions'''
    l, w, h = dimensions
    surface_area = 2*l*w + 2*l*h + 2*w*h
    wrapping_slack = l*w
    return surface_area + wrapping_slack


def ribbon_size(dimensions):
    '''Return required ribbon for the box with these dimensions'''
    l, w, h = dimensions
    smallest_perimeter = 2*l + 2*w
    bow_slack = l*w*h
    return smallest_perimeter + bow_slack


def calculate_wrapping(lines):
    '''Calculate total wrapping for a set of raw dimension lines
    Return a tuple of total paper, total ribbon required
    '''
    all_dimensions = [parse(line) for line in lines]
    paper = sum([paper_size(d) for d in all_dimensions])
    ribbon = sum([ribbon_size(d) for d in all_dimensions])
    return paper, ribbon


def run(args):  # pragma: no cover
    filename = args[0]
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    paper, ribbon = calculate_wrapping(lines)
    print(f'Wrapping paper needed by the elves: {paper}')
    print(f'Ribbon needed by the elves: {ribbon}')

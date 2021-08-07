'''Advent of Code 2015 day 18: Like a GIF For Your Yard
   https://adventofcode.com/2015/day/18'''


def parse(lines):
    '''Given a list of n lines, return a grid of characters'''
    return [list(line) for line in lines]


def sum_coords(p, q):
    '''Sum two coordinate pairs'''
    return tuple(i + j for i, j in zip(p, q))


def in_grid(p, grid):
    '''Test whether coordinate pair p is in grid'''
    x, y = p
    return (x >= 0 and x < len(grid) and
            y >= 0 and y < len(grid[0]))


def neighbours(coord, grid):
    '''Return the list of neighbours of grid[x][y] for coord (x, y)
    Note we use x y here for convenience rather than as their usual
    axis values'''
    deltas = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i, j) != (0, 0):
                deltas.append((i, j))

    candidates = [sum_coords(coord, d) for d in deltas]
    coords = [c for c in candidates if in_grid(c, grid)]

    results = []
    for x, y in coords:
        results.append(grid[x][y])
    return sorted(results)


def iteration(grid):
    '''Run one iteration of Santa's animation on the grid'''
    size = len(grid)
    new = [['.' for _ in range(size)] for _ in range(size)]
    for x in range(size):
        for y in range(size):
            on = [light for light in neighbours((x, y), grid) if light == '#']
            if grid[x][y] == '.':
                if len(on) == 3:
                    new[x][y] = '#'
            elif grid[x][y] == '#':
                if len(on) in [2, 3]:
                    new[x][y] = '#'
    return new


def lights_on(grid):
    '''Count the number of lights on in a grid'''
    lights = 0
    size = len(grid)
    for x in range(size):
        for y in range(size):
            if grid[x][y] == '#':
                lights += 1
    return lights


def light_corners(grid):
    n = len(grid) - 1
    grid[0][0] = '#'
    grid[n][n] = '#'
    grid[0][n] = '#'
    grid[n][0] = '#'


def run(args):  # pragma: no cover
    filename = args[0]
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    grid = parse(lines)
    for _ in range(100):
        grid = iteration(grid)
    lights = lights_on(grid)
    print(f'#lights after 100 iterations: {lights}')

    grid = parse(lines)
    for _ in range(100):
        light_corners(grid)
        grid = iteration(grid)
    light_corners(grid)
    lights = lights_on(grid)
    print(f'#lights after 100 iterations with stuck corners: {lights}')

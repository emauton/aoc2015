'''Advent of Code 2015 day 10: Elves Look, Elves Say
   https://adventofcode.com/2015/day/10'''


def look_say(number):
    '''Do a single look-and-say iteration over number

    This is an interesting example where Python's iterators seem to fall down
    a bit for handling sequences - because e.g. itertools.takewhile consumes
    "one past" its end. So, back to C style index wrangling.

    Cf. https://adventofcode.com/2015/day/10'''
    result = ''

    i = 0
    while i < len(number):
        n = number[i]
        j = i + 1
        while j < len(number) and number[j] == n:
            j += 1
        count = j - i
        result += f'{count}{n}'
        i = j
    return result


def iterate(number, times):
    '''Iterate look_say over number x times'''
    for i in range(0, times):
        number = look_say(number)
    return number


def run(args):  # pragma: no cover
    number = args[0]
    times = int(args[1])
    result = iterate(number, times)
    print(f'length for {number} after {times} turns: {len(result)}')

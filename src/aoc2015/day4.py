'''Advent of Code 2015 day 4: The Ideal Stocking Stuffer
   https://adventofcode.com/2015/day/4'''


import hashlib


def generate_hashes(key):
    '''Generate a sequence (index, hexdigest) of MD5 hashes of (key, index)
    where index runs through the positive natural numbers
    '''
    n = 0
    while True:
        n += 1
        val = f'{key}{n}'
        h = hashlib.md5(val.encode('utf-8'))
        yield n, h.hexdigest()


def mine_coin(key, prefix):
    '''Return the first index where hash hex of key+index starts with prefix'''
    for n, h in generate_hashes(key):
        if h.startswith(prefix):
            return n


def run(args):  # pragma: no cover
    key = args[0]
    five_zero = mine_coin(key, '00000')
    six_zero = mine_coin(key, '000000')
    print(f'First five-zero coin: {five_zero}')
    print(f'First six-zero coin: {six_zero}')

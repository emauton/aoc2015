'''Cian's try for Advent of Code 2015'''

import argparse
import importlib
import logging
import sys

from aoc2015 import __version__

_logger = logging.getLogger(__name__)


def parse_args(args):
    '''Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    '''
    parser = argparse.ArgumentParser(description='AoC 2015 commandline driver')
    parser.add_argument(
        '--version',
        action='version',
        version='aoc2015 {ver}'.format(ver=__version__),
    )
    parser.add_argument(dest='day', help='the number of the AoC day to run',
                        type=int, metavar='DAY')
    parser.add_argument(
        '-v',
        '--verbose',
        dest='loglevel',
        help='set loglevel to INFO',
        action='store_const',
        const=logging.INFO,
    )
    parser.add_argument(
        '-vv',
        '--very-verbose',
        dest='loglevel',
        help='set loglevel to DEBUG',
        action='store_const',
        const=logging.DEBUG,
    )
    return parser.parse_known_args(args)


def setup_logging(loglevel):
    '''Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    '''
    logformat = '[%(asctime)s] %(levelname)s:%(name)s:%(message)s'
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt='%Y-%m-%d %H:%M:%S'
    )


def dispatch(args):
    '''Dispatch to the run() function for a particular day'''
    args, remainder = parse_args(args)
    setup_logging(args.loglevel)

    _logger.debug(f'Dispatching for day {args.day}')
    name = f'aoc2015.day{args.day}'
    try:
        module = importlib.import_module(name)
        module.run(remainder)
    except ModuleNotFoundError:
        print(f'No module named {name} - have you created it?')


def main():  # pragma: no cover
    dispatch(sys.argv[1:])


if __name__ == "__main__":
    main()

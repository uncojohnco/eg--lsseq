#!/usr/bin/env python3

# https://pymotw.com/3/argparse/
# https://realpython.com/python-command-line-arguments/#a-few-methods-for-parsing-python-command-line-arguments

import os
import sys
import argparse
import logging
import pprint


import lss.lsseq

_pp = pprint.PrettyPrinter(indent=4)

_log = logging.getLogger(__name__)


def _get_version():
    """Resolve the version of this tool"""

    # https://stackoverflow.com/questions/458550/standard-way-to-embed-version-into-python-package
    from lss.__version__ import __version__
    return __version__


# Pycharm debug server
_HOST, _PORT = 'localhost', 40129
_version = _get_version()


def _init_argparser_debug():

    parser = argparse.ArgumentParser(add_help=False)

    group = parser.add_argument_group("debug")

    group.add_argument(
        "-v", "--verbose", dest="verbose", action="count", default=0,
        help="set logging level to 'debug'"
    )
    group.add_argument(
        "-d", "--debug", dest="debug", action="store_true", default=False,
        help="enable 'pycharm' debugger"
    )

    group.add_argument(
        "--host", dest="debugger_host", default=None,
        help="set 'host' for debug server", type=str
    )

    group.add_argument(
        "--port", dest="debugger_port", default=None,
        help="set 'port' for debug server", type=int
    )

    return parser


def init_argparse() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(
        prog='lss',
        parents=[_init_argparser_debug()],
        usage="lss [OPTION] [DIRECTORY]...",
        description="."
    )

    parser.add_argument(
        "--version", action="version",
        version=f"'lss' version {_version}"
    )

    parser.add_argument(
        'directory', default='', type=str, nargs="?",
        help='the directory to work on. Leave empty to work on the cwd'
    )

    return parser


def _setup_log_verbosity(verbosity: int):

    if verbosity >= 1:
        logging.basicConfig(level=logging.DEBUG)
        _log.debug("logging level set to DEBUG")


def _enable_debug(host: str, port: int):

    import pydevd_pycharm

    pydevd_pycharm.settrace(host=host, port=port, stdoutToServer=True, stderrToServer=True)
    _log.debug(f"pydevd enabled - host: '{host}', port: '{port}'")


def _run(dir_path: str):

    dir_path = os.path.abspath(dir_path)
    _log.info(dir_path)

    if not os.path.isdir(dir_path):
        raise RuntimeError(f"Defined directory arg is not valid!': '{dir_path}'")

    result = lss.lsseq.run(dir_path)
    print(result, file=sys.stdout)


def main(args: argparse.Namespace) -> None:

    if args.verbose:
        verbosity_level = args.verbose
        _setup_log_verbosity(verbosity_level)
    else:
        logging.basicConfig(level=logging.INFO)

    _log.debug("args: %s", _pp.pformat(args.__dict__))

    if args.debug:
        host = args.debugger_host or _HOST
        port = args.debugger_port or _PORT
        _enable_debug(host, port)

    dir_path = args.directory or os.getcwd()

    _run(dir_path)


if __name__ == '__main__':

    parser = init_argparse()
    args = parser.parse_args()

    sys.exit(main(args))

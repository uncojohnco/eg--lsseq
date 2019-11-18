#!/usr/bin/env python3

import os
import sys
import doctest

import lss.lsseq


def main():

    # TODO: implement optparse...

    if len(sys.argv) == 1:
        # Current dir if no arg is specified
        dir_path = '.'
    elif len(sys.argv) == 2:
        dir_path = sys.argv[0]
        # TODO: improve help...
        if '--help' in sys.argv[1]:
            print('Usage: lss /path/to/dir')
            return

        if '--test' in sys.argv[1]:
            print('TODO: Implement flag to run doctest strings...')
            return

        dir_path = os.path.abspath(dir_path)

        if os.path.isdir(dir_path):
            result = lss.lsseq.run(dir_path)
            print(result)
        else:
            print('Not a directory', dir_path)

sys.exit(main())

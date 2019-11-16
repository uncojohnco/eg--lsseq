#!/usr/bin/env python3

from collections import defaultdict
from typing import Any, List, Dict

import re
import os


import lss.util


class FileComposer:

    _file_paths: List[str]
    _file_groups: Dict[str, Any]

    def __init__(self, pattern):

        self._pattern = pattern

        self._file_groups = None

    def do_it(self) -> :

        if os.path.isdir(self._pattern):
            ret = next(os.walk(dirpath), None)
            files = ret[-1] if ret else []

        seqs = lss.util.yield_sequences_in_list(files)

        return seqs

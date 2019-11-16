#!/usr/bin/env python3

from collections import defaultdict
from typing import Any, List, Dict, Iterator, Pattern, Sequence, Union

import pathlib

import re
import os

from lss.dataclass import FileData, Fileobj, FileSequence

# Regular expression pattern for matching file names on disk.
FILE_GROUP_PATTERN = r"^(?P<basename>.*?)(?P<frames>\d+)?(?P<ext>\.\w*)*?$"
FILE_GROUP_RE = re.compile(FILE_GROUP_PATTERN)


# TODO: For now we do the work on the file name
#  and not the full path to keep the complexity minimal...
def get_file_group_key(filename, disk_re: Pattern = None) -> Dict:
    """
    >>> get_file_group_key('file01_0040.rgb')
    {'basename': 'file01_', 'frames': '0040', 'ext': '.rgb'}
    >>> get_file_group_key('file.info.03.rgb.txt')
    {'basename': 'file.info.03', 'frames': 'None, 'ext': '.txt'}

    """
    check = FILE_GROUP_RE.match or disk_re

    match = check(filename)
    groupdict = match.groupdict()

    return groupdict


class FileComposer:

    _file_paths: List

    def __init__(self, file_paths: Sequence):

        self._file_paths = file_paths

    def build_file_group_map(self):

        file_seq_map = defaultdict(set)

        for fp in self._file_paths:
            groups = get_file_group_key(fp)
            key = '{basename}-{ext}'.format(**groups)
            file_seq_map[key].add(fp)

        return file_seq_map

    def build_file_groups(self, file_seq_map: Dict) -> Iterator[Union[Fileobj,FileSequence]]:

        for key, file_paths in file_seq_map.items():

            fp = pathlib.Path(file_paths[0])

            dirname = fp.parent
            basename = fp.name
            ext = fp.suffix

            fd = FileData(dir=dirname, basename=basename, extension=ext)

            if file_paths > 1:
                yield Fileobj(file_data=fd)
            else:
                yield FileSequence(file_data=fd, file_paths=file_paths)

    def do_it(self) -> List[Union[Fileobj,FileSequence]]:

        file_seq_map = self.build_file_group_map()
        return list(self.build_file_groups(file_seq_map))

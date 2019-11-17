
# [PEP 563 -- Postponed Evaluation of Annotations](https://python.org/dev/peps/pep-0563/)
# https://stackoverflow.com/questions/33533148/how-do-i-specify-that-the-return-type-of-a-method-is-the-same-as-the-class-itsel
from __future__ import annotations

import os
import logging

from typing import List, Match, Tuple, Union
from dataclasses import dataclass

from lss.const import DIGITS_RE
import lss.util


log = logging.getLogger(__name__)


@dataclass
class SeqMatch:
    start: int
    end: int
    frames: Tuple


class Item:

    def __init__(self, item: str):

        self._item = item

        self._str_digits = DIGITS_RE.findall(self.name)
        self._str_parts = DIGITS_RE.split(self.name)

    def diff_sequence(self, item: Item) -> Union[SeqMatch,None]:

        if self.str_parts != item.str_parts:
            return None

        if len(self.str_digits) != len(item.str_digits):
            return None

        name1, name2 = self.name, item.name

        seqmatch = lss.util.diff_sequence(name1, name2)

        return seqmatch

    def is_sibling(self, item: Item) -> bool:

        diff_result = self.diff_sequence(item)
        if diff_result:
            return True

        return False

    @property
    def name(self) -> str:
        return self._item

    @property
    def str_parts(self) -> List[str]:
        return self._str_parts

    @property
    def str_digits(self) -> List[str]:
        return self._str_digits

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        n = self.name
        return f'<lss.Item "{n}">'


class FileItem(Item):

    def __init__(self, filepath: str):

        # assumed the path has already been expanded...
        self._path = filepath
        self._dirname, self._filename = os.path.split(self._path)

        super(FileItem, self).__init__(self._filename)

    def is_sibling(self, item: FileItem) -> bool:

        if self._dirname != item._dirname:
            return False

        return super(FileItem, self).is_sibling(item)

    @property
    def dirname(self) -> str:
        return self._dirname

    def __repr__(self):
        n = self.name
        return f'<lss.FileItem "{n}">'


# [PEP 563 -- Postponed Evaluation of Annotations](https://python.org/dev/peps/pep-0563/)
# https://stackoverflow.com/questions/33533148/how-do-i-specify-that-the-return-type-of-a-method-is-the-same-as-the-class-itsel
from __future__ import annotations

import os

from typing import List, Union

from lss.const import DIGITS_RE
import lss.util


class Item:

    def __init__(self, item):

        self._item = item
        self._path = os.path.abspath(str(item))

        self._dirname, self._filename = os.path.split(self._path)

        self._digits = DIGITS_RE.findall(self.name)
        self._parts = DIGITS_RE.split(self.name)

    def is_sibling(self, item: Union[str, Item]) -> bool:

        if not isinstance(item, Item):
            item = Item(item)

        if self._parts != item._parts:
            return False

        diff_result = lss.util.diff_sequence(self.name, item.name)
        is_sibling = len(diff_result) == 1

        return is_sibling

    @property
    def name(self) -> str:
        return self._filename

    @property
    def parts(self) -> List[str]:
        return self._parts

    @property
    def digits(self) -> List[int]:
        return self._digits

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        n = self.name
        return f'<lss.Item "{n}">'

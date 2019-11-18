

import os
import logging

from typing import List

from lss.const import DIGITS_RE

log = logging.getLogger(__name__)


class Item:
    """
    A primitive class for defining an abstract representation of an item.

    The purpose to be used  to find the substring representing
    a frame against another item.

    Examples:
        >>> item = Item('mario01_v003.rgb')
        >>> item.name
        'mario01_v003.rgb'
        >>> item.str_parts
        ['mario', '_v', '.rgb']
        >>> item.str_digits
        ['01', '003']
    """

    def __init__(self, item: str):

        self._item = item

        self._str_digits = DIGITS_RE.findall(item)
        self._str_parts = DIGITS_RE.split(item)

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
    """
    A primitive class for representing a file sequence on disk

    The purpose to be used  to find the substring representing
    a frame against another item.
    """

    def __init__(self, filepath: str):

        # assumed the path has already been expanded...
        self._path = filepath
        self._dirname, self._filename = os.path.split(self._path)

        super(FileItem, self).__init__(self._filename)

    @property
    def dirname(self) -> str:
        return self._dirname

    def __repr__(self):
        n = self.name
        return f'<lss.FileItem "{n}">'


import logging

from typing import List

import pathlib

from lss.const import DIGITS_RE


log = logging.getLogger(__name__)


Path = pathlib.PurePath


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

    dirname: str
    filename: str
    path: Path

    def __init__(self, filepath: str):

        # assumed the path has already been expanded...
        p_ = Path(str(filepath))
        self.dirname = str(p_.parent)

        self.filename = p_.name
        self.basename = p_.stem
        self.ext = p_.suffix

        self.path = p_

        super(FileItem, self).__init__(self.filename)

    def __repr__(self):
        n = self.name
        return f'<lss.FileItem "{n}">'



from typing import List, Tuple

from dataclasses import dataclass


@dataclass
class SequenceStrParts:
    """
    >>> s = SequenceStrParts('prefix_', '_suffix.ext',  4)
    >>> print(f'{s.prefix}{s.padding}{s.suffix}')
    prefix_####_suffix.ext

    >>> s = SequenceStrParts('file01_', '.rgb', 4)
    >>> print(f'{s.prefix}{s.padding}{s.suffix}')
    file01_####.rgb

    >>> s = SequenceStrParts('file', '_001.rgb', 2)
    >>> print(f'{s.prefix}{s.padding}{s.suffix}')
    file##_001.rgb

    """

    prefix: str
    suffix: str
    zfill: int

    char:  str = '#'

    @property
    def padding(self) -> str:
        return self.char * self.zfill



@dataclass
class Sequence:

    str_parts: SequenceStrParts
    frames: Tuple[int]


# class FileSequence:
#
#     _item: FileItem
#     _items: List[FileItem]
#
#     def __init__(self, fileitem: FileItem):
#
#         super(FileSequence, self).__init__(fileitem)
#
#         self._dirname = self._item.dirname

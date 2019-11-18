

from typing import List, Tuple

from dataclasses import dataclass

from lss.dataclass.base import Fileobj


@dataclass
class SequenceStrParts:
    """
    A data object for representing the str parts of interest of a
    string that represents a frame sequence.

    Examples:
        >>> s = SequenceStrParts('prefix_', '_suffix.ext',  4)
        >>> print(f'{s.prefix}{s.padding}{s.suffix}')
        prefix_####_suffix.ext

        >>> s = SequenceStrParts('file', '_001.rgb', 2)
        >>> print(f'{s.prefix}{s.printf}{s.suffix}')
        file%02d_001.rgb

        >>> s = SequenceStrParts('', '', 4)
        >>> s.padding
        '####'

        >>> s = SequenceStrParts('', '', 3)
        >>> s.printf
        '%03d'
        >>> s = SequenceStrParts('', '', 1)
        >>> s.printf
        '%d'
    """

    prefix: str
    suffix: str

    pad_len: int
    pad_char:  str = '#'

    @property
    def padding(self) -> str:
        """
        Creates a padding representation for the str "frame" part.
        """
        return self.pad_char * self.pad_len

    @property
    def printf(self) -> str:
        """
        Creates an printf style representation for the str "frame" part.
        """

        if self.pad_len < 2:
            return '%d'
        else:
            return f'%0{self.pad_len}d'


@dataclass
class Sequence:

    str_parts: SequenceStrParts
    frames: Tuple[int]


@dataclass
class FileSequence(Sequence):

    fileobj: Fileobj

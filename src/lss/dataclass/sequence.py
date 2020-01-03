

from typing import Tuple

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

    pad_len: int = 0
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


# TODO: Sequence behavior should be split into separate class, however, with dataclass inheritance,
#  would get `TypeError: non-default argument 'fileobj' follows default argument`
#  https://stackoverflow.com/questions/51575931/class-inheritance-in-python-3-7-dataclasses

# TODO: should be able to instantiate this class with a string...
@dataclass
class FileSequence:
    """
    TODO:

    Examples:
        >>> str_parts = SequenceStrParts('prefix_', '_suffix.ext',  4)
        >>> fo = Fileobj('root', '.ext')
        >>> s = FileSequence(str_parts, fo, frames=(1, 2, 3))
        >>> s.is_sequence
        True
        >>> s = FileSequence(str_parts, fo)
        >>> s.is_sequence
        False
    """

    str_parts: SequenceStrParts
    fileobj: Fileobj  # TODO: Replace this behavior with pathlib.PurePath?
    frames: Tuple[int, ...] = ()

    @property
    def is_sequence(self) -> bool:
        return len(self.frames) > 1

    # TODO: Add wrapper properties: prefix, suffix - str_parts.prefix etc

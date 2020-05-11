
import logging

from typing import List, Optional, Set, Union, Tuple

import lss.util

from lss import SubstrMatch, Item, FileItem, SequenceStrParts
from lss.dataclass.base import Fileobj
from lss.error import SequenceError


log = logging.getLogger(__name__)


LazyItem = Union[str, Item]


def find_matching_frame_substrings(
        item1: LazyItem, item2: LazyItem,
        strict=True) -> Optional[SubstrMatch]:
    """
    Diff between item1 and item2 to to resolve the frame representation
    of each item.

    Example:
        >>> find_matching_frame_substrings('file01_0040.rgb', 'file01_0041.rgb')
        SubstrMatch(pos=SubstrPos(start=7, end=11), groups=('0040', '0041'))

        >>> find_matching_frame_substrings('file1.03.rgb', 'file2.03.rgb')
        SubstrMatch(pos=SubstrPos(start=4, end=5), groups=('1', '2'))

        >>> find_matching_frame_substrings('file02_0040.rgb', 'file01_0041.rgb')

    :param item1: The string object for comparison against.
    :param item2: The string to compare to the object string.
    :param strict: If True, the length of the digit padding
                    must be the same when comparing

    :return: List of SeqMatch
    """

    if not isinstance(item1, Item):
        item1 = Item(item1)

    if not isinstance(item2, Item):
        item2 = Item(item2)

    if item1.str_parts != item2.str_parts:
        return None

    if len(item1.str_digits) != len(item2.str_digits):
        return None

    name1, name2 = item1.name, item2.name

    substr_match = lss.util.find_matching_frame_substrings(name1, name2, strict)
    return substr_match


class SequenceBuilder:
    """
    Class to handle the collection of sequential sequence of items.

    >>> s = SequenceBuilder(Item('file.0001.jpg'))
    >>> s.append(Item('file.0002.jpg'))
    >>> s.append(Item('file.0003.jpg'))
    >>> s.is_sequence
    True
    >>> s.frames
    {1, 2, 3}

    >>> s = SequenceBuilder(Item('mario01.0001.jpg'))
    >>> s.is_sequence
    False
    >>> len(s.frames)
    0
    """

    def __init__(self, item: Item):

        self._base: Item = item
        self._items: List[Item] = [item]

        self._seq_str_parts: SequenceStrParts = None
        self._frames: Set[int] = set()
        self._is_sequence: bool = False

    def can_include(self, item: Item) -> bool:
        """
        Validate if the supplied item can be a part of this sequence.

        :param item: The item to compare against the base item
        """

        substr_match = find_matching_frame_substrings(self._base, item)
        if not substr_match:
            return False

        # Dont include if the matched frame of the other item
        # already exists in this sequence frame set.
        frame = substr_match.groups[1]

        if frame in self._frames:
            return False

        return True

    def _init_sequence(self, substr_match: SubstrMatch):
        """
        Method to initialise this as a true sequence.
        """

        basename = self._base.name
        base_frame = substr_match.groups[0]

        frame_pos = substr_match.pos
        pos1, pos2 = frame_pos.start, frame_pos.end

        # This is used later for creating a Concrete Sequence
        seq_str_parts = SequenceStrParts(
            prefix=basename[:pos1],
            suffix=basename[pos2:],
            pad_len=len(base_frame)
        )

        self._frames.add(int(base_frame))

        self._seq_str_parts = seq_str_parts
        self._is_sequence = True

    def append(self, item: Item):

        substr_match = find_matching_frame_substrings(self._base, item)
        log.debug(f'{item} - {substr_match}')

        if not substr_match:
            raise SequenceError('\n'.join(
                'Item dosent belong to this sequence!'
                'Sequence.base: {self._base}'
                'Item: {item}'
            ))

        # The first append will toggle the state that this is a Sequence,
        # i.e it has more than one item
        if not self._is_sequence:
            self._init_sequence(substr_match)

        self._frames.add(int(substr_match.groups[1]))
        self._items.append(item)

    def __str__(self):
        return self._base.str_parts

    @property
    def items(self) -> List[Item]:
        """
        The items used in the creation of this sequence.
        """
        return self._items

    @property
    def frames(self) -> Set[int]:
        """
        The frames contained in this sequence.
        This is on ordered set for fast lookup
        """
        return self._frames

    @property
    def ordered(self) -> Tuple[int]:
        """
        The order representaion of frames
        """
        return tuple(sorted(self.frames))

    @property
    def seq_str_parts(self) -> SequenceStrParts:
        """
        # TODO:
        """

        return self._seq_str_parts

    @property
    def is_sequence(self) -> bool:
        """
        # TODO:
        """

        return self._is_sequence


class FileSequenceBuilder(SequenceBuilder):

    _fileobj: Fileobj
    _base: FileItem

    def __init__(self, fileitem: FileItem):

        super(FileSequenceBuilder, self).__init__(fileitem)

        # TODO: Replace this behavior with pathlib.PurePath?
        self._fileobj = Fileobj(
            dirname=self._base.dirname,
            ext=self._base.ext
        )

    # TODO: Implement PurePath but with the generic sequence filename
    #  i.e file01_####.rgb
    # def _init_sequence(self, substr_match: SubstrMatch):
    #
    #     super(FileSequenceBuilder, self)._init_sequence(substr_match)
    #
    #     self._fileobj = Fileobj(
    #         dirname=self._base.dirname,
    #         ext=self._base.ext
    #     )

    @property
    def fileobj(self) -> Fileobj:
        """
        # TODO:
        :return:
        """

        return self._fileobj

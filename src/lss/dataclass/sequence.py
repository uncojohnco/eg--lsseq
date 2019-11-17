
import logging

from typing import List, Set

from lss.dataclass.item import Item, FileItem


log = logging.getLogger(__name__)


class SequenceCollector:

    _item_pri: Item
    _items: List[Item]
    _frames: Set[int]
    _pad: int

    # For now we initialise a Sequence from a single item and
    # append more items using the append method...
    def __init__(self, item: Item):

        self._item_pri = item
        self._items = [item]

        self._frames = set() # TODO: change to frozenset

    def can_include(self, item: Item) -> bool:

        diff_result = self._item_pri.diff_sequence(item)
        if not diff_result:
            return False

        frame = diff_result.frames[1]

        # Dont include if the matched frame of the other item
        # already exists in this sequence frame set.
        if frame in self._frames:
            return False

        return True

    def append(self, item: Item):

        self._items.append(item)

        d = self._item_pri.diff_sequence(item)
        log.debug(f'{item} - {d}')

        if not self._frames:
            self._frames.add(d.frames[0])

        self._frames.add(d.frames[1])

    # def __str__(self):
    #     pass

    @property
    def items(self):
        return self._items


class FileSequence:

    _item: FileItem
    _items: List[FileItem]

    def __init__(self, fileitem: FileItem):

        super(FileSequence, self).__init__(fileitem)

        self._dirname = self._item.dirname

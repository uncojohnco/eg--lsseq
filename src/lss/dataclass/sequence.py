
from typing import List

from lss.dataclass.item import Item
import lss.util


def sibling_frames(item1: Item, item2: Item):

    if item1.parts != item2.parts:
        return []

    diff_result = lss.util.diff_sequence(item1.name, item2.name)

    return diff_result


class Sequence:

    def __init__(self, item: Item):

        self._items = []
        self._items.append(item)

        self._parts = item.parts

    def includes(self, item: Item):
        return self._items[-1].is_sibling(item)

    @property
    def parts(self) -> List[str]:
        return self._parts
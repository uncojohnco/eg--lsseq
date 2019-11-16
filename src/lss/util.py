import logging
from typing import List

from lss.const import DIGITS_RE


log = logging.getLogger(__name__)


def diff_sequence(name1: str, name2: str, strict=True) -> List:

    log.debug(f'diff: "{name1} {name2}')

    matches1 = [m for m in DIGITS_RE.finditer(name1)]
    matches2 = [m for m in DIGITS_RE.finditer(name2)]

    # Bail early as the two items are different
    if not len(matches1) == len(matches2):
        return []

    # The diff result
    diff_result = []

    # Iterate through each items digit match.
    for match1, match2 in zip(matches1, matches2):

        start1, start = match1.start(), match2.start()
        group1, group2 = match1.group(), match2.group()

        # The items cannot be the same if...

        # If the matches don't have the same start position
        if start1 != start:
            continue

        # If the match groups are equal, i.e if we are matching the 1st digit match found in
        # "file01_0040.rgb" and "file01_0041.rgb", we should ignore these as this digit match
        # represent a part of the name and not a frame!
        if group1 == group2:
            continue

        # If strict is True, The length of the padding must be the same!
        if strict is True and len(group1) != len(group2):
            continue

        data = {
            'start': start1,
            'end': match1.end(),
            'frames': (group1, group2)
        }
        diff_result.append(data)

    return diff_result

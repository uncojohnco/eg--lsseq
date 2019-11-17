import logging

from typing import Tuple, Union
from dataclasses import dataclass

from lss.const import DIGITS_RE


log = logging.getLogger(__name__)


@dataclass
class SeqMatch:
    start: int
    end: int
    frames: Tuple


def diff_sequence(str1: str, str2: str, strict=True) -> Union[SeqMatch,None]:
    """Diff between str1 and str2 to to resolve the frame representation
    of each string.

    Example:
        >>> diff_sequence('file01_0040.rgb', 'file01_0041.rgb')
        SeqMatch(start=7, end=11, frames=('0040', '0041'))

        >>> diff_sequence('file1.03.rgb', 'file2.03.rgb')
        SeqMatch(start=4, end=5, frames=('1', '2'))

        >>> diff_sequence('file02_0040.rgb', 'file01_0041.rgb')


    :param str1: The string object for comparison against.
    :param str2: The string to compare to the object string.
    :param strict: If True, the length of the digit padding
                    must be the same when comparing

    :return: List of SeqMatch

    """

    log.debug(f'diff: "{str1} {str2}')

    matches1 = list(DIGITS_RE.finditer(str1))
    matches2 = list(DIGITS_RE.finditer(str2))

    if len(matches1) != len(matches2):
        return None

    diff_result = []

    # Iterate through ordered pairs of digits found in each name
    for m1, m2 in zip(matches1, matches2):

        digit_str1, digit_str2 = m1.group(), m2.group()
        start1, start2 = m1.start(), m2.start()

        # Skip if the pair of matching "digit strings" are equal,
        # hence this pair cant be representative of frame sequence
        if digit_str1 == digit_str2:
            continue

        # Ignore if the matches don't have the same start position
        if start1 != start2:
            continue

        # If strict is True, the length of the padding must be the same!
        if strict is True and len(digit_str1) != len(digit_str2):
            continue

        # If we get to this point - we have found a digit string part
        # representing a sequence
        seq_match = SeqMatch(
            start=m1.start(), end=m1.end(),
            frames=(digit_str1, digit_str2)
        )
        diff_result.append(seq_match)

    # if more than one set of matches has been found
    if not diff_result or len(diff_result) > 1:
        return None

    log.debug(r'diff_result: {diff_result}')

    return diff_result[0]

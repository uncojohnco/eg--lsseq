import logging

from typing import Optional, Sequence

from lss.const import DIGITS_RE
from lss.dataclass.base import SubstrMatch, SubstrPos

log = logging.getLogger(__name__)


def find_matching_frame_substrings(
        str1: str, str2: str,
        strict=True) -> Optional[SubstrMatch]:
    """
    Diff between str1 and str2 to to resolve the frame representation
    of each string.

    Examples:
        >>> find_matching_frame_substrings('file01_0040.rgb', 'file01_0041.rgb')
        SubstrMatch(pos=SubstrPos(start=7, end=11), groups=('0040', '0041'))

        >>> find_matching_frame_substrings('file1.03.rgb', 'file2.03.rgb')
        SubstrMatch(pos=SubstrPos(start=4, end=5), groups=('1', '2'))

        >>> find_matching_frame_substrings('file02_0040.rgb', 'file01_0041.rgb')

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

    diff_results = []

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
        seq_match = SubstrMatch(
            pos=SubstrPos(m1.start(), m1.end()),
            groups=(digit_str1, digit_str2)
        )
        diff_results.append(seq_match)

    log.debug(r'diff_results: {diff_results}')

    # If more than one substring match is found, we consider this result to be 
    # invalid for our purposes of finding the substring representing 
    # a frame sequence
    if not diff_results or len(diff_results) > 1:
        return None

    substr_match = diff_results[0]

    return substr_match


# Stolen from https://github.com/mohsen3/lss
# TODO: replace with own implementation!
def compact_frame_range(frames: Sequence[int]):
    """Converts a list of numbers into the compact representation of the numbers.
    >>> compact_frame_range([1, 2, 3, 4])
    '1-4'
    >>> compact_frame_range([1, 2, 5, 3])
    '1-3 5'
    >>> compact_frame_range([1, 2, 5, 7, 8, 9])
    '1-2 5 7-9'
    """

    nums = sorted(frames)

    formatted = []
    i = 0
    while i < len(frames):
        count = 0
        while i + count < len(nums) and nums[i] + count == nums[i + count]:
            count = count + 1
        formatted.append(str(nums[i]) + ('' if count == 1 else '-' + str(nums[i] + count - 1)))
        i = i + count

    return ' '.join(formatted)

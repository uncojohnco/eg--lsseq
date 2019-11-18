import pathlib

from typing import Generator, Iterator, List

from lss.dataclass.item import FileItem
from lss.dataclass.sequence import Sequence
from lss.builder import SequenceBuilder


def build_sequences_form1(file_items: Iterator[FileItem]) -> List[SequenceBuilder]:
    """
    Process a list of files into

    :param file_items: file items to be processed.
    :return:
    """

    sequences_f1 = []

    for file in file_items:

        item = FileItem(file)

        found = False

        for seq in sequences_f1:
            if seq.can_include(item):
                seq.append(item)

                found = True
                break

        if not found:
            seq = SequenceBuilder(item)
            sequences_f1.append(seq)

    return sequences_f1


def get_sequences(filenames: List[str]):
    """
    Process a list of filenames to be collected into their

    Examples:
        >>> files = ['f01.rgb', 'f02.rgb','f03.rgb',]
        >>> get_sequences(files)

    :param filenames:
    :return:
    """

    file_items = map(FileItem, filenames)

    sequences_f1 = build_sequences_form1(file_items)

    sequences = []
    for seq_f1 in sequences_f1:

        ordered_frames = sorted(seq_f1.frames)

        seq = Sequence(
            str_parts=seq_f1.seq_str_parts,
            frames=tuple(ordered_frames)
        )

        sequences.append(seq)

    return sequences


def run(dir_path):

    """
    >>> run('./test-jc--dd-2019/tests/files/simple1')

    :param dir_path:
    :return:
    """

    path = pathlib.Path(dir_path)

    filenames = path.iterdir()

    get_sequences(filenames)

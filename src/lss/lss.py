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
            seq = self._builder(item)
            sequences_f1.append(seq)

    return sequences_f1


def build_seq(built_seq: SequenceBuilder) -> Sequence:
    """
    From a processed "1st form sequence", generate a concrete Sequence object.

    :param built_seq: The conceptual representation of a sequence of frames.
    """

    ordered_frames = sorted(built_seq.frames)

    seq = Sequence(
        str_parts=built_seq.seq_str_parts,
        frames=tuple(ordered_frames)
    )

    return seq


def build_sequences(built_sequences: Iterator[SequenceBuilder]) -> Generator[Sequence, None, None]:

    for b_seq in built_sequences:
        yield build_seq(b_seq)


def get_sequences(filenames: List[str]):
    """
    Process a list of filenames to be collected into their

    Examples:
        >>> files = ['f01.rgb', 'f02.rgb','f03.rgb',]
        >>> d = Director()
        >>> d.build(files)

    :param filenames:
    :return:
    """

    file_items = map(FileItem, filenames)

    sequences_f1 = build_sequences_form1(file_items)
    sequences = build_sequences(sequences_f1)

    return sequences


def run(dir_path):

    """
    G

    :param dir_path:
    :return:
    """

    path = pathlib.Path(dir_path)

    filenames = path.iterdir()

    get_sequences(filenames)

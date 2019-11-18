import os
import pathlib

from typing import Iterator, List, Iterable, Generator

from lss import FileItem, FileSequence
from lss.builder import FileSequenceBuilder


def build_sequences_form1(file_items: Iterator[FileItem]) -> List[FileSequenceBuilder]:
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
            seq = FileSequenceBuilder(item)
            sequences_f1.append(seq)

    return sequences_f1


def build_sequences_concrete(sequences_f1: Iterable[FileSequenceBuilder]) -> Generator[FileSequenceBuilder, None, None]:

    for seq_f1 in sequences_f1:

        seq = FileSequence(
            str_parts=seq_f1.seq_str_parts,
            frames=seq_f1.ordered,
            fileobj=seq_f1.fileobj,
        )

        yield seq


def get_sequences(file_paths: Iterable[str]) -> Generator[FileSequence, None, None]:
    """
    Process a list of filenames to be collected into their

    Examples:
        >>> files = ['f01.rgb', 'f02.rgb','f03.rgb',]
        >>> list(get_sequences(files))
        [FileSequence(str_parts=SequenceStrParts(prefix='f', suffix='.rgb', pad_len=2, pad_char='#'), fileobj=Fileobj(dirname='.', ext='.rgb'), frames=(1, 2, 3))]

    :param file_paths:
    :return:
    """

    file_items = map(FileItem, file_paths)
    sequences_f1 = build_sequences_form1(file_items)
    yield from build_sequences_concrete(sequences_f1)


# TODO: add commandline formatter
def format_sequence(seq: FileSequence) -> str:
    """
    Examples:
        >>> from lss import SequenceStrParts
        >>> from lss.dataclass.base import Fileobj

        >>> fo = Fileobj('root', '.ext')

        >>> str_parts = SequenceStrParts('mario01_', '.ext',  4)
        >>> mario = FileSequence(str_parts, Fileobj('root', '.ext'), frames=(1, 2, 3))
        >>> format_sequence(mario)
        '3 mario01_%04d.ext 1-3'

        >>> str_parts = SequenceStrParts('peach01', '.ext')
        >>> peach = FileSequence(str_parts, fo)
        >>> format_sequence(peach)
        '1 peach01.ext'

    :param seq:
    :return:
    """
    s = seq.str_parts

    if seq.is_sequence:
        count = len(seq.frames)
        bn = f'{s.prefix}{s.printf}{s.suffix}'

        # TODO: implement compact frame format
        comp_frames = seq.frames

        return f'{count} {bn} {comp_frames}'

    # This is a single file, i.e it dosent represent a sequence of files
    else:
        bn = seq.str_parts.prefix
        return f'1 {bn}{s.suffix}'


def run(dir_path):

    """
    Examples:
        >>> run('../../tests/files/simple1')
        5 file01_%04d.rgb 40-42, 44, 45
        >>> run('../../tests/files/ex1')
        1 elem.info
        46 sd_fx29.%04d.rgb 101-121 123-147
        1 strange.xml

    :param dir_path:
    :return:
    """

    dir_path = os.path.abspath(dir_path)

    path = pathlib.Path(dir_path)

    filenames = map(str, path.iterdir())

    sequences = get_sequences(filenames)

    for seq in sequences:

        output = format_sequence(seq)
        print(output)

import os
import pathlib

import logging

from typing import Generator, Iterable, List, Sequence, Union

import lss.util
from lss import FileItem, FileSequence, SequenceStrParts
from lss.builder import FileSequenceBuilder


log = logging.getLogger(__name__)

LazyFileItems = Union[Sequence[str], Sequence[FileItem]]


def build_sequences_form1(file_paths:  Iterable[str]) -> List[FileSequenceBuilder]:
    """
    Process a list of files into

    :param file_paths: file items to be processed.
    :return:
    """

    sequences_f1 = []

    file_paths = sorted(file_paths)

    for file in file_paths:

        if not isinstance(file, FileItem):
            file = FileItem(file)

        found = False

        for seq in sequences_f1:
            if seq.can_include(file):
                seq.append(file)

                found = True
                break

        if not found:
            seq = FileSequenceBuilder(file)
            sequences_f1.append(seq)

    return sequences_f1


def build_sequences_concrete(sequences_f1: Iterable[FileSequenceBuilder]) -> Generator[FileSequenceBuilder, None, None]:

    for seq_f1 in sequences_f1:

        if seq_f1.is_sequence:

            seq = FileSequence(
                str_parts=seq_f1.seq_str_parts,
                fileobj=seq_f1.fileobj,
                frames=seq_f1.ordered,
            )
        # This item is not part of a sequence
        else:
            # TODO: Refactor this so that we arent reliant on SequenceStrParts for a single file!
            seq_str_parts = SequenceStrParts(seq_f1._base.basename, seq_f1._base.ext)
            seq = FileSequence(
                str_parts=seq_str_parts,
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

    sequences_f1 = build_sequences_form1(file_paths)
    return list(build_sequences_concrete(sequences_f1))  # TODO:


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
        comp_frames = lss.util.compact_frame_range(seq.frames)

        return f'{count} {bn} {comp_frames}'

    # This is a single file, i.e it dosent represent a sequence of files
    else:
        bn = seq.str_parts.prefix
        return f'1 {bn}{s.suffix}'


def run(dir_path):

    """
    Examples:
        >>> import os
        >>> olddir = os.getcwd()
        >>> targetdir = os.path.dirname(__file__)
        >>> os.chdir(targetdir)

        >>> print(run('../../tests/files/simple1'))
        5 file01_%04d.rgb 40-42 44-45

        >>> print(run('../../tests/files/ex1'))
        1 elem.info
        46 sd_fx29.%04d.rgb 101-121 123-147
        1 strange.xml

        # TODO: this test is failing...
        >>> print(run('../../tests/files/broken_seq'))
        5 file01_%04d.rgb 40-42 44-45
        5 file02_%d.rgb 0-4
        4 file%d.03.rgb 1-4

       >>> os.chdir(olddir)

    :param dir_path:
    :return:
    """

    dir_path = os.path.abspath(dir_path)
    log.debug(f'dir path: "{dir_path}"')

    path = pathlib.Path(dir_path)

    filenames = map(str, path.iterdir())

    sequences = list(get_sequences(filenames))

    log.debug(f'Sequences resolved: "{sequences}"')

    lines = []

    for seq in sequences:
        output = format_sequence(seq)
        lines.append(output)

    return '\n'.join(lines)

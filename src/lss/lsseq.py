import os
import pathlib

from typing import Iterator, List, Iterable

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


def get_sequences(file_paths: Iterable[str]) -> List[FileSequence]:
    """
    Process a list of filenames to be collected into their

    Examples:
        >>> files = ['f01.rgb', 'f02.rgb','f03.rgb',]
        >>> get_sequences(files)
        [FileSequence(str_parts=SequenceStrParts(prefix='f', suffix='.rgb', pad_len=2, pad_char='#'), frames=(1, 2, 3), fileobj=Fileobj(dirname='.', ext='.rgb'))]

    :param file_paths:
    :return:
    """

    file_items = map(FileItem, file_paths)

    sequences_f1 = build_sequences_form1(file_items)

    sequences = []
    for seq_f1 in sequences_f1:

        ordered_frames = sorted(seq_f1.frames)

        # TODO:
        # if not seq_f1.is_sequence:
        #   Handle single File ...

        seq = FileSequence(
            str_parts=seq_f1.seq_str_parts,
            frames=tuple(ordered_frames),
            fileobj=seq_f1.fileobj
        )

        sequences.append(seq)

    return sequences


# TODO: add commandline formatter
def format_sequence(seq: FileSequence) -> str:

    # TODO: Handle a sequence that is a single file!

    count = len(seq.frames)
    s = seq.str_parts
    bn = f'{s.prefix}{s.printf}{s.suffix}'

    # TODO: implement compact frame format
    comp_frames = seq.frames

    return f'{count} {bn} {comp_frames}'


def run(dir_path):

    """
    Examples:
        >>> run('../../tests/files/simple1')
        5 file01_%04d.rgb 40-42, 44, 45

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

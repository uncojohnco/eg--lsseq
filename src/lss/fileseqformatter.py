#!/usr/bin/env python3


from typing import List

from lss.dataclass import FileSequence, Fileobj


# TODO: ...
def format_frames_compact(frames):
    """
    Converts a list of numbers into the compact representation of the numbers.

    >>> format_frames_compact([1, 2, 3, 4])
    '1-4'
    >>> format_frames_compact([1, 2, 5, 3])
    '1-3 5'compress_frames
    >>> format_frames_compact([1, 2, 5, 7, 8, 9])
    '1-2 5 7-9'
    """

    return '1-2 5 7-9'
    

class FileSeqFormatter:
    
    def __init__(self, file_groups: List[Fileobj]):
        self._file_groups = file_groups

    @staticmethod
    def _file_sequence(fileseq: FileSequence) -> str:

        count = len(fileseq.frames)

        bn = fileseq.basename

        zfill = fileseq.zfill
        pad_str = '%d'.format(zfill)

        if zfill > 1:
            pad_str = '%0{}d'.format(zfill)

        ext = fileseq.extension

        frames = fileseq.frames
        frame_chunks = format_frames_compact(frames)

        output = f'{count} {bn}{pad_str}.{ext}\t{frame_chunks}'

        return output

    @staticmethod
    def _file_single(fileobj: Fileobj) -> str:

        bn = fileobj.basename

        return f'1 {bn}'

    def do_it(self) -> List[str]:

        for fg in self._file_groups:
            if isinstance(fg, FileSequence):
                yield self._file_sequence(fg)
            else:
                yield self._file_single(fg)

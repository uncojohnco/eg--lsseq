

#!/usr/bin/env python3

from typing import List

from lss.dataclass import FileSequence, Fileobj



def compress_frames():
    pass
    

class FileSeqFormatter:
    
    def __init__(self, file_groups: List[Fileobj]):
        self._file_groups = file_groups

    def _file_sequence(self, fileobj: FileSequence):

        count = len(fileobj.frames)

        bn = fileobj.basename

        zfill = fileobj.zfill
        pad_str = '%d'.format(zfill)

        if zfill > 1:
            pad_str = '%0{}d'.format(zfill)

        ext = fileobj.extension

        frame_chunks = 

        output = f'{count} {bn}{pad_str}.{ext}\t{frame_chunks}'


    def _file_single(self, fileobj: Fileobj):
        pass

    def _process(self, file_group: Fileobj):

        if len(file_group):
            yield self._file_sequence(fg)
        else:
            yield self._file_single(fg)

    def do_it(self) -> str:

        for fg in self._file_groups:
            yield self._process(fg)

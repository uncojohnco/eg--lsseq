
from typing import Any, FrozenSet, List, Dict

import os
import pathlib
import re


from dataclasses import dataclass


@dataclass
class FileData:

    dir: str
    basename: str
    extension: str


class Fileobj:

    _filedata: FileData

    def __init__(self, file_data: FileData):

        self._filedata = _fd = file_data

        self._file_path = os.path.join(_fd.dir, _fd.basename)

    @property
    def file_path(self) -> str:
        return self._file_path
    
    @property
    def dir(self) -> str:
        return self._filedata.dir

    @property
    def basename(self) -> str:
        return self._filedata.basename

    @property
    def extension(self) -> str:
        return self._filedata.extension

    def __len__(self) -> int:
        """
        The length (number of files) represented by this :class:`FileSequence`.
        """

        return 1


class FileSequence(Fileobj):
    """
    :class: `FileSequence` represents an ordered sequence of files.
    """

    _file_paths: List[str]
    _frames: FrozenSet
    _zfill: int

    def __init__(self, file_data: FileData, file_paths):

        super(FileSequence, self).__init__(file_data)

        self._file_paths = file_paths

        # Sequence behavior

        self._frames = None
        self._zfill = None

        self._setup_frames()

    # TODO: ...
    def _setup_frames(self):
        pass

    @property
    def frames(self) -> frozenset[int]:
        return self._frames
    
    @property
    def zfill(self) -> int:
        return self._zfill

    @property
    def file_paths(self) -> List[str]:
        return self._file_paths

    def __len__(self) -> int:
        """
        The length (number of files) represented by this :class:`FileSequence`.
        """
        
        if not self._frames or not self._zfill:
            return 1

        return len(self._frames)

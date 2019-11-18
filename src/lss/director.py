
from typing import List

from lss.dataclass.item import FileItem
from lss.sequence import SequenceBuilder


class Director:

    _builder = SequenceBuilder

    def build_sequences_form1(self, files: List[FileItem]):

        sequences_f1 = []

        for file in files:

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

    def build_sequence(self, sequences: List[SequenceBuilder]):



    def build(self, files: List[FileItem]):

        sequences_f1 = self.build_sequences_form1(files)
        sequences = self.build_sequence(sequences_f1)

        return

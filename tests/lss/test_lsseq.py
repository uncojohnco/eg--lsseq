from dataclasses import dataclass
import pprint
from typing import Sequence
import yaml

import pytest

from lss import lsseq

TEST_DATA_YAML = 'data__get_sequences.yaml'

_pf = pprint.PrettyPrinter(indent=4).pformat

# lightweight class to validate the input data from the yaml are expected data types
@dataclass
class CaseData:
    id: str
    files: Sequence[str]
    expected_outputs: Sequence[dict]


def _generate_test_data():

    from pathlib import Path
    path = Path(__file__).parent / TEST_DATA_YAML

    with path.open() as f:
        test_data = yaml.safe_load(f)

    for case_data in test_data:
        case = CaseData(**case_data)
        yield pytest.param(case.files, case.expected_outputs, id=case.id)


testdata = list(_generate_test_data())


@pytest.mark.parametrize("files,expected_outputs", testdata)
def test__get_sequences(files, expected_outputs):

    # Act
    sequences = list(lsseq.get_sequences(files))

    # Assert
    assert len(sequences) == len(expected_outputs), f'sequences: {sequences}'

    for seq, expected in zip(sequences, expected_outputs):
        for attr, value in expected.items():
            assert str(getattr(seq, attr)) == value, f'sequences: {_pf(sequences)}'

import pytest

from lss import lss_cli

# https://mypy.readthedocs.io/en/stable/common_issues.html#import-cycles
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import argparse



@pytest.fixture
def setup_args(mocker):
    """
    Convenient fixture for `lss_cli` module to:
        - setup args
        - mock `_run` behaviour
    """

    # https://alysivji.github.io/pytest-fixures-with-function-arguments.html
    def _setup_args(args: list) -> 'argparse.Namespace':

        mocker.patch('lss.lss_cli._run', name='lss_cli._run')

        parser = lss_cli.init_argparse()
        args = parser.parse_args(args)

        return args

    return _setup_args

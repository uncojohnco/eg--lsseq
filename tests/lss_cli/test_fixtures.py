
import pytest

from lss import lss_cli


# https://stackoverflow.com/questions/59379412/pytest-mark-a-test-as-a-must-pass-and-stop-testing-if-it-fails
@pytest.mark.must_pass
def test__patched_main(mocker, setup_args):

    _dir_path = 'dummy_path'

    # Arrange
    args = setup_args([_dir_path])

    spy_run = mocker.spy(lss_cli, '_run')

    # Act
    lss_cli.main(args)

    # Assert
    assert args.directory == _dir_path
    spy_run.assert_called_with(_dir_path)

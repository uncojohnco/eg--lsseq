
import logging

from unittest import mock
import pytest


from lss import lss_cli


def test__verbose__lvl1(setup_args, caplog):

    args = setup_args(['-v'])

    with caplog.at_level(logging.DEBUG):
        lss_cli.main(args)
        assert 'logging level set to DEBUG' in caplog.text


def test__verbose__lvl2(setup_args, caplog):

    args = setup_args(['-vv'])

    with caplog.at_level(logging.DEBUG):
        lss_cli.main(args)
        assert 'logging level set to DEBUG' in caplog.text


def test__debugger__enable__pycharm(mocker, setup_args):

    settrace = mocker.patch('pydevd_pycharm.settrace')

    args = setup_args(['-d'])

    lss_cli.main(args)

    assert settrace.called


def test__get_version(capsys):

    _ver = lss_cli._version

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        parser = lss_cli.init_argparse()
        parser.parse_args(['--version'])

    out, err = capsys.readouterr()

    assert _ver in out

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

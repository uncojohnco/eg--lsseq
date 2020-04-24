import pytest
from pytest_reorder import make_reordering_hook


from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from _pytest.nodes import Item
    from _pytest.runner import CallInfo


# https://github.com/not-raspberry/pytest_reorder
pytest_collection_modifyitems = make_reordering_hook([
    r'(^|.*/)test_fixtures',
    None,
])


# https://stackoverflow.com/questions/59379412/pytest-mark-a-test-as-a-must-pass-and-stop-testing-if-it-fails
# https://docs.pytest.org/en/latest/example/simple.html#incremental-testing-test-steps
# TODO: This behaviour seems to work only on sibling tests of the
#       test marked as `must_pass` that are in the same module.
#       The desired behaviour is that if a test marked `must_pass` fails,
#       This should skip test execution of any other tests in the session.
def pytest_runtest_makereport(item: 'Item', call: 'CallInfo'):

    if 'must_pass' in item.keywords and call.excinfo is not None:
        parent = item.parent
        parent._mpfailed = item


def pytest_runtest_setup(item: 'Item'):

    must_pass_failed = getattr(item.parent, '_mpfailed', None)  # type: Item
    if must_pass_failed is not None:
        pytest.skip('must pass test failed (%s)' % must_pass_failed.name)

import pytest


def test_subtraction():
    assert 4 - 4 == 0


@pytest.mark.smoke
def test_addition():
    assert 4 + 4 == 8


@pytest.mark.smoke
def test_multiplication():
    assert 4 * 4 == 16

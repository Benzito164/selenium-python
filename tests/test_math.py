import pytest


def test_addition():
    assert 1+1 == 2


def test_subtraction():
    assert 0-10 == -10


@pytest.mark.parametrize(
    "a,b,expected",
    [(0, 5, 0), (1, 5, 5), (2, 5, 10), (-3, 5, -15), (-4, -5, 20)])
def test_multiply(a, b, expected):
    assert a*b == expected


def test_divide_by_zero_assertion():
    with pytest.raises(ZeroDivisionError):
        12 / 0

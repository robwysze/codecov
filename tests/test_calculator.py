import pytest

from codecov.calculator import Calculator


def test_addition():
    f_number = 2
    s_number = 2
    expected = 4
    assert Calculator.addition(f_number, s_number) == expected

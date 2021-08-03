import pytest

from codecov.calculator import Calculator


def test_addition():
    f_number = 2
    s_number = 2
    expected = 4
    assert Calculator.addition(f_number, s_number) == expected


def test_subtraction():
    f_number = 5
    s_number = 2
    expected = 3
    assert Calculator.subtraction(f_number, s_number) == expected


def test_multiplication():
    f_number = 6
    s_number = 5
    expected = 30
    assert Calculator.multiplication(f_number, s_number) == expected

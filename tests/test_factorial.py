"""
Unit tests for the factorial function
"""


import pytest
from template_python_project import factorial


def test_negative_number():
    """
    error - negative number
    """
    with pytest.raises(factorial.FactorialError) as error:
        factorial.factorial(-1)
    assert str(error.value) == "[-1] is not a positive number"


def test_not_a_number_abc():
    """
    error - "abc" string
    """
    with pytest.raises(factorial.FactorialError):
        factorial.factorial("abc")


def test_not_a_number_list():
    """
    error - a list
    """
    with pytest.raises(factorial.FactorialError):
        factorial.factorial([1])


def test_not_a_number_none():
    """
    error - None
    """
    with pytest.raises(factorial.FactorialError):
        factorial.factorial(None)


def test_not_an_int():
    """
    error - float
    """
    with pytest.raises(factorial.FactorialError):
        factorial.factorial(1.2)


def test_valid_factorial():
    """
    valid - some valid factorial results to check the implementation
    """
    assert factorial.factorial(0) == 1
    assert factorial.factorial(1) == 1
    assert factorial.factorial(2) == 2
    assert factorial.factorial(3) == 6
    assert factorial.factorial(10) == 3628800

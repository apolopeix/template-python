"""
Factorial example module
"""


def factorial(num):
    """
    Simple implementation of factorial
    :param num: positive integer number
    :return: result of applying factorial to n
    """
    try:
        if num < 0:
            raise FactorialError("[{}] is not a positive number".format(num))

        if num == 0 or num == 1:
            return 1

        return num * factorial(num - 1)

    except TypeError:
        raise FactorialError("[{}] is not a valid parameter".format(num))


class FactorialError(Exception):
    """
    Exception for the factorial module
    """
    pass

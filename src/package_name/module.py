"""
A module to help demonstrate software testing.
"""


def is_even(number: int) -> bool:
    """
    Determines if a number is even.

    An even number is divisible by 2 without a remainder.

    Args:
        number (int):
            The number to check.

    Returns:
        bool:
            True if the number is even, False if it is odd.

    Examples:
        >>> is_even(2)
        True
        >>> is_even(3)
        False
    """
    return number % 2 == 0

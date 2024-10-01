"""
Run a test using Hypothesis property-based testing.
"""

from hypothesis import given
from hypothesis.strategies import integers
from package_name.module import is_even


@given(integers())
def test_is_even(number):
    # add a print statement to observe Hypothesis test integers
    print(f"Testing whether {number} is an even number with Hypothesis.")
    if number % 2 == 0:
        assert is_even(number)
    else:
        assert not is_even(number)

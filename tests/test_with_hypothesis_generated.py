# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

import package_name.module
from hypothesis import given, strategies as st


@given(number=st.integers())
def test_fuzz_is_even(number: int) -> None:
    package_name.module.is_even(number=number)

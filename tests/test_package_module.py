"""
Run a test through pytest.
"""

from package_name.module import is_even


def test_is_even():
    # assert that 2 is detected as an even number
    assert is_even(2)

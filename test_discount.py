import pytest
from discount import apply_discount


# Live coding 1: this test found the bug (it divided by 10 instead of 100)
def test_ten_percent_off():
    assert apply_discount(100, 10) == 90


# CORE: edge cases
def test_zero_percent_changes_nothing():
    assert apply_discount(100, 0) == 100


def test_hundred_percent_is_free():
    assert apply_discount(100, 100) == 0


# STRETCH: one test function, many cases
@pytest.mark.parametrize("price, percent, expected", [
    (100, 10, 90),
    (100, 0, 100),
    (100, 100, 0),
    (50, 50, 25),
    (80, 25, 60),
])
def test_discount_table(price, percent, expected):
    assert apply_discount(price, percent) == expected


# STRETCH: invalid input must be rejected
def test_negative_percent_is_rejected():
    with pytest.raises(ValueError):
        apply_discount(100, -5)

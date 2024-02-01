import pytest
from modules import descending_order


def describe_descending_roder():
    def should_error_when_not_number():
        """🧪 should error if not a number"""
        with pytest.raises(ValueError, match="❗️ Input should be a number"):
            descending_order.descending_order("blah")

    def should_return_1_when_input_1():
        """🧪 should return 1 when input is 1"""
        assert descending_order.descending_order(1) == 1

    def should_return_54421_when_input_42145():
        """🧪 should return 54421 when input is 42145"""
        assert descending_order.descending_order(42145) == 54421

    def should_return_654321_when_input_145263():
        """🧪 should return 654321 when input is 145263"""
        assert descending_order.descending_order(145263) == 654321

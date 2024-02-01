import pytest
from modules import descending_order


def describe_descending_roder():
    def should_error_when_not_number():
        """🧪 should error if not a number"""
        with pytest.raises(ValueError, match="❗️ Input should be a number"):
            descending_order.descending_order("blah")

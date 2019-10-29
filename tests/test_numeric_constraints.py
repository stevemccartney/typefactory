"""
Test numeric constraints return an error string when value does not satisfy constraint and None when it does
"""
from decimal import Decimal

import pytest

from typefactory.constraints import numeric


class TestMinimum:
    @staticmethod
    @pytest.mark.parametrize("config, value", [(2, 1), (2.0, 1.0), (Decimal(2), Decimal(1))])
    def test_minimum_triggered_by_value_less_than_minimum(config, value):
        c = numeric.Minimum(config)
        assert isinstance(c(value), str)

    @staticmethod
    @pytest.mark.parametrize("config, value", [(2, 2), (2.0, 2.0), (Decimal(2), Decimal(2))])
    def test_minimum_not_triggered_by_value_equal_to_minimum(config, value):
        c = numeric.Minimum(config)
        assert c(value) is None

    @staticmethod
    @pytest.mark.parametrize("config, value", [(2, 3), (2.0, 3.0), (Decimal(2), Decimal(3))])
    def test_minimum_not_triggered_by_value_greater_than_minimum(config, value):
        c = numeric.Minimum(config)
        assert c(value) is None


class TestExclusiveMinimum:
    @staticmethod
    @pytest.mark.parametrize("config, value", [(2, 1), (2.0, 1.0), (Decimal(2), Decimal(1))])
    def test_minimum_triggered_by_value_less_than_minimum(config, value):
        c = numeric.ExclusiveMinimum(config)
        assert isinstance(c(value), str)

    @staticmethod
    @pytest.mark.parametrize("config, value", [(2, 2), (2.0, 2.0), (Decimal(2), Decimal(2))])
    def test_minimum_triggered_by_value_equal_to_minimum(config, value):
        c = numeric.ExclusiveMinimum(config)
        assert isinstance(c(value), str)

    @staticmethod
    @pytest.mark.parametrize("config, value", [(2, 3), (2.0, 3.0), (Decimal(2), Decimal(3))])
    def test_minimum_not_triggered_by_value_greater_than_minimum(config, value):
        c = numeric.ExclusiveMinimum(config)
        assert c(value) is None


class TestMaximum:
    @staticmethod
    @pytest.mark.parametrize("config, value", [(2, 1), (2.0, 1.0), (Decimal(2), Decimal(1))])
    def test_maximum_not_triggered_by_value_less_than_maximum(config, value):
        c = numeric.Maximum(config)
        assert c(value) is None

    @staticmethod
    @pytest.mark.parametrize("config, value", [(2, 2), (2.0, 2.0), (Decimal(2), Decimal(2))])
    def test_maximum_not_triggered_by_value_equal_to_maximum(config, value):
        c = numeric.Maximum(config)
        assert c(value) is None

    @staticmethod
    @pytest.mark.parametrize("config, value", [(2, 3), (2.0, 3.0), (Decimal(2), Decimal(3))])
    def test_maximum_triggered_by_value_greater_than_maximum(config, value):
        c = numeric.Maximum(config)
        assert isinstance(c(value), str)


class TestExclusiveMaximum:
    @staticmethod
    @pytest.mark.parametrize("config, value", [(2, 1), (2.0, 1.0), (Decimal(2), Decimal(1))])
    def test_exclusive_maximum_not_triggered_by_value_less_than_exclusive_maximum(config, value):
        c = numeric.ExclusiveMaximum(config)
        assert c(value) is None

    @staticmethod
    @pytest.mark.parametrize("config, value", [(2, 2), (2.0, 2.0), (Decimal(2), Decimal(2))])
    def test_exclusive_maximum_triggered_by_value_equal_to_exclusive_maximum(config, value):
        c = numeric.ExclusiveMaximum(config)
        assert isinstance(c(value), str)

    @staticmethod
    @pytest.mark.parametrize("config, value", [(2, 3), (2.0, 3.0), (Decimal(2), Decimal(3))])
    def test_exclusive_maximum_not_triggered_by_value_greater_than_exclusive_maximum(config, value):
        c = numeric.ExclusiveMaximum(config)
        assert isinstance(c(value), str)


class TestMultipleOf:
    @staticmethod
    @pytest.mark.parametrize("config, value", [(2, 1), (2.0, 1.0), (Decimal(2), Decimal(1))])
    def test_multiple_of_triggered_by_value_not_multiple_of(config, value):
        c = numeric.MultipleOf(config)
        assert isinstance(c(value), str)

    @staticmethod
    @pytest.mark.parametrize("config, value", [(2, 4), (2.0, 4.0), (Decimal(2), Decimal(4))])
    def test_multiple_of_not_triggered_by_value_that_is_multiple_of(config, value):
        c = numeric.MultipleOf(config)
        assert c(value) is None

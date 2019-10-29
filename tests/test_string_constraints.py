"""
Test string constraints return an error string when value does not satisfy constraint and None when it does
"""
from typefactory.constraints import string


class TestMinLength:
    @staticmethod
    def test_min_length_triggered_by_string_shorter_than_min_length():
        c = string.MinLength(4)
        assert isinstance(c("123"), str)

    @staticmethod
    def test_min_length_not_triggered_by_string_same_length_as_min_length():
        c = string.MinLength(4)
        assert c("1234") is None

    @staticmethod
    def test_min_length_not_triggered_by_string_longer_than_min_length():
        c = string.MinLength(4)
        assert c("12345") is None


class TestMaxLength:
    @staticmethod
    def test_max_length_not_triggered_by_string_shorter_than_min_length():
        c = string.MaxLength(4)
        assert c("123") is None

    @staticmethod
    def test_max_length_not_triggered_by_string_same_length_as_max_length():
        c = string.MaxLength(4)
        assert c("1234") is None

    @staticmethod
    def test_max_length_triggered_by_string_longer_than_max_length():
        c = string.MaxLength(4)
        assert isinstance(c("12345"), str)


class TestPattern:
    @staticmethod
    def test_pattern_not_triggered_by_matching_string():
        c = string.Pattern("^[a-z]{2,4}$")
        assert c("abc") is None

    @staticmethod
    def test_pattern_triggered_by_non_matching_string():
        c = string.Pattern("^[a-z]{2,4}$")
        assert isinstance(c("abcdefgh"), str)

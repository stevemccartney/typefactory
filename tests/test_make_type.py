import pytest

from typefactory import make_type
from typefactory.constraints import numeric


@pytest.mark.parametrize("type_", (int, str, float))
def test_make_type_returns_a_new_type_that_is_a_subclass_of_the_base_type(type_):
    """
    make_type(base, name, typed_constraints) should return a new type that is a subclass of the base type given in the
    base parameter.
    """
    new = make_type(type_, "NewType", [])
    assert new != type_
    assert issubclass(new, type_)


def test_new_types_have_introspectable_constraints():
    new = make_type(int, "NewType", [numeric.Minimum(0), numeric.Maximum(10)])
    assert isinstance(new.__constraints__[0], numeric.Minimum)
    assert new.__constraints__[0].param == 0
    assert isinstance(new.__constraints__[1], numeric.Maximum)
    assert new.__constraints__[1].param == 10

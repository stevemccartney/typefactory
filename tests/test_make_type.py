import pytest

from typefactory import make_type
from typefactory.constraints import numeric


@pytest.mark.parametrize("type_", (int, str, float))
def test_make_type_returns_a_new_type_that_is_a_subclass_of_the_base_type(type_):
    """
    Given a base type
    When a new type is created from the base type with no constraints
    Then the new type is a distinct subclass of the original type
    """
    new = make_type(type_, "NewType", [])
    assert new != type_
    assert issubclass(new, type_)


def test_new_types_have_introspectable_constraints():
    """
    Given a list of minimum and maximum numeric constraints
    When a new type is created as a subclass of int with these constraints
    Then the new type can be introspected to confirm the constraints are present on the type
    """
    constraints = [numeric.Minimum(0), numeric.Maximum(10)]
    new = make_type(int, "NewType", constraints)
    assert isinstance(new.__constraints__[0], numeric.Minimum)
    assert new.__constraints__[0].param == 0
    assert isinstance(new.__constraints__[1], numeric.Maximum)
    assert new.__constraints__[1].param == 10


def test_instantiating_a_new_type_returns_expected_type():
    """
    Given a new type created by make_type()
    When the type is instantiated with a valid value
    Then an instance of the new type is returned
    And the instance can also be verified as being a subclass of the base type (int in this case)
    """
    NewType = make_type(int, "NewType", [numeric.Minimum(0), numeric.Maximum(10)])
    instance = NewType(5)
    assert isinstance(instance, NewType)
    assert isinstance(instance, int)


def test_instantiating_a_new_type_with_a_bad_value_throws_exception():
    """
    Given a new type created by make_type()
    When the type is instantiated with an invalid value
    Then a ValueError is raised
    """
    NewType = make_type(int, "NewType", [numeric.Minimum(0), numeric.Maximum(10)])
    with pytest.raises(ValueError):
        NewType(-5)


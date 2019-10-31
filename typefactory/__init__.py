"""
Implement constraints as per https://json-schema.org/understanding-json-schema/reference/numeric.html
"""
from typing import TypeVar, Type

from inspect import getfullargspec

__version__ = "0.1.1"

BaseType = TypeVar("BaseType")


def make_type(base: Type, name: str, type_constraints) -> Type:
    def __new__(cls, value):
        result = base.__new__(cls, value)
        errors = []
        for constraint in cls.__constraints__:
            # TODO: make this call an lru cache for performance?
            argspec = getfullargspec(constraint)
            if len(argspec.args) == 2:
                error = constraint(result)
            else:
                error = constraint(result, cls.__constraints__)

            if error:
                errors.append(error)
        if errors:
            raise ValueError(f"Invalid {cls.__name__}({value}): {errors}")
        return result

    methods = {"__new__": __new__, "__constraints__": type_constraints}
    return type(name, (base,), methods)


def type_constraints(value):
    """
    If the value passed in is either a constrained type or instance of a constrained type, return the constraint objects
    for the type.
    """
    return getattr(value, "__constraints__", [])

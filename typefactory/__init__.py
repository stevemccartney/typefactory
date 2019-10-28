"""
Implement constraints as per https://json-schema.org/understanding-json-schema/reference/numeric.html
"""
from typing import TypeVar, Type

BaseType = TypeVar("BaseType")


def make_type(base: Type, name: str, type_constraints) -> Type:
    def __new__(cls, value):
        result = base.__new__(cls, value)
        errors = []
        for constraint in cls.__constraints__:
            error = constraint(result)
            if error:
                errors.append(error)
        if errors:
            raise ValueError(f"Invalid {cls.__name__}({value}): {errors}")
        return result

    methods = {"__new__": __new__, "__constraints__": type_constraints}
    return type(name, (base,), methods)

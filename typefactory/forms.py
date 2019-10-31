from typing import Type

from wtforms import StringField, Field, IntegerField, PasswordField
from wtforms.widgets import TextInput, PasswordInput

from typefactory import type_constraints
from typefactory.constraints import string, numeric

__all__ = ("make_string_field", "make_password_field", "make_integer_field")

constraint_input = {
    string.MinLength: "minlength",
    string.MaxLength: "maxlength",
    string.Pattern: "pattern",
    numeric.Minimum: "min",
    numeric.Maximum: "max",
    numeric.MultipleOf: "step",
}


def kwargs_for_input_type(type_):
    kwargs = {}
    field_constraints = type_constraints(type_)
    for field_constraint in field_constraints:
        class_ = field_constraint.__class__
        if class_ in constraint_input and class_ not in kwargs:
            kwargs[constraint_input[class_]] = field_constraint.param

    return kwargs


class ConstrainedInput(TextInput):
    """
    A ConstrainedInput widget adds attributes to the input tag based on the constraints attached to the type passed
    in the constructor in the constrained_type parameters.
    """

    def __init__(self, constrained_type: Type = None):
        super().__init__()
        self.type_ = constrained_type
        self.default_kwargs = kwargs_for_input_type(self.type_)

    def __call__(self, field, **kwargs):
        kwargs_with_defaults = self.default_kwargs.copy()
        kwargs_with_defaults.update(kwargs)
        return super().__call__(field, **kwargs_with_defaults)


class ConstrainedTextInput(ConstrainedInput):
    input_type = "text"


class ConstrainedPasswordInput(ConstrainedInput, PasswordInput):
    input_type = "password"


class ConstrainedIntegerInput(ConstrainedInput):
    input_type = "number"


def make_password_field(value_type: Type, name: str, base_field_type: Type[Field] = PasswordField, **kwargs) -> Type:
    return make_string_field(value_type, name, base_field_type, widget_class=ConstrainedPasswordInput, **kwargs)


def make_string_field(value_type: Type, name: str, base_field_type: Type[Field] = StringField, widget_class=ConstrainedTextInput, **kwargs) -> Type:
    kwargs["filters"] = (lambda x: value_type(x) if x is not None else "", )
    kwargs["widget"] = widget_class(value_type)

    def __init__(self, *args, **kwargs):
        if hasattr(self, "render_kw") and "render_kw" not in kwargs:
            kwargs["render_kw"] = self.render_kw
        if hasattr(self, "filters") and "filters" not in kwargs:
            kwargs["filters"] = self.filters
        return base_field_type.__init__(self, *args, **kwargs)

    kwargs["__init__"] = __init__
    return type(name, (base_field_type,), kwargs)


def make_integer_field(value_type: Type, name: str, base_field_type: Type[Field] = IntegerField) -> Type:
    attributes = {
        "filters": lambda x: value_type(x) if x is not None else "",
        "widget": ConstrainedIntegerInput(value_type),
    }
    return type(name, (base_field_type,), attributes)

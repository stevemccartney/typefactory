# TypeFactory

**TypeFactory is in a pre-alpha state and should not be used in production.  The overall API, types and exceptions are expected to change significantly.**

TypeFactory simplifies the creation and utilisation of typed and constrained value objects.

## Why?

Passing around primitive values (strings, ints, floats etc...) tends to led towards code checking constraints at multiple layers within a single app and subsequently to inconsistencies and bugs as constraint checks in different layers diverge.

By casting the raw data as value objects based on constrained types, and using optionally type checking:
- domain concepts and rules can be encapsulated at the lowest possible level in value objects
- code becomes clearer and tied to domain concepts
- the amount of code dedicated to data validation can be reduced and centralised
- bugs related to bad data may be reduced
- validation is naturally pushed out to the application boundaries leaving code that can be focused on implementing domain logic/business rules

## Features

- extend an existing type with constraints
- built-in constraints for string and numeric types that match JSON Schema constraints (e.g. minimum, multiple_of, pattern etc...)
- create custom constraints for any type
- introspect types and values to extract and utilise their constraints, such as when creating HTML forms
- extended ValueError exception that reports all failing constraints for a value

## Examples

### Defining types

```python
from typefactory import make_type
from typefactory.constraints import string, numeric

Id = make_type(str, "Id", [string.Pattern("^[A-Z2-7]{26}$")])
Age = make_type(int, "Age", [numeric.Minimum(0), numeric.Maximum(150)])
Username = make_type(str, "Username", [string.MinLength(4), string.MaxLength(32), string.Pattern("^[A-Za-z][A-Za-z0-9]{2,30}[A-zA-z]$")])
Password = make_type(str, "Password", [string.MinLength(8), string.MaxLength(256)])
```

### Using types

```
>>> my_age = Age(40)
>>> my_age
40
>>> type(my_age)
<class '__main__.Age'>
>>> isinstance(my_age, int)
True
>>> isinstance(my_age, Age)
True
```

### Exceptions

Types throw ValueErrors when their input data does not satisfy the types constraints.  All failing constraints are returned.

```python
username = Username("123")

>>> ValueError: Invalid Username(123): ['Value cannot be less than 4 characters in length', 'Value must match pattern ^[A-Za-z][A-Za-z0-9]{2,30}[A-zA-z]$']

username = Username("1username")

>>> ValueError: Invalid Username(1username): ['Value must match pattern ^[A-Za-z][A-Za-z0-9]{2,30}[A-zA-z]$']
```

### Type Checking

Created types can be used with optional type checking tools to enable type strong contracts propagate through the code base, reducing the need to assert values satisfy constraints at multiple levels within the code.

Typically values will be converted to richer, constrained types at the external boundaries (e.g. incoming web request or database record) and then used internally.

```python
def register(id: Id, username: Username, password: Password):
    ...
```

## Installation

Install from [PyPI](https://pypi.org/project/typefactory): 

```bash
pip install typefactory
```

## Roadmap

- Subclass ValueError to pass back list of all failing constraints
- Container types
- Functions for creating the following from types:
    - Flask URL converters
    - SqlAlchemy custom types
    - Marshmallow fields
    - WTForms fields and widgets

# Changelog

## v0.1.2 - 2020-01-25

- Include all subpackages automatically via find_packages

## v0.1.1 - 2019-10-29

- Add tests for instantiating a new type with valid and invalid values
- Improve test module comments

## v0.1.0 - 2019-10-28

- Initial release
- Added make_type() function to create new types from a base type + constraints
- Added initial set of constraint classes for string and numeric constraints based on those in JSON Schema (minimum, exclusiveMinimum, multiple_of etc...)

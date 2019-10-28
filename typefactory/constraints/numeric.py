from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, Union


Number = Union[int, float, Decimal]


@dataclass
class MultipleOf:
    param: Number

    def __call__(self, value: Number) -> Optional[str]:
        if value % self.param != 0:
            return f"Value must be a multiple of {self.param}"


@dataclass
class Minimum:
    param: Number

    def __call__(self, value: Number) -> Optional[str]:
        if value < self.param:
            return f"Value must be >= {self.param}"


@dataclass
class ExclusiveMinimum:
    param: Number

    def __call__(self, value: Number) -> Optional[str]:
        if value <= self.param:
            return f"Value must be > {self.param}"


@dataclass
class Maximum:
    param: Number

    def __call__(self, value: Number) -> Optional[str]:
        if value > self.param:
            return f"Value must be <= {self.param}"


@dataclass
class ExclusiveMaximum:
    param: Number

    def __call__(self, value: Number) -> Optional[str]:
        if value >= self.param:
            return f"Value must be < {self.param}"

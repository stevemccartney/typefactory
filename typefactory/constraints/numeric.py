from dataclasses import dataclass
from numbers import Real
from typing import Optional


@dataclass
class MultipleOf:
    param: Real

    def __call__(self, value: Real) -> Optional[str]:
        if value % self.param != 0:
            return f"Value must be a multiple of {self.param}"
        else:
            return None


@dataclass
class Minimum:
    param: Real

    def __call__(self, value: Real) -> Optional[str]:
        if value < self.param:
            return f"Value must be >= {self.param}"
        else:
            return None


@dataclass
class ExclusiveMinimum:
    param: Real

    def __call__(self, value: Real) -> Optional[str]:
        if value <= self.param:
            return f"Value must be > {self.param}"
        else:
            return None


@dataclass
class Maximum:
    param: Real

    def __call__(self, value: Real) -> Optional[str]:
        if value > self.param:
            return f"Value must be <= {self.param}"
        else:
            return None


@dataclass
class ExclusiveMaximum:
    param: Real

    def __call__(self, value: Real) -> Optional[str]:
        if value >= self.param:
            return f"Value must be < {self.param}"
        else:
            return None

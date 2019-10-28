import re
from dataclasses import dataclass
from typing import Optional, Pattern as PatternType


@dataclass
class MinLength:
    param: int

    def __call__(self, value: str) -> Optional[str]:
        if len(value) < self.param:
            return f"Value cannot be less than {self.param} characters in length"


@dataclass
class MaxLength:
    param: int

    def __call__(self, value: str) -> Optional[str]:
        if len(value) > self.param:
            return f"Value cannot be more than {self.param} characters in length"


@dataclass
class Pattern:
    param: str
    compiled_re: Optional[PatternType] = None

    def __post_init__(self):
        self.compiled_re = re.compile(self.param)

    def __call__(self, value: str) -> Optional[str]:
        if not self.compiled_re.fullmatch(value):
            return f"Value must match pattern {self.param}"

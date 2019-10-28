import re
from dataclasses import dataclass, field
from typing import Optional, Pattern as PatternType


@dataclass
class MinLength:
    param: int

    def __call__(self, value: str) -> Optional[str]:
        if len(value) < self.param:
            return f"Value cannot be less than {self.param} characters in length"
        else:
            return None


@dataclass
class MaxLength:
    param: int

    def __call__(self, value: str) -> Optional[str]:
        if len(value) > self.param:
            return f"Value cannot be more than {self.param} characters in length"
        else:
            return None


@dataclass
class Pattern:
    param: str
    compiled_re: PatternType = field(init=False)

    def __post_init__(self):
        self.compiled_re = re.compile(self.param)

    def __call__(self, value: str) -> Optional[str]:
        if not self.compiled_re.fullmatch(value):
            return f"Value must match pattern {self.param}"
        else:
            return None

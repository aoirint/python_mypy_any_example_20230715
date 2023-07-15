from typing import Any


a: Any = None
b: str = "1"
c: str | None = a

if c is None:
    c = b

reveal_type(c)  # Revealed type is "builtins.str"

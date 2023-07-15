from typing import Any


a: Any = None
b: int = 1
c: str | None = a

if c is None:
    c = b  # Incompatible types in assignment (expression has type "int", variable has type "Optional[str]")  [assignment]

reveal_type(c)  # Revealed type is "Union[builtins.str, None]"

from typing import Any


a: Any = None
b: int = 1
c: str = a if a is not None else b

reveal_type(c)  # Revealed type is "builtins.str"

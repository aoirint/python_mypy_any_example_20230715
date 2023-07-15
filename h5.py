from typing import Any


a: Any = None
b: int = 1
c: str = b if a is None else a

reveal_type(c)  # Revealed type is "builtins.str"

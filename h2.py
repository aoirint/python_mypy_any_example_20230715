from typing import Any


a: Any = None
b: int = 1

reveal_type(a if a is not None else b)  # Revealed type is "Any"

from typing import Any


def get_int() -> int:
    return 0

a: Any = None
b: str = a if a is not None else get_int()

reveal_type(b)  # Revealed type is "builtins.str"

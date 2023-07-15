from typing import Any


a: Any = None
b: int = 1
c: str = a or b  # Incompatible types in assignment (expression has type "Union[Any, int]", variable has type "str")  [assignment]

reveal_type(c)  # Revealed type is "builtins.str"

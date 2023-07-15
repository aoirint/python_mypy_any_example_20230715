from pathlib import Path
from typing import Any

class A:
    pass

def engine_root() -> A:
    return A()

voicevox_dir: Any = Path()

root_dir: Path | None = voicevox_dir

if root_dir is None:
    root_dir = engine_root()  # Incompatible types in assignment (expression has type "A", variable has type "Path | None")  [assignment]

reveal_type(root_dir)  # Revealed type is "Union[pathlib.Path, None]"

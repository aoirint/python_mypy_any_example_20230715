from pathlib import Path
from typing import Any

class A:
    pass

def engine_root() -> A:
    return A()

voicevox_dir: Any = Path()

root_dir: Path = voicevox_dir if voicevox_dir is not None else engine_root()

reveal_type(root_dir)  # Revealed type is "pathlib.Path"

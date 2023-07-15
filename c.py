from pathlib import Path
from typing import Any

def engine_root() -> Path:
    return Path()

voicevox_dir: Any = Path()

root_dir: Path = voicevox_dir if voicevox_dir is not None else engine_root()

reveal_type(root_dir)  # Revealed type is "Any"

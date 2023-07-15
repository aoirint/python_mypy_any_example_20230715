from pathlib import Path
from typing import Any

def engine_root() -> Path:
    return Path()

arg_voicevox_dir: Any = Path()

voicevox_dir: Path | None = arg_voicevox_dir

root_dir = voicevox_dir if voicevox_dir is not None else engine_root()

reveal_type(voicevox_dir)  # Revealed type is "Union[pathlib.Path, None]"
reveal_type(root_dir)  # Revealed type is "pathlib.Path"

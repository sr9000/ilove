from pathlib import Path

from . import base

_DEFAULT_NAME = "default.db"


def create_default() -> Path:
    path = Path(_DEFAULT_NAME)
    if path.exists():
        path.unlink()

    path.touch()  # Create an empty file
    return path


def init(path: Path) -> None:
    assert path.exists()
    assert path.is_file()

    if not base.db.is_closed():
        base.db.close()
    base.db.init(path)
    base.db.connect()
    base.db.create_tables(base.get_all_models())

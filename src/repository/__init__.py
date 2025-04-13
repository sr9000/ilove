from pathlib import Path
from . import base


def init(dbname: str) -> None:
    path = Path(dbname)
    assert path.exists()
    assert path.is_file()

    if not base.db.is_closed():
        base.db.close()
    base.db.init(path)
    base.db.connect()
    base.db.create_tables(base.get_all_models())

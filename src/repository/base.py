from peewee import *

db = SqliteDatabase(None)


class Base(Model):
    def __init_subclass__(cls: "Base", **kwargs):
        super().__init_subclass__(**kwargs)
        _ALL_MODELS.append(cls)

    class Meta:
        database = db


_ALL_MODELS: list[Base] = []


def get_all_models() -> list[Base]:
    return list(_ALL_MODELS)

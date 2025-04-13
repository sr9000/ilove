from peewee import *

from .base import Base


class Task(Base):
    name = TextField()
    is_active = BooleanField(default=True)
    is_short = BooleanField(default=False)
    is_important = BooleanField(default=False)

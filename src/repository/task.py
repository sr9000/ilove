from .base import Base
from peewee import *


class Task(Base):
    name = TextField()
    is_active = BooleanField(default=True)
    is_short = BooleanField(default=False)
    is_important = BooleanField(default=False)

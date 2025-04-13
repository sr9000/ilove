import flet as ft

import repository
from view import pages


def main(page: ft.Page):
    pages.ilove(page)


db_path = repository.create_default()
repository.init(db_path)

ft.app(main)

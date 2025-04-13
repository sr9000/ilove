import flet as ft

import repository
from view import pages


def main(page: ft.Page):
    db_path = repository.create_default()
    repository.init(db_path)
    pages.ilove(page)


ft.app(main)

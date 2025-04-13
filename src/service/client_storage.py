from typing import Any

import flet as ft

_GLOBAL_PAGE: ft.Page | None = None


def init(page: ft.Page):
    global _GLOBAL_PAGE
    _GLOBAL_PAGE = page


def set_val(name: str, value: Any):
    return _GLOBAL_PAGE.client_storage.set(name, value)


def get_val(name: str) -> Any:
    return _GLOBAL_PAGE.client_storage.get(name)

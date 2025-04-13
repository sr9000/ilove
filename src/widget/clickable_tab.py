from typing import Callable

import flet as ft


class ClickableTab(ft.Tab):
    def __init__(self, on_click: Callable[[], None] = None, **kwargs):
        super().__init__(**kwargs)

        self.on_click = lambda: None
        if on_click is not None:
            self.on_click = on_click

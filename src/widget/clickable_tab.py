from typing import Callable

import flet as ft

type Callback = Callable[[], None]


class ClickableTab(ft.Tab):
    def __init__(
        self,
        on_click: Callback = lambda: None,
        did_mount: Callback = lambda: None,
        will_unmount: Callback = lambda: None,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.on_click = on_click
        self._did_mount = did_mount
        self._will_unmount = will_unmount

    def did_mount(self):
        super().did_mount()
        self._did_mount()

    def will_unmount(self):
        super().will_unmount()
        self._will_unmount()

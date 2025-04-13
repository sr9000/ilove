from typing import Callable

import flet as ft

type EventCallback = Callable[[ft.ControlEvent], None]


def _chain(*callbacks: EventCallback) -> EventCallback:
    def _inner(e: ft.ControlEvent):
        for cb in callbacks:
            cb(e)

    return _inner


def _new_button(
    button: str | tuple[str, EventCallback], close_cb: EventCallback
) -> ft.TextButton:
    style = ft.ButtonStyle(color=ft.Colors.BLUE)
    match button:
        case str(s):
            return ft.TextButton(text=s, style=style, on_click=close_cb)
        case (str(s), EventCallback(cb)):
            return ft.TextButton(text=s, style=style, on_click=_chain(close_cb, cb))
        case _:
            raise ValueError(f"Invalid button data: {button!r}")


def show_warning(
    page, msg: str, buttons: list[str | tuple[str, EventCallback]]
) -> None:
    def close_banner(_: ft.ControlEvent):
        page.close(banner)

    banner = ft.Banner(
        bgcolor=ft.Colors.AMBER_100,
        leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.AMBER, size=40),
        content=ft.Text(value=msg, color=ft.Colors.BLACK),
        actions=[_new_button(bt, close_banner) for bt in buttons],
    )
    page.open(banner)

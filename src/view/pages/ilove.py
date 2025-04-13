import flet as ft

import view.tabs.counter
from service import client_storage
from view import tabs
from widget.clickable_tab import ClickableTab


def init(page: ft.Page):
    client_storage.init(page)
    page.add(
        ft.Tabs(
            selected_index=0,
            animation_duration=300,
            expand=True,
            tabs=[
                ft.Tab(
                    text="Home",
                    icon=ft.Icons.HOME,
                    content=view.tabs.counter.counter(ft.Pagelet(content=ft.Text())),
                ),
                ft.Tab(
                    text="Logs",
                    icon=ft.Icons.EVENT_NOTE,
                    content=ft.Text("This is logs"),
                ),
                tabs.tasks(),
            ],
            on_click=lambda e: (
                e.control.on_click() if isinstance(e.control, ClickableTab) else None
            ),
        )
    )

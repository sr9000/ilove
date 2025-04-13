import flet as ft

from service import client_storage
from view import tabs


def init(page: ft.Page):
    client_storage.init(page)
    page.add(
        ft.Tabs(
            selected_index=0,
            animation_duration=300,
            expand=1,
            tabs=[
                ft.Tab(
                    text="Home",
                    icon=ft.Icons.HOME,
                    content=tabs.counter(ft.Pagelet(content=ft.Text())),
                ),
                ft.Tab(
                    text="Logs",
                    icon=ft.Icons.EVENT_NOTE,
                    content=ft.Text("This is logs"),
                ),
                ft.Tab(
                    text="Tasks",
                    icon=ft.Icons.CHECKLIST,
                    content=ft.Text("This is tasks"),
                ),
            ],
        )
    )

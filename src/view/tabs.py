import flet as ft

from control.counter import increment_click
from service import client_storage


def counter(page: ft.Pagelet) -> ft.Pagelet:
    init_number = client_storage.get_val("number.setting") or 0
    counter_widget = ft.Text(str(init_number), size=50, data=init_number)

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click(counter_widget)
    )
    page.content = ft.SafeArea(
        ft.Container(
            counter_widget,
            alignment=ft.alignment.center,
        ),
        expand=True,
    )

    return page

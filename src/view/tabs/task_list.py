import flet as ft

from repository.task import Task
from widget.clickable_tab import ClickableTab


class TaskBind(ft.Card):
    def __init__(self, task: Task, hiding_switch=True):
        is_active = ft.Switch(
            value=task.is_active, visible=not hiding_switch, on_change=lambda e: None
        )


def new() -> ClickableTab:
    active_only_chip = ft.Chip(
        label=ft.Text("active only"), selected=True, on_select=lambda e: None
    )
    sorted_chip = ft.Chip(label=ft.Text("sorted"), on_select=lambda e: None)
    grouped_chip = ft.Chip(label=ft.Text("grouped"), on_select=lambda e: None)

    name_field = ft.TextField(label="name")
    short_chip = ft.Chip(label=ft.Text("short"), on_select=lambda e: None)
    important_chip = ft.Chip(label=ft.Text("important"), on_select=lambda e: None)

    return ClickableTab(
        text="Tasks",
        icon=ft.Icons.CHECKLIST,
        content=ft.Container(
            margin=10,
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            active_only_chip,
                            sorted_chip,
                            grouped_chip,
                        ]
                    ),
                    ft.Divider(thickness=2),
                    ft.Row(
                        controls=[
                            ft.IconButton(
                                icon=ft.Icons.ADD_CIRCLE_OUTLINE,
                                on_click=lambda e: None,
                            ),
                            name_field,
                            short_chip,
                            important_chip,
                        ]
                    ),
                    ft.ListView(),
                ]
            ),
        ),
    )

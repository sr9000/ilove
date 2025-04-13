import flet as ft

from repository.task import Task
from view.alerts import show_warning
from widget.clickable_tab import ClickableTab


class TaskBind(ft.Card):
    def __init__(self, task: Task, hiding_switch=True, **kwargs):
        self.task = task

        self.is_active = ft.Switch(
            value=task.is_active, visible=not hiding_switch, on_change=lambda e: None
        )
        self.name = ft.Text(value=task.name)
        self.is_short = ft.Icon(
            ft.Icons.TIMER_OUTLINED, color=ft.Colors.PRIMARY, visible=task.is_short
        )
        self.is_important = ft.Icon(
            ft.Icons.CRISIS_ALERT, color=ft.Colors.TERTIARY, visible=task.is_important
        )

        self.edit = ft.Button(text="edit", icon=ft.Icons.EDIT, visible=False)

        super().__init__(
            content=ft.Container(
                ft.Row(
                    controls=[
                        self.is_active,
                        self.is_short,
                        self.is_important,
                        ft.VerticalDivider(),
                        self.name,
                        self.edit,
                    ]
                ),
                on_click=self.on_click,
                on_hover=self.on_hover,
            ),
            **kwargs,
        )

    def on_click(self, _: ft.ControlEvent): ...  # open edit mode

    def on_hover(self, e: ft.ControlEvent):
        self.edit.visible = e.data.lower() in ("yes", "true", "t", "1")
        self.edit.update()


def new() -> ClickableTab:
    active_only_chip = ft.Chip(
        label=ft.Text("active only"), selected=True, on_select=lambda e: None
    )
    sorted_chip = ft.Chip(label=ft.Text("sorted"), on_select=lambda e: None)
    grouped_chip = ft.Chip(label=ft.Text("grouped"), on_select=lambda e: None)

    name_field = ft.TextField(label="name")
    short_chip = ft.Chip(label=ft.Text("short"), on_select=lambda e: None)
    important_chip = ft.Chip(label=ft.Text("important"), on_select=lambda e: None)

    list_view = ft.ListView(controls=[], expand=True)

    def add_new_task(e: ft.ControlEvent):
        stripped = name_field.value.strip()
        if not stripped:
            show_warning(e.control.page, "Name must not be empty!", ["Okay"])
            return

        task = Task.create(
            name=stripped,
            is_short=short_chip.selected,
            is_important=important_chip.selected,
        )

        name_field.value = ""
        name_field.update()

        new_bind = TaskBind(task, hiding_switch=not active_only_chip.selected)
        list_view.controls.insert(0, new_bind)
        list_view.update()

    view_modes = ft.Row(
        controls=[
            active_only_chip,
            sorted_chip,
            grouped_chip,
        ]
    )
    task_options = ft.Row(
        vertical_alignment=ft.CrossAxisAlignment.END,
        controls=[
            ft.IconButton(icon=ft.Icons.ADD_CIRCLE_OUTLINE, on_click=add_new_task),
            ft.Column(
                controls=[ft.Row(controls=[short_chip, important_chip]), name_field]
            ),
        ],
    )

    return ClickableTab(
        text="Tasks",
        icon=ft.Icons.CHECKLIST,
        content=ft.Container(
            margin=10,
            content=ft.Column(
                controls=[view_modes, ft.Divider(thickness=2), task_options, list_view]
            ),
        ),
    )

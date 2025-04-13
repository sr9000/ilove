import uuid
from dataclasses import dataclass
from enum import IntEnum, auto

import flet as ft

from repository.task import Task
from view.alerts import show_warning
from widget.clickable_tab import ClickableTab

_topic_task_modified = f"task-modified"
_topic_list_view_changed = f"list-view-changed-{uuid.uuid4()}"


class _LVAction(IntEnum):
    ADD = auto()
    REMOVE = auto()


@dataclass
class _LVMessage:
    action: _LVAction
    task_id: int


class TaskBind(ft.Card):
    def __init__(self, task: Task, hiding_switch=True, **kwargs):
        self.is_active = ft.Switch(visible=not hiding_switch, on_change=lambda e: None)
        self.name = ft.Text()
        self.is_short = ft.Icon(ft.Icons.TIMER_OUTLINED, color=ft.Colors.PRIMARY)
        self.is_important = ft.Icon(ft.Icons.CRISIS_ALERT, color=ft.Colors.TERTIARY)

        self.task = task
        self.hiding_switch = hiding_switch

        self.edit = ft.Button(text="edit", icon=ft.Icons.EDIT, visible=False)

        super().__init__(
            content=ft.Container(
                ft.Row(
                    controls=[
                        self.is_active,
                        self.is_important,
                        self.is_short,
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

    @property
    def hiding_switch(self) -> bool:
        return not self.is_active.visible

    @hiding_switch.setter
    def hiding_switch(self, hiding_switch: bool):
        self.is_active.visible = not hiding_switch

    @property
    def task(self) -> Task:
        return self._task

    @task.setter
    def task(self, task: Task):
        self._task = task

        self.is_active.value = task.is_active
        self.name.value = task.name
        self.is_short.visible = task.is_short
        self.is_important.visible = task.is_important

    def before_update(self):
        self.visible = self.is_active.visible or self.task.is_active

    def on_click(self, _: ft.ControlEvent): ...  # open edit mode

    def on_hover(self, e: ft.ControlEvent):
        self.edit.visible = e.data.lower() in ("true", "yes", "t", "1")
        self.edit.update()


def new(page: ft.Page) -> ClickableTab:
    active_only_chip = ft.Chip(
        label=ft.Text("active only"), selected=True, on_select=lambda e: None
    )
    sorted_chip = ft.Chip(label=ft.Text("sorted"), on_select=lambda e: None)
    grouped_chip = ft.Chip(label=ft.Text("grouped"), on_select=lambda e: None)

    name_field = ft.TextField(label="name")
    short_chip = ft.Chip(label=ft.Text("short"), on_select=lambda e: None)
    important_chip = ft.Chip(label=ft.Text("important"), on_select=lambda e: None)

    list_view = ft.ListView(controls=[], expand=True)

    def add_new_task(_: ft.ControlEvent):
        stripped = name_field.value.strip()
        if not stripped:
            show_warning(page, "Name must not be empty!", ["Okay"])
            return

        task: Task = Task.create(
            name=stripped,
            is_short=short_chip.selected,
            is_important=important_chip.selected,
        )

        name_field.value = ""
        name_field.update()

        page.pubsub.send_all_on_topic(
            _topic_list_view_changed, _LVMessage(_LVAction.ADD, task.get_id())
        )

    def on_list_view_changed(_: str, msg: _LVMessage):
        if not isinstance(msg, _LVMessage):
            return

        if msg.action == _LVAction.ADD:
            task = Task.get(msg.task_id)
            new_bind = TaskBind(task, hiding_switch=not active_only_chip.selected)
            list_view.controls.insert(0, new_bind)

        if msg.action == _LVAction.REMOVE:
            list_view.controls = list(
                filter(lambda tb: tb.task.id != msg.task_id, list_view.controls)
            )

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
                controls=[ft.Row(controls=[important_chip, short_chip]), name_field]
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
        did_mount=lambda: page.pubsub.subscribe_topic(
            _topic_list_view_changed, on_list_view_changed
        ),
        will_unmount=lambda: page.pubsub.unsubscribe_topic(_topic_list_view_changed),
    )

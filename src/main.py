import flet as ft


def main(page: ft.Page):
    init_number = page.client_storage.get("number.setting") or 0

    counter = ft.Text(str(init_number), size=50, data=init_number)

    def increment_click(e):
        counter.data += 1
        page.client_storage.set("number.setting", counter.data)
        counter.value = str(counter.data)
        counter.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )
    page.add(
        ft.SafeArea(
            ft.Container(
                counter,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)

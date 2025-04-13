import flet as ft

from service import client_storage


def increment_click(counter: ft.Text):
    def _inner(*args, **kwargs):
        counter.data += 1
        client_storage.set_val("number.setting", counter.data)
        counter.value = str(counter.data)
        counter.update()

    return _inner

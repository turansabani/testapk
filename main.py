import flet as ft
from flet.core.alignment import center
from flet.core.control_event import ControlEvent

from flet import  TextField

def main(page: ft.Page) -> None:
    page.window.width = 300
    txt:TextField = TextField(text_align=center)
    txt2: TextField = TextField(text_align=center)
    txt3:TextField = TextField(text_align=center)
    txt4: TextField = TextField(text_align=center)
    page.title = 'Domates'
    txt.value= "enter to me"
    txt2.value = "cool"
    page.theme_mode='Dark'
    page.vertical_alignment=ft.MainAxisAlignment.CENTER

    page.add(txt,txt2,txt3,txt4)

if __name__ == '__main__':
    ft.app(target=main)

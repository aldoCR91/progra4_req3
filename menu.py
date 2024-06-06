import flet as ft

def handle_menu_item_click(e, page, appbar_text_ref):
    #print(f"{e.control.content.value}.on_click")
    page.show_snack_bar(ft.SnackBar(content=ft.Text(f"{e.control.content.value}")))
    appbar_text_ref.current.value = e.control.content.value
    if e.control.content.value == "Registrar nuevo":
        page.go("/create")
    if e.control.content.value == "Ver Activos":
        page.go("/read")
    if e.control.content.value == "Calcular todas las depreciaciones":
        page.go("/all_calc")
    if e.control.content.value == "Eliminar":
        page.go("/delete")
    page.update()

def handle_on_open(e):
    print(f"{e.control.content.value}.on_open")

def handle_on_close(e):
    print(f"{e.control.content.value}.on_close")

def create_menubar(appbar_text_ref, page):
    return ft.MenuBar(
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            bgcolor=ft.colors.GREY_200,
            mouse_cursor={ft.MaterialState.HOVERED: ft.MouseCursor.WAIT,
                          ft.MaterialState.DEFAULT: ft.MouseCursor.ZOOM_OUT},
        ),
        controls=[
            ft.SubmenuButton(
                content=ft.Text("Activos"),
                on_open=handle_on_open,
                on_close=handle_on_close,
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Registrar nuevo"),
                        leading=ft.Icon(ft.icons.STAR),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                        on_click=lambda e: handle_menu_item_click(e, page, appbar_text_ref)
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Calcular todas las depreciaciones"),
                        leading=ft.Icon(ft.icons.EDIT),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                        on_click=lambda e: handle_menu_item_click(e, page, appbar_text_ref)
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Eliminar"),
                        leading=ft.Icon(ft.icons.DELETE),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                        on_click=lambda e: handle_menu_item_click(e, page, appbar_text_ref)
                    )
                ]
            )
        ]
    )

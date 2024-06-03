import flet as ft
from activos_data import activos, agregar_activo, actualizar_tabla
from menu import create_menubar
from views import create_main_view, create_create_view, create_read_view, create_update_view, create_delete_view, create_detail_view

def main(page: ft.Page):
    page.title = "Edwards LTDA"
    page.theme_mode = ft.ThemeMode.LIGHT
    appbar_text_ref = ft.Ref[ft.Text]()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_full_screen = False
    page.window_width = 500


    app_bar = ft.AppBar(
        title=ft.Text("Control de activos", ref=appbar_text_ref, color=ft.colors.WHITE),
        center_title=True,
        bgcolor=ft.colors.PURPLE_400
    )

    menubar = create_menubar(appbar_text_ref, page)

    def route_change(route):
        page.views.clear()
        page.views.append(create_main_view(app_bar, menubar, activos))
        
        if page.route == "/create":
            page.views.append(create_create_view(app_bar, menubar, page))
        elif page.route == "/read":
            page.views.append(create_read_view(app_bar, menubar))
        elif page.route == "/update":
            page.views.append(create_update_view(app_bar, menubar))
        elif page.route == "/delete":
            page.views.append(create_delete_view(app_bar, menubar))
        elif page.route.startswith("/detail"):
            identificador = page.route.split("/")[-1]
            page.views.append(create_detail_view(app_bar, menubar, activos, identificador))
        
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)

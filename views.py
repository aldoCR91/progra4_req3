import flet as ft
from activos_data import data_table, agregar_activo

tf_identificador = ft.TextField(label="Identificador", width=400, keyboard_type=ft.KeyboardType.NUMBER, value="0")
tf_nombre = ft.TextField(label="Nombre", width=400)
tf_responsable = ft.TextField(label="Responsable", width=400)
tf_valor = ft.TextField(label="Valor monetario", width=400, keyboard_type=ft.KeyboardType.NUMBER, value="0")
tf_valor_res = ft.TextField(label="Valor de rescate", width=400, keyboard_type=ft.KeyboardType.NUMBER, value="0")
tf_vida_util = ft.TextField(label="Vida util (years)", width=400, keyboard_type=ft.KeyboardType.NUMBER, value="0")

def create_main_view(app_bar, menubar, activos):
    return ft.View(
        "/",
        [
            app_bar,
            ft.Row([menubar]),
            ft.Text(f"Cantidad de activos: {len(activos)}"),
            data_table,
        ],
    )

def create_create_view(app_bar, menubar, page):
    return ft.View(
        "/create",
        [
            app_bar,
            ft.Row([menubar]),
            ft.Text("Datos del nuevo activo", size=30, color="pink600", italic=True),
            tf_identificador,
            tf_nombre,
            tf_responsable,
            tf_vida_util,
            tf_valor,
            tf_valor_res,
            ft.OutlinedButton(text="Guardar", on_click=lambda e: agregar_activo(tf_identificador, tf_nombre, tf_responsable, tf_valor, tf_valor_res, tf_vida_util, page)),
        ],
    )

def create_read_view(app_bar, menubar):
    return ft.View(
        "/read",
        [
            app_bar,
            ft.Row([menubar]),
            ft.Text("read"),
        ],
    )

def create_update_view(app_bar, menubar):
    return ft.View(
        "/update",
        [
            app_bar,
            ft.Row([menubar]),
            ft.Text("update"),
        ],
    )

def create_delete_view(app_bar, menubar):
    return ft.View(
        "/delete",
        [
            app_bar,
            ft.Row([menubar]),
            ft.Text("delete"),
        ],
    )

def create_detail_view(app_bar, menubar):
    return ft.View(
        "/detail",
        [
            app_bar,
            ft.Row([menubar]),
            ft.Text("Detalle de la depreciacion del activo"),
        ],
    )

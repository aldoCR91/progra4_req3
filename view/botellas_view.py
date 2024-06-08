import flet as ft
from controllers.botella import Botella_Controller

def create_botellas_view(app_bar, menubar):
    
    controller = Botella_Controller()

    botellas = controller.get_botellas()
    
    columns = [
        ft.DataColumn(ft.Text("Capacidad")),
        ft.DataColumn(ft.Text("Color")),
        ft.DataColumn(ft.Text("Dimensiones")),
    ]
    
    rows = []

    for botella in botellas:
        row = ft.DataRow(
            cells= [
                ft.DataCell(ft.Text(f"{botella.get_capacidad()}")),
                ft.DataCell(ft.Text(f"{botella.get_color()}")),
                ft.DataCell(ft.Text(f"{botella.get_dimensiones()}")),
            ]
        )
        rows.append(row)
    
    return ft.View(
        "/create",
        [
            app_bar,
            ft.Row([menubar]),
            ft.Text("Datos de las botellas", size=30, color="pink600", italic=True),
            ft.DataTable(columns=columns, rows=rows)

        ],
    )
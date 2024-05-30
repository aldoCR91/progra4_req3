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

def create_detail_view(app_bar, menubar, data, identificador):
    # Buscar activo
    activo = True #next((item for item in activos if item["identificador"] == identificador), None)
    
    identificador = int(identificador)
    data = data[identificador]
    
    nombre = data['nombre']
    responsable = data['responsable']
    valor = int(data['valor'])
    valor_res = int(data['valor_res'])
    vida_util = int(data['vida_util'])
    
    #Tabla de linea recta
    columns=[
        ft.DataColumn(ft.Text("Periodo")),
        ft.DataColumn(ft.Text("Valor a depreciar")),
        ft.DataColumn(ft.Text("Factor")),
        ft.DataColumn(ft.Text("Depreciacion anual")),
        ft.DataColumn(ft.Text("Depreciacion acumulada")),
        ft.DataColumn(ft.Text("Valor en libros")),
    ]
    rows = []
    i = 0
    
    while i <= int(data['vida_util']):
        if i != len(data):
            row = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(f"{i}")),
                    ft.DataCell(ft.Text(f"{valor - valor_res}")),
                    ft.DataCell(ft.Text(f"{(100 / vida_util):.2f}%")),
                    ft.DataCell(ft.Text(f"{(valor - valor_res)*(0.1)}")),
                    ft.DataCell(ft.Text(f"{i * ( (valor - valor_res)/10)}")),
                    ft.DataCell(ft.Text( (valor - valor_res) - (i * (valor - valor_res)) )),
                ]
            )
        if i == len(data):
            row = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(f"{i}")),
                ft.DataCell(ft.Text(f"{valor - valor_res}")),
                ft.DataCell(ft.Text(f"{vida_util}%")),
                ft.DataCell(ft.Text(f"{(valor - valor_res)*(0.1)}")),
                ft.DataCell(ft.Text(f"{i * (valor - valor_res)}")),
                ft.DataCell(ft.Text(f"0")),
            ]
        )
        rows.append(row)
        i = i + 1
        
    
    
    
    
    
    
    
    if activo:
        return ft.View(
            "/detail",
            [
                app_bar,
                ft.Row([menubar]),
                ft.Text(f"Edwards LTDA", size=14, weight=ft.FontWeight.BOLD),
                ft.Text("Depreciacion Linea Recta", size=14, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                ft.Text(f"{nombre}:              {valor}"),
                ft.Text(f"Valor de rescate:     {valor_res}"),
                ft.Text(f"Vida util:            {vida_util}"),
                ft.Divider(),
                ft.DataTable(
                    columns=columns,
                    rows=rows
                ),
                ft.Divider()
                
                
                
                
            ],
        )
    else:
        return ft.View(
            "/detail",
            [
                app_bar,
                ft.Row([menubar]),
                ft.Text("Activo no encontrado")
            ],
        )

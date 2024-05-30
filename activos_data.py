import flet as ft

activos = []

columns = [
    ft.DataColumn(ft.Text("Identificador")),
    ft.DataColumn(ft.Text("Nombre")),
    ft.DataColumn(ft.Text("Responsable")),
    ft.DataColumn(ft.Text("Valor")),
    ft.DataColumn(ft.Text("Valor residual")),
    ft.DataColumn(ft.Text("Vida util")),
    ft.DataColumn(ft.Text("Detalles")),
]

data_table = ft.DataTable(columns=columns, rows=[])

def detalles_click(e):
    ft.Text(f"Detalle de la devaluacion del activo: {e.control.data['identificador']}, {e.control.data['nombre']}")
    ft.Divider(),
    anos = e.control.data['vida_util']
    valor = e.control.data['valor']
    valor_res = e.control.data['valor_res']
    vida_util = e.control.data['vida_util']
    _columns = [
        ft.DataColumn(ft.Text("Periodo")),
        ft.DataColumn(ft.Text("Valor a depreciar")),
        ft.DataColumn(ft.Text("Factor")),
        ft.DataColumn(ft.Text("Depreciacion anual")),
        ft.DataColumn(ft.Text("Depreciacion acumulada")),
        ft.DataColumn(ft.Text("Valor en libros")),
    ]

    _rows = []
    i = 0
    while i < anos:
        _row = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(f"{i}")),
                ft.DataCell(ft.Text(f"{i}")),
            ]
        )
        _rows.append(_row)
        i += 1

    _data_table = ft.DataTable(columns=_columns, rows=_rows)

def actualizar_tabla():
    global activos

    data_table.rows.clear()

    for item in activos:
        row = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(item["identificador"])),
                ft.DataCell(ft.Text(item["nombre"])),
                ft.DataCell(ft.Text(item["responsable"])),
                ft.DataCell(ft.Text(item["valor"])),
                ft.DataCell(ft.Text(item["valor_res"])),
                ft.DataCell(ft.Text(item["vida_util"])),
                ft.DataCell(ft.ElevatedButton(text="Detalles", on_click=detalles_click, data=item)),
            ]
        )
        data_table.rows.append(row)

def agregar_activo(tf_identificador, tf_nombre, tf_responsable, tf_valor, tf_valor_res, tf_vida_util, page):
    global activos
    activo = {
        "identificador": tf_identificador.value,
        "nombre": tf_nombre.value,
        "responsable": tf_responsable.value,
        "valor": tf_valor.value,
        "valor_res": tf_valor_res.value,
        "vida_util": tf_vida_util.value
    }
    activos.append(activo)
    tf_identificador.value = ""
    tf_nombre.value = ""
    tf_responsable.value = ""
    tf_valor.value = ""
    tf_valor_res.value = ""
    tf_vida_util.value = ""
    page.show_snack_bar(ft.SnackBar(content=ft.Text("Activo agregado!!!")))
    actualizar_tabla()
    page.update()

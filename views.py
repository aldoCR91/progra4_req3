import flet as ft
from activos_data import data_table, agregar_activo

tf_identificador = ft.TextField(label="Identificador", width=400, keyboard_type=ft.KeyboardType.NUMBER, value="")
tf_nombre = ft.TextField(label="Nombre", width=400)
tf_responsable = ft.TextField(label="Responsable", width=400)
tf_valor = ft.TextField(label="Valor monetario", width=400, keyboard_type=ft.KeyboardType.NUMBER, value="")
tf_valor_res = ft.TextField(label="Valor de rescate", width=400, keyboard_type=ft.KeyboardType.NUMBER, value="")
tf_vida_util = ft.TextField(label="Vida util (years)", width=400, keyboard_type=ft.KeyboardType.NUMBER, value="")

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
    columns2=[
        ft.DataColumn(ft.Text("Periodo")),
        ft.DataColumn(ft.Text("Valor a depreciar")),
        ft.DataColumn(ft.Text("Factor")),
        ft.DataColumn(ft.Text("Denominador")),
        ft.DataColumn(ft.Text("Depreciacion anual")),
        ft.DataColumn(ft.Text("Depreciacion acumulada")),
        ft.DataColumn(ft.Text("Valor en libros")),
    ]
    rows = []
    i = 0
    
    while i <= int(data['vida_util']):
        if i == 0:
            row = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(f"{i}")),   # Periodo
                    ft.DataCell(ft.Text(f"{valor - valor_res}")), # Valor a depreciar
                    ft.DataCell(ft.Text(f"-")), # Factor
                    ft.DataCell(ft.Text(f"-")), #Depreciacion anual
                    ft.DataCell(ft.Text(f"-")), #Depreciacion acumulada
                    ft.DataCell(ft.Text( f"{int((valor - valor_res) - (i * ((valor - valor_res)/vida_util) ))}")), # Valor en libros
                ]
            )
        if i > 0:
            row = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(f"{i}")),   # Periodo
                    ft.DataCell(ft.Text(f"{valor - valor_res}")), # Valor a depreciar
                    ft.DataCell(ft.Text(f"{int((100 / vida_util))}%")), # Factor
                    ft.DataCell(ft.Text(f"{int((valor - valor_res)/(vida_util))}")), #Depreciacion anual
                    ft.DataCell(ft.Text(f"{int( i * ( (valor - valor_res)/10))}")), #Depreciacion acumulada
                    ft.DataCell(ft.Text( f"{int((valor - valor_res) - (i * ((valor - valor_res)/vida_util) ))}")), # Valor en libros
                ]
            )
        if i == vida_util:
            row = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(f"{i}")),   # Periodo
                    ft.DataCell(ft.Text(f"{valor - valor_res}")), # Valor a depreciar
                    ft.DataCell(ft.Text(f"{int((100 / vida_util))}%")), # Factor
                    ft.DataCell(ft.Text(f"{int((valor - valor_res)/(vida_util))}")), #Depreciacion anual
                    ft.DataCell(ft.Text(f"{int( i * ( (valor - valor_res)/10))}")), #Depreciacion acumulada
                    ft.DataCell(ft.Text(f"-" )), # Valor en libros
                ]
        )
        rows.append(row)
        i = i + 1

    def denominador(vida_util:int):
        vida = vida_util
        fac = 0
        while vida > 0:
            fac = fac + vida
            vida = vida - 1
        return fac
    
    _periodo = 0
    _valor_adepreciar = valor - valor_res
    _factor = vida_util
    _denominador = denominador(vida_util)
    _dep_anual = 0
    _dep_acumulada = 0
    _valor_libros = _valor_adepreciar
    print(f"valor en libros: {_valor_libros}")

    i = vida_util
    rows2 = []

    while i >= 0:
        
        if _periodo == 0:
            _valor_libros = _valor_adepreciar
            row = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(f"{_periodo}")),   # Periodo
                    ft.DataCell(ft.Text(f"{_valor_adepreciar}")), # Valor a depreciar
                    ft.DataCell(ft.Text(f"-")), # Factor
                    ft.DataCell(ft.Text(f"-")), # Denominador
                    ft.DataCell(ft.Text(f"-")), #Depreciacion anual
                    ft.DataCell(ft.Text(f"-")), #Depreciacion acumulada
                    ft.DataCell(ft.Text( f"{_valor_libros}")), # Valor en libros
                ]
            )
        if _periodo > 0:
            #_dep_anual = (_valor_adepreciar * 1)
            _dep_anual = round((_valor_adepreciar * _factor)/_denominador)
            _dep_acumulada = _dep_acumulada + _dep_anual
            _valor_libros = _valor_adepreciar - _dep_acumulada
            if _periodo == 10:
                _valor_libros = "0"
            row = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(f"{_periodo}")),   # Periodo
                    ft.DataCell(ft.Text(f"{_valor_adepreciar}")), # Valor a depreciar
                    ft.DataCell(ft.Text(f"{int(_factor)}%")), # Factor
                    ft.DataCell(ft.Text(f"{int(_denominador)}%")), # Denominador
                    ft.DataCell(ft.Text(f"{int(_dep_anual)}")), #Depreciacion anual
                    ft.DataCell(ft.Text(f"{int(_dep_acumulada )}")), #Depreciacion acumulada
                    ft.DataCell(ft.Text( f"{int(_valor_libros)}")), # Valor en libros
                ]
            )
            _factor = _factor - 1

        rows2.append(row)
        _periodo = _periodo + 1
        i = i - 1
        
    lv1 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    lv1.controls.append(ft.Text(f"Edwards LTDA", size=14, weight=ft.FontWeight.BOLD))
    lv1.controls.append(ft.Text("Depreciacion Linea Recta", size=14, weight=ft.FontWeight.BOLD))
    lv1.controls.append(ft.Divider())
    lv1.controls.append(ft.DataTable(columns=columns, rows=rows))
    lv1.controls.append(ft.Divider())
    lv1.controls.append(ft.Text(f"Edwards LTDA", size=14, weight=ft.FontWeight.BOLD))
    lv1.controls.append(ft.Text("Depreciacion Suma de digitos", size=14, weight=ft.FontWeight.BOLD))
    lv1.controls.append(ft.Divider())
    lv1.controls.append(ft.DataTable(columns=columns2,rows=rows2 ))
    
    

    

    



    
    
    if activo:
        return ft.View(
            "/detail",
            controls=[
                app_bar,
                ft.Row([menubar]),
                ft.Text(f"Edwards LTDA", size=14, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                ft.Text(f"{nombre}:                 {valor}"),
                ft.Text(f"Valor de rescate:     {valor_res}"),
                ft.Text(f"Vida util:            {vida_util}"),
                ft.Text(f"Responsable:            {responsable}"),
                ft.Divider(),
                lv1,
                #ft.DataTable(columns=columns, rows=rows),
                
                
                
                
                
            ],
            auto_scroll=True,
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
#import flet as ft
import threading
#from time import sleep
from models.activo import Activo_Model






activos:Activo_Model = []

# Clase que herede de thred
class Activo_Controller(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.activos = activos
    
    def calc_depreciacion_lineal(self, activo: Activo_Model):
        datos = []
        dato = {
            "periodo": int,
            "valor_a_depreciar": float,
            "factor": int,
            "depreciacion_anual": float,
            "depreciacion_acumulada": float,
            "valor_en_libros": int
            }
        
        periodo = 0
        
        if periodo == 0:
            dato["periodo"] = 0
            dato["valor_a_depreciar"] = activo.get_valor() - activo.get_val_res()
            dato["factor"] = int( 100 / activo.get_vida_util() )
            dato["depreciacion_anual"] = 0
            dato["depreciacion_acumulada"] = 0
            dato["valor_en_libros"] = dato["valor_a_depreciar"]
            datos.append(dato)
            dato["periodo"] = dato["periodo"] + 1
        if periodo > 0:
            dato
            
            
        
        valor_a_depreciar = activo.get_valor() - activo.get_val_res()
        factor = int( 100 / activo.get_vida_util() )
        depreciacion_anual = 0
        depreciacion_acumulada = 0
        valor_en_libros = valor_a_depreciar
        
        
        
        
print ('Soy el hilo principal')
for i in range(0,6):
    t = Hilo(i)
    t.start()
    t.join()




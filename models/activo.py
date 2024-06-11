class Activo_Model:
    
    # Constructor de la clase
    def __init__(self, nombre: str, valor: float , val_res: float, vida_util: int) -> None:
        self.nombre = nombre
        self.valor = valor
        self.val_res = val_res
        self.vida_util = vida_util
        
    def set_nombre(self, nombre: str) -> None:
        self.nombre = nombre
        
    def set_valor(self, valor: float) -> None:
        self.valor = valor
        
    def set_val_res(self, val_res: float) -> None:
        self.val_res = val_res
        
    def set_vida_util(self, vida_util: int) -> None:
        self.vida_util = vida_util
    
    def get_nombre(self):
        return self.nombre
    
    def get_valor(self):
        return self.valor
    
    def get_val_res(self):
        return self.val_res
    
    def get_vida_util(self):
        return self.vida_util
    
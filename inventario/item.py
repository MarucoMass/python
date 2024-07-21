class Item:
    def __init__(self, nombre: str, nivel_minimo_requerido: int):
        self._nombre = nombre
        self._nivel_minimo_requerido = nivel_minimo_requerido
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def nivel_minimo_requerido(self):
        return self._nivel_minimo_requerido

    def __str__(self):
        return f'Item(nombre={self.nombre}, nivel_minimo_requerido={self.nivel_minimo_requerido})'

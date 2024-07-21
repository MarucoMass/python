from inventario import Inventario
from item import Item

class Personaje:

    __lista_valores = []

    def __init__(self, nombre: str, inventario: Inventario):
        self.__nombre = Personaje.__valor_unico(nombre)
        self.__cantidad_puntos_nivel = 1
        self.__inventario = inventario
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def cantidad_puntos_nivel(self):
        return self.__cantidad_puntos_nivel
    
    @property
    def inventario(self):
        return self.__inventario
    
    def agregar_item_inventario(self, item: Item):
        if self.cantidad_puntos_nivel >= item.nivel_minimo_requerido:
            self.inventario.agregar_item(item)
        else:
            raise ValueError("Nivel insuficiente para agregar el item.")
    
    def arrojar_item_inventario(self, item: Item):
        self.inventario.arrojar_item(item)
    
    def __str__(self):
        return f'Personaje(nombre={self.nombre}, cantidad_puntos_nivel={self.cantidad_puntos_nivel})'
    
    @classmethod
    def __valor_unico(cls, value):
        if (value in cls.__lista_valores):
            raise Exception("El valor está repetido")
        cls.__lista_valores.append(value)
        return value

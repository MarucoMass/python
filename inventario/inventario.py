from item import Item

class Inventario:
    def __init__(self):
        self.__items: list = []
    
    @property
    def cantidad_items(self):
        return len(self.items)
    
    @property
    def items(self):
        return self.__items
    
    def agregar_item(self, item: Item):
        self.items.append(item)

    
    def arrojar_item(self, item: Item):
        self.items.remove(item)
    
    def __str__(self):
        return f'Inventario(cantidad_items={self.cantidad_items})'

from inventario import Inventario
from item import Item
from personaje import Personaje

item1 = Item(nombre="Espada", nivel_minimo_requerido=1)
item2 = Item(nombre="Escudo", nivel_minimo_requerido=2)
item3 = Item(nombre="Casco", nivel_minimo_requerido=1)

inventario = Inventario()
inventario.agregar_item(item1)
inventario.agregar_item(item2)

    

personaje = Personaje("Héroe", inventario)


personaje.agregar_item_inventario(item3)
try:
    personaje.agregar_item_inventario(item2)
except ValueError as e:
    print(e)


print(personaje)
print(personaje.inventario)


personaje.arrojar_item_inventario(item1)
print(personaje.inventario)
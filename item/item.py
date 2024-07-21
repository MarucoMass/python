from typing import List, Self

class Item:
    def __init__(self, nombre: str, descripcion: str):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__cantidad_items_generado_receta = 0
        self.__ingredientes_receta: List[Self] = []

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, value: str):
        self.__nombre = value

    @property
    def descripcion(self) -> str:
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, value: str):
        self.__descripcion = value

    @property
    def cantidad_items_generado_receta(self) -> int:
        return self.__cantidad_items_generado_receta

    @cantidad_items_generado_receta.setter
    def cantidad_items_generado_receta(self, value: int):
        self.__cantidad_items_generado_receta = value

    @property
    def cantidad_ingredientes_distintos(self) -> int:
        return len(set(self.__ingredientes_receta))

    @property
    def ingredientes_receta(self) -> list:
        return sorted(self.__ingredientes_receta, key=lambda x: x.nombre, reverse=True)

    def __str__(self):
        return (f"Item(nombre={self.nombre}, descripcion={self.descripcion}, "
                f"cantidad_items_generado_receta={self.cantidad_items_generado_receta}, "
                f"cantidad_ingredientes_distintos={self.cantidad_ingredientes_distintos})")

    def add_ingrediente(self, item:Self):
        self.__ingredientes_receta.append(item)

    def remove_ingrediente(self, item:Self):
        self.__ingredientes_receta.remove(item)

    def generar_item(self, ingredientes: List[Self]) -> int:

        ingredientes_receta_set = set(self.ingredientes_receta)
        ingredientes_set = set(ingredientes)

        if ingredientes_set == ingredientes_receta_set:
            self.cantidad_items_generado_receta += 1
            return self.cantidad_items_generado_receta
        else:
            raise ValueError("Los ingredientes no coinciden con la receta")
        


ingrediente1 = Item("Azúcar", "Azúcar refinada")
ingrediente2 = Item("Harina", "Harina de trigo")
ingrediente3 = Item("Huevos", "Huevos frescos")
ingrediente4 = Item("Manteica", "Manteca fresca")


receta = Item("Pastel", "Pastel de chocolate")
receta.add_ingrediente(ingrediente1)
receta.add_ingrediente(ingrediente2)
receta.add_ingrediente(ingrediente3)


ingredientes_para_generar = [ingrediente1, ingrediente2, ingrediente3]

try:
    cantidad_generada = receta.generar_item(ingredientes_para_generar)
    print(f"Cantidad de items generados: {cantidad_generada}")
except ValueError as e:
    print(e)

for i in receta.ingredientes_receta:
    print(i)
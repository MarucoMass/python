
class Direccion:
    def __init__(self, direccion: str):
        self.__direccion = direccion

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion: str):
        self.__direccion = direccion

    def calcular_costo_envio(self) -> float:
        raise NotImplementedError("Este método debe ser implementado por una subclase")

    def __str__(self):
        return f'Direccion(direccion={self.direccion})'

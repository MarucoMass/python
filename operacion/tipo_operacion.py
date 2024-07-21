class TipoOperacion:
    def __init__(self, nombre: str):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    def __str__(self):
        return f'TipoOperacion(nombre={self.__nombre})'

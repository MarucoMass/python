class Archivo:

    __lista_valores = []

    def __init__(self, nombre: str, peso_kb: int):
        self.__nombre = Archivo.__valor_unico(nombre)
        self.__peso_kb = peso_kb

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def peso_kb(self):
        return self.__peso_kb

    @peso_kb.setter
    def peso_kb(self, peso_kb: int):
        self.__peso_kb = peso_kb

    def copiar_archivo(self):
        return Archivo(f"{self.nombre}_copia", self.peso_kb)

    def __str__(self):
        return f'Archivo(nombre={self.__nombre}, peso_kb={self.__peso_kb})'

    @classmethod
    def __valor_unico(cls, value):
        if (value in cls.__lista_valores):
            raise Exception("El valor está repetido")
        cls.__lista_valores.append(value)
        return value
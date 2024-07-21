class Activo:

    __lista_valores = []

    def __init__(self, nombre: str, simbolo: str, comision_en_porcentaje: float):
        self.__nombre = nombre
        self.__simbolo = Activo.__valor_unico(simbolo)
        self.__comision_en_porcentaje = comision_en_porcentaje

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def simbolo(self):
        return self.__simbolo

    @simbolo.setter
    def simbolo(self, simbolo: str):
        self.__simbolo = simbolo

    @property
    def comision_en_porcentaje(self):
        return self.__comision_en_porcentaje

    @comision_en_porcentaje.setter
    def comision_en_porcentaje(self, comision_en_porcentaje: float):
        self.__comision_en_porcentaje = comision_en_porcentaje

    def __str__(self):
        return (f'Activo(nombre={self.nombre}, simbolo={self.simbolo}, '
                f'comision_en_porcentaje={self.comision_en_porcentaje})')


    @classmethod
    def __valor_unico(cls, value):
        if (value in cls.__lista_valores):
            raise Exception("El valor está repetido")
        cls.__lista_valores.append(value)
        return value
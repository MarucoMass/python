from direccion import Direccion

class Cliente:

    __lista_valores = []   

    def __init__(self, apellido: str, nombre: str, email: str, direccion: Direccion):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__email = Cliente.__valor_unico(email)
        self.__direccion = direccion

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido: str):
        self.__apellido = apellido

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def email(self):
        return self.__email

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion: Direccion):
        self.__direccion = direccion

    def __str__(self):
        return f'Cliente(apellido={self.apellido}, nombre={self.nombre}, email={self.email}, direccion={self.direccion})'

    
    @classmethod
    def __valor_unico(cls, value):
        if (value in cls.__lista_valores):
            raise Exception("El valor está repetido")
        cls.__lista_valores.append(value)
        return value
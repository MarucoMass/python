from clienteFrecuente import ClienteFrecuente

class Cliente:
    def __init__(self, nombre:str, apellido: str, clienteFrecuente:ClienteFrecuente = None):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cliente_frecuente = clienteFrecuente


    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, new_apellido):
        self.__apellido = new_apellido

    @property
    def cliente_frecuente(self):
        return self.__cliente_frecuente

    def asociar_cliente_frecuente(self, cliente_frecuente: ClienteFrecuente):
        self.__cliente_frecuente = cliente_frecuente

    @property
    def es_cliente_frecuente(self):
        return self.cliente_frecuente is not None


    def nueva_compra(self, monto: float):
        if self.es_cliente_frecuente:
            self.cliente_frecuente.add_puntos(monto)
        else:
            raise Exception("No se puede hacer la compra porque no es un cliente frecuente")
from datetime import date
from tipo_operacion import TipoOperacion
from activo import Activo

class Operacion:
    __nro_counter = int(0) 

    def __init__(self, fecha_orden: date, cantidad_operada: int, precio_operado: float, 
                 tipo_operacion: TipoOperacion, activo: Activo, en_proceso: bool = True):
        self.__nro = Operacion.__autoincrementar_nro()
        self.__fecha_orden = fecha_orden
        self.__cantidad_operada = cantidad_operada
        self.__precio_operado = precio_operado
        self.__tipo_operacion = tipo_operacion
        self.__activo = activo
        self.__en_proceso = en_proceso

    @property
    def nro(self):
        return self.__nro

    @property
    def fecha_orden(self):
        return self.__fecha_orden

    @fecha_orden.setter
    def fecha_orden(self, fecha_orden: date):
        self.__fecha_orden = fecha_orden

    @property
    def en_proceso(self):
        return self.__en_proceso

    @en_proceso.setter
    def en_proceso(self, en_proceso: bool):
        self.__en_proceso = en_proceso

    @property
    def cantidad_operada(self):
        return self.__cantidad_operada

    @cantidad_operada.setter
    def cantidad_operada(self, cantidad_operada: int):
        self.__cantidad_operada = cantidad_operada
        self.__monto_operado = self.__calcular_monto_operado()

    @property
    def precio_operado(self):
        return self.__precio_operado

    @precio_operado.setter
    def precio_operado(self, precio_operado: float):
        self.__precio_operado = precio_operado
        self.__monto_operado = self.__calcular_monto_operado()

    @property
    def tipo_operacion(self):
        return self.__tipo_operacion

    @tipo_operacion.setter
    def tipo_operacion(self, tipo_operacion: TipoOperacion):
        self.__tipo_operacion = tipo_operacion

    @property
    def activo(self):
        return self.__activo

    @activo.setter
    def activo(self, activo: Activo):
        self.__activo = activo

    @property
    def monto_operado(self):
        return (self.cantidad_operada * self.precio_operado) * (1 + self.activo.comision_en_porcentaje / 100)

    def __str__(self):
        return (f'Operacion(nro={self.nro}, fecha_orden={self.fecha_orden}, en_proceso={self.en_proceso}, '
                f'cantidad_operada={self.cantidad_operada}, precio_operado={self.precio_operado}, '
                f'tipo_operacion={self.tipo_operacion}, activo={self.activo}, '
                f'monto_operado={self.monto_operado})')

    @classmethod
    def __autoincrementar_nro(cls):
        cls.__nro_counter += 1
        return cls.__nro_counter
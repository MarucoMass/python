class TipoMovimiento():

    def __init__(self, nombre : str, parking_en_dias: int) -> None:
        self.__nombre = nombre
        self.__parking_en_dias = parking_en_dias

    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def parking_en_dias(self):
        return self.__parking_en_dias
    @parking_en_dias.setter
    def parking_en_dias(self, parking_en_dias):
        self.__parking_en_dias = parking_en_dias
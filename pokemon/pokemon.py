class Pokemon:
    __nro_counter = int(0) 

    def __init__(self, nombre: str):
        self.__nro = Pokemon.__autoincrementar_nro()
        self.__nombre = nombre

    @property
    def nro(self):
        return self.__nro

    @property
    def nombre(self):
        return self.__nombre

    def __str__(self):
        return f'Pokemon(nro={self.nro}, nombre={self.nombre})'
    

    @classmethod
    def __autoincrementar_nro(cls):
        cls.__nro_counter += 1
        return cls.__nro_counter

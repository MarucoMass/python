from pokedex import Pokedex

class Personaje:
    def __init__(self, nombre: str, pokedex: Pokedex = None):
        self.__nombre = nombre
        self.__pokedex = pokedex

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def pokedex(self):
        return self.__pokedex
    @pokedex.setter
    def pokedex(self, value):
        self.__pokedex = value
    
    @property
    def es_entrenador_pokemon(self) -> bool:
        return self.pokedex is not None


    def __str__(self):
        if self.es_entrenador_pokemon:
            return f'Personaje(nombre={self.nombre}, cantidad_pokemones={self.pokedex.cantidad_pokemones})'
        else:
            return f'Personaje(nombre={self.nombre})'

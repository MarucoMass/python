from pokemon import Pokemon

class Pokedex:

    __lista_valores = []

    def __init__(self, nro: int):
        self.__nro = Pokedex.__valor_unico(nro)
        self.__pokemones = []

    @property
    def nro(self):
        return self.__nro

    @property
    def cantidad_pokemones(self):
        return len(self.pokemones)
    @property
    def pokemones(self):
        return sorted(self.__pokemones, key=lambda x: x.nro)

    def capturar_pokemon(self, pokemon: Pokemon):
        self.__pokemones.append(pokemon)

    def liberar_pokemon(self, pokemon: Pokemon):
        self.__pokemones.remove(pokemon)

    def __str__(self):
        return f'Pokedex(nro={self.nro}, cantidad_pokemones={self.cantidad_pokemones})'

    
    @classmethod
    def __valor_unico(cls, value):
        if (value in cls.__lista_valores):
            raise Exception("El valor está repetido")
        cls.__lista_valores.append(value)
        return value

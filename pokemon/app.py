from pokemon import Pokemon
from pokedex import Pokedex
from personaje import Personaje

pikachu = Pokemon(nombre="Pikachu")
charmander = Pokemon(nombre="Charmander")

# Crear una pokedex y capturar pokemones
pokedex = Pokedex(123)
pokedex.capturar_pokemon(pikachu)
pokedex.capturar_pokemon(charmander)

# Crear un personaje y asignarle una pokedex
ash = Personaje("Ash Ketchum", pokedex)

# Mostrar el personaje y su pokedex
print(ash)
print(ash.pokedex.pokemones)
for pokemon in ash.pokedex.pokemones:
    print(pokemon)

# Liberar un pokemon y mostrar la pokedex actualizada
ash.pokedex.liberar_pokemon(pikachu)
print(ash.pokedex)
for pokemon in ash.pokedex.pokemones:
        print(pokemon)

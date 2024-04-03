#Camilo Castillo. cc 1.002.245.758
import random

# Clase que representa un Pokémon
class Pokemon:
    def __init__(self, nombre, salud, ataques):
        self.nombre = nombre
        self.salud = salud
        self.ataques = ataques

    def atacar(self, objetivo):
        # Selección de un ataque aleatorio
        ataque = random.choice(self.ataques)
        # Aplicar el daño del ataque al objetivo
        objetivo.recibir_daño(ataque.daño)
        print(f"{self.nombre} usó {ataque.nombre} contra {objetivo.nombre}")
        print(f"{objetivo.nombre} ahora tiene {objetivo.salud} de salud.\n")  # Mostrar salud del objetivo después del ataque

    def recibir_daño(self, daño):
        # Reducir la salud del Pokémon según el daño recibido
        self.salud -= daño
        if self.salud < 0:
            self.salud = 0

    def esta_vivo(self):
        # Verificar si el Pokémon está vivo (salud > 0) (pd: si esto esta en salud >= 0 se queda como un ciclo)
        return self.salud > 0

# Clase que representa un equipo de Pokémon
class EquipoPokemon:
    def __init__(self):
        self.pokemones = []

    def agregar_pokemon(self, pokemon):
        # Agregar un Pokémon al equipo
        if len(self.pokemones) < 3:
            self.pokemones.append(pokemon)
        else:
            print("El equipo está completo, no se puede agregar más Pokémon.")

    def esta_vivo(self):
        # Verifica si al menos un Pokémon del equipo está vivo
        return any(pokemon.esta_vivo() for pokemon in self.pokemones)

    def obtener_pokemon_vivo(self):
        # Obtener el primer Pokémon del equipo que esté vivo
        for pokemon in self.pokemones:
            if pokemon.esta_vivo():
                return pokemon
        return None

# Simulador una batalla Pokémon
def simular_batalla(equipo1, equipo2, estrategia1, estrategia2):
    print("¡Comienza la batalla Pokémon!")
    
    while equipo1.esta_vivo() and equipo2.esta_vivo():
        # Turno del equipo 1
        pokemon1 = equipo1.obtener_pokemon_vivo()
        if pokemon1:
            pokemon2 = equipo2.obtener_pokemon_vivo()
            if pokemon2:
                estrategia1.atacar(pokemon1, pokemon2)
            else:
                print("¡El equipo 2 no puede continuar!")
                break
        else:
            print("¡El equipo 1 no puede continuar!")
            break

        # Turno del equipo 2
        pokemon2 = equipo2.obtener_pokemon_vivo()
        if pokemon2:
            pokemon1 = equipo1.obtener_pokemon_vivo()
            if pokemon1:
                estrategia2.atacar(pokemon2, pokemon1)
            else:
                print("¡El equipo 1 no puede continuar!")
                break
        else:
            print("¡El equipo 2 no puede continuar!")
            break

    if equipo1.esta_vivo():
        print("¡El equipo 1 es el ganador!")
    elif equipo2.esta_vivo():
        print("¡El equipo 2 es el ganador!")
    else:
        print("¡Ha sido un empate!")

# Clase que representa un ataque
class Ataque:
    def __init__(self, nombre, daño):
        self.nombre = nombre
        self.daño = daño

# Clase base para las estrategias de ataque
class EstrategiaAtaque:
    def atacar(self, pokemon, oponente):
        raise NotImplementedError

# Estrategia de ataque aleatorio
class EstrategiaAtaqueAleatorio(EstrategiaAtaque):
    def atacar(self, pokemon, oponente):
        pokemon.atacar(oponente)

# Estrategia de ataque por selección del usuario
class EstrategiaAtaqueUsuario(EstrategiaAtaque):
    def atacar(self, pokemon, oponente):
        print(f"Es tu turno, elige el ataque para {pokemon.nombre}:")
        for i, ataque in enumerate(pokemon.ataques):
            print(f"{i + 1}. {ataque.nombre}")
        opcion = int(input("Selecciona el número del ataque: ")) - 1
        if opcion >= 0 and opcion < len(pokemon.ataques):
            pokemon.ataques[opcion].daño

# Definición de los Pokémon y sus ataques
# Todos los ataques de los pokemones son basados en sus stats oficiales de potencia y vida a nivel 100.
pikachu = Pokemon("Pikachu", 211, [
    Ataque("Impactrueno", 40),
    Ataque("Rayo", 110),
    Ataque("Ataque Rápido", 40),
    Ataque("Placaje", 40)
])

caterpie = Pokemon("Caterpie", 231, [
    Ataque("Placaje", 40),
    Ataque("Tacleada", 45),
    Ataque("Supersónico", 55),
    Ataque("Drenadoras", 35)
])
Pidgeotto = Pokemon("Pidgeotto", 267, [
    Ataque("Picotazo", 35),
    Ataque("Remolino", 40),
    Ataque("Tornado", 60),
    Ataque("Ataque Rápido", 40)
])

Bulbasaur = Pokemon("Bulbasaur", 231, [
    Ataque("Látigo Cepa", 45),
    Ataque("Drenadoras", 80),
    Ataque("Placaje", 40),
    Ataque("Somnífero", 0)  # Supongo que el ataque Somnífero no tiene potencia de daño en este contexto
])

Charmander = Pokemon("Charmander", 219, [
    Ataque("Lanzallamas", 95),
    Ataque("Gruñido", 0),  # Supongo que el ataque Gruñido no tiene potencia de daño en este contexto
    Ataque("Arañazo", 40),
    Ataque("Ascuas", 40)
])

Squirtle = Pokemon("Squirtle", 229, [
    Ataque("Pistola Agua", 40),
    Ataque("Burbuja", 40),
    Ataque("Ataque Rápido", 40),
    Ataque("Placaje", 40)
])

Krabby = Pokemon("Krabby", 201, [
    Ataque("Burbuja", 40),
    Ataque("Rayo Burbuja", 65),
    Ataque("Placaje", 40),
    Ataque("Tajo Cruzado", 75)
])

Raticate = Pokemon("Raticate", 251, [
    Ataque("Hipercolmillo", 80),
    Ataque("Ataque Rápido", 40),
    Ataque("Placaje", 40),
    Ataque("Golpe Cabeza", 70)
])

Muk = Pokemon("Muk", 351, [
    Ataque("Lodo", 65),
    Ataque("Bomba Lodo", 90),
    Ataque("Ataque Ácido", 40),
    Ataque("Infortunio", 0)  # Supongo que el ataque Infortunio no tiene potencia de daño en este contexto
])

Kingler = Pokemon("Kingler", 251, [
    Ataque("Hidropulso", 110),
    Ataque("Rayo Burbuja", 65),
    Ataque("Rayo", 65),
    Ataque("Placaje", 40)
])

# Definición de los equipos
equipo1 = EquipoPokemon()
equipo1.agregar_pokemon(pikachu)
equipo1.agregar_pokemon(Charmander)
equipo1.agregar_pokemon(Kingler)

equipo2 = EquipoPokemon()
equipo2.agregar_pokemon(Muk)
equipo2.agregar_pokemon(Squirtle)
equipo2.agregar_pokemon(Bulbasaur)


# Estrategias de ataque
estrategia_aleatoria = EstrategiaAtaqueAleatorio()
estrategia_usuario = EstrategiaAtaqueUsuario()

# Simular batalla
# Si hay 1 o 2 jugadores, cambiar estrategia_aleatoria por estrategia_usuario
simular_batalla(equipo1, equipo2, estrategia_aleatoria, estrategia_aleatoria)

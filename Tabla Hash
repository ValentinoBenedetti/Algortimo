class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __repr__(self):
        return f"Pokemon(nombre={self.nombre}, nivel={self.nivel}, tipo={self.tipo}, subtipo={self.subtipo})"

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key, value):
        index = key % self.size
        self.table[index].append(value)

    def get(self, key):
        index = key % self.size
        return self.table[index]

    def get_all(self):
        return [item for sublist in self.table for item in sublist]

# Crear las tres tablas hash
tipo_hash = HashTable(10)
digito_hash = HashTable(10)
nivel_hash = HashTable(10)

pokemons = [
    {"nombre": "Pikachu", "nivel": 35, "tipo": "Eléctrico", "subtipo": None},
    {"nombre": "Charizard", "nivel": 40, "tipo": "Fuego", "subtipo": "Volador"},
    {"nombre": "Bulbasaur", "nivel": 30, "tipo": "Planta", "subtipo": "Veneno"},
    {"nombre": "Starmie", "nivel": 30, "tipo": "Agua", "subtipo": "Psíquico"},
    {"nombre": "Psyduck", "nivel": 25, "tipo": "Agua", "subtipo": None},
    {"nombre": "Gyarados", "nivel": 35, "tipo": "Agua", "subtipo": "Volador"},
    {"nombre": "Onix", "nivel": 38, "tipo": "Roca", "subtipo": "Tierra"},
    {"nombre": "Geodude", "nivel": 28, "tipo": "Roca", "subtipo": "Tierra"},
    {"nombre": "Vulpix", "nivel": 20, "tipo": "Fuego", "subtipo": None},
    {"nombre": "Blastoise", "nivel": 50, "tipo": "Agua", "subtipo": None},
    {"nombre": "Umbreon", "nivel": 45, "tipo": "Siniestro", "subtipo": None},
    {"nombre": "Nidoking", "nivel": 40, "tipo": "Veneno", "subtipo": "Tierra"}
]

for p in pokemons:
    pokemon = Pokemon(p["nombre"], p["nivel"], p["tipo"], p["subtipo"])

    # Insertar en la tabla hash por tipo
    tipo_hash.insert(hash(pokemon.tipo), pokemon)
    if pokemon.subtipo:
        tipo_hash.insert(hash(pokemon.subtipo), pokemon)

    # Insertar en la tabla hash por último dígito del nivel
    digito_hash.insert(pokemon.nivel % 10, pokemon)

    # Insertar en la tabla hash por nivel
    nivel_hash.insert(pokemon.nivel // 10, pokemon)

# Mostrar todos los Pokémon cuyos niveles terminan en 3, 7 y 9
print("\n E- Pokémons cuyos niveles terminan en 3, 7 y 9:")
for digito in [3, 7, 9]:
    for pokemon in digito_hash.get(digito):
        print(pokemon)

# Mostrar todos los Pokémon cuyos niveles son múltiplos de 2, 5 y 10
print("\n F- Pokémons cuyos niveles son múltiplos de 2, 5 y 10:")
for pokemon in nivel_hash.get_all():
    if pokemon.nivel % 2 == 0 or pokemon.nivel % 5 == 0:
        print(pokemon)

# Mostrar todos los Pokémon de los siguientes tipos: Acero, Fuego, Eléctrico, Hielo
print("\n G- Pokémons de los tipos Acero, Fuego, Eléctrico, Hielo:")
for tipo in ["Acero", "Fuego", "Eléctrico", "Hielo"]:
    for pokemon in tipo_hash.get(hash(tipo)):
        print(pokemon)

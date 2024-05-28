# defino la pila con los personajes de Marvel
pila_mcu = [
    {"nombre": "Iron Man", "peliculas": 10},
    {"nombre": "Captain America", "peliculas": 9},
    {"nombre": "Thor", "peliculas": 8},
    {"nombre": "Hulk", "peliculas": 6},
    {"nombre": "Black Widow", "peliculas": 7},
    {"nombre": "Hawkeye", "peliculas": 5},
    {"nombre": "Groot", "peliculas": 5},
    {"nombre": "Rocket Raccoon", "peliculas": 5},
    {"nombre": "Doctor Strange", "peliculas": 4},
    {"nombre": "Spider-Man", "peliculas": 5}
]

# a- posición de Rocket Raccoon y Groot
def posicion_personaje(pila, nombre_personaje):
    for i, personaje in enumerate(reversed(pila), start=1):
        if personaje["nombre"] == nombre_personaje:
            return i
    return None

pos_rocket = posicion_personaje(pila_mcu, "Rocket Raccoon")
pos_groot = posicion_personaje(pila_mcu, "Groot")

# b- personajes que participaron en más de 5 películas
def personajes_mas_de_5_peliculas(pila):
    personajes = [personaje for personaje in pila if personaje["peliculas"] > 5]
    return personajes

personajes_mas_5 = personajes_mas_de_5_peliculas(pila_mcu)

# c. cuantas películas participo Black Widow
def peliculas_black_widow(pila):
    for personaje in pila:
        if personaje["nombre"] == "Black Widow":
            return personaje["peliculas"]
    return 0

peliculas_bw = peliculas_black_widow(pila_mcu)

# d. personajes cuyos nombre empiezan con C, D y G
def personajes_con_letra(pila, letras):
    personajes = [personaje for personaje in pila if personaje["nombre"][0] in letras]
    return personajes

personajes_cdg = personajes_con_letra(pila_mcu, {"C", "D", "G"})

# resultados
print(f"Posición de Rocket Raccoon: {pos_rocket}")
print(f"Posición de Groot: {pos_groot}")

print("Personajes que participaron en más de 5 películas:")
for personaje in personajes_mas_5:
    print(f"{personaje['nombre']} participó en {personaje['peliculas']} películas")

print(f"Black Widow participó en {peliculas_bw} películas")

print("Personajes cuyos nombres empiezan con C, D y G:")
for personaje in personajes_cdg:
    print(personaje["nombre"])

pila_episodio_v = ["Luke Skywalker", "Darth Vader", "Han Solo", "Princesa Leia Organa", "Ben Kenobi", "C3PO", "Emperador Palpatine", "Yoda", "Lando Calrissian", "Boba Fett", "Firmus Piett", "Capitan Needan", "Almirante Ozzel"]
pila_episodio_vii = ["Rey", "Kylo Ren", "Luke Skywalker", "Finn", "Han Solo", "Chewbacca", "Poe Dameron", "Leia Organa", "General Armitage Hux", "C3PO", "Snoke"]

def interseccion_pilas(pila1, pila2):
    conjunto1 = set(pila1)
    conjunto2 = set(pila2)
   
    interseccion = conjunto1.intersection(conjunto2)
    
    return list(interseccion)

personajes_comunes = interseccion_pilas(pila_episodio_v, pila_episodio_vii)

print("Personajes que aparecen en ambos episodios:", personajes_comunes)

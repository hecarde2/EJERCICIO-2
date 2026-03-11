heroes = [
    {"nombre": "Spider-Man", "universo": "Marvel", "poder": "Agilidad", "nivel": 85},
    {"nombre": "Iron Man", "universo": "Marvel", "poder": "Tecnologia", "nivel": 90},
    {"nombre": "Batman", "universo": "DC", "poder": "Inteligencia", "nivel": 88},
    {"nombre": "Superman", "universo": "DC", "poder": "Fuerza", "nivel": 98}
]

print("Lista de héroes:")
for i, heroe in enumerate(heroes):
    print(i, heroe["nombre"], "-", heroe["universo"], "-", heroe["poder"], "- Nivel:", heroe["nivel"])


equipo = []
cantidad = int(input("¿Cuántos héroes quieres en tu equipo? "))

for _ in range(cantidad):
    opcion = int(input("Elige el número del héroe: "))
    equipo.append(heroes[opcion - 1])


print("\nTu equipo:")
for i, h in enumerate(equipo):
    print(i, h["nombre"], "- Nivel:", h["nivel"])

# Contar Marvel y DC en el equipo
marvel = 0
dc = 0

for h in equipo:
    if h["universo"] == "Marvel":
        marvel += 1
    else:
        dc += 1

print("\nHéroes de Marvel en tu equipo:", marvel)
print("Héroes de DC en tu equipo:", dc)

# Nivel total del equipo
nivel_total = sum(h["nivel"] for h in equipo)
print("Nivel total del equipo:", nivel_total)

heroes = [
    {"nombre": "Spider-Man", "universo": "Marvel", "poder": "Agilidad", "nivel": 85},
    {"nombre": "Iron Man", "universo": "Marvel", "poder": "Tecnologia", "nivel": 90},
    {"nombre": "Batman", "universo": "DC", "poder": "Inteligencia", "nivel": 88},
    {"nombre": "Superman", "universo": "DC", "poder": "Fuerza", "nivel": 98}
]

# Mostrar héroes
print("Lista de héroes:")
for i, heroe in enumerate(heroes, start=1):
    print(i, heroe["nombre"], "-", heroe["universo"], "- Nivel:", heroe["nivel"])

# Crear equipo
equipo = []

while True:
    opcion = int(input("Elige el número del héroe (0 para terminar): "))
    
    if opcion == 0:
        break
    
    equipo.append(heroes[opcion - 1])

# Mostrar equipo
print("\nTu equipo:")
for i, h in enumerate(equipo, start=1):
    print(i, h["nombre"], "-", h["universo"], "- Nivel:", h["nivel"])

# Contar Marvel y DC
marvel = 0
dc = 0

for h in equipo:
    if h["universo"] == "Marvel":
        marvel += 1
    else:
        dc += 1

print("\nHéroes de Marvel en tu equipo:", marvel)
print("Héroes de DC en tu equipo:", dc)

# Nivel total
nivel_total = sum(h["nivel"] for h in equipo)
print("Nivel total del equipo:", nivel_total)
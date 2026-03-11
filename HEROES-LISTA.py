heroes = [
    {"nombre": "Spider-Man", "universo": "Marvel", "poder": "Agilidad", "nivel": 85},
    {"nombre": "Iron Man", "universo": "Marvel", "poder": "Tecnologia", "nivel": 90},
    {"nombre": "Batman", "universo": "DC", "poder": "Inteligencia", "nivel": 88},
    {"nombre": "Superman", "universo": "DC", "poder": "Fuerza", "nivel": 98}
]


print("Lista de héroes:")
for i, heroe in enumerate(heroes):
    print(i, heroe["nombre"], "-", heroe["universo"], "- Nivel:", heroe["nivel"])


equipo = []

while True:
    opcion = int(input("Elige el número del héroe (escribe 4 para terminar): "))
    
    if opcion == 4:
        break
    
    if heroes[opcion] in equipo:
        print("ya ingreso ese heroe.")
    else:
        equipo.append(heroes[opcion])



print("\nTu equipo:")
for i, h in enumerate(equipo):
    print(i, h["nombre"], "-", h["universo"], "- Nivel:", h["nivel"])

marvel = 0
dc = 0

for h in equipo:
    if h["universo"] == "Marvel":
        marvel += 1
    else:
        dc += 1

print("\nHéroes de Marvel en tu equipo:", marvel)
print("Héroes de DC en tu equipo:", dc)


nivel_total = sum(h["nivel"] for h in equipo)
print("Nivel total del equipo:", nivel_total)
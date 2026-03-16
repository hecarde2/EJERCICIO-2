print("SALA DE CINE")

fila = {1,2,3,4,5,6,7,8}
columna = {1,2,3,4,5,6,7,8,9,10}
asientos = {}

for f in fila:
    for c in columna:
        asientos[(f,c)] = "O"

opcion = 1

while opcion != 2:

    print("PUESTOS DE LA SALA DE CINE")

    for f in sorted(fila):
        for c in sorted(columna):
            print(asientos[(f,c)], end=" ")
        print()

    print("INGRESE 1 PARA REGISTRAR  ASIENTO")
    print("INGRESE 2 PARA SALIR DEL SISTEMA")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:

        fila_user = int(input("Ingrese la fila donde quiere sentarse (1-8): "))
        columna_user = int(input("Ingrese la columna (1-10): "))

        if asientos[(fila_user, columna_user)] == "O":
            asientos[(fila_user, columna_user)] = "X"
            print("Hizo reserva de asiento")
        else:
            print("Ese asiento ya está ocupado")

    elif opcion == 2:
        print("Gracias por usar la sala de cine")
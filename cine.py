print("cine")
filas = 8
columnas = 10
asientos = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
]
f = True
while f != False:

 for i in asientos:
        print(i)

 asiento_fila = int(input("ingrese la fila de (0-8): "))
 asiento_columna = int(input("ingrese la columna (0-10): "))

 if asiento_fila > 9:
      print("error no existe asiento")
 elif asiento_fila < 0:
      print("error numero no valido")

 if asiento_columna > 10:
      print("error no existe asiento")
 elif asiento_columna < 0:
      print("error numero no valido")
 

 if asientos[asiento_fila][asiento_columna] == 0:
      asientos[asiento_fila][asiento_columna] = "x"
 else:
     print("asiento reservado")
 for i in asientos:
        print(i)
 seguir = int(input(" ingrese 1 para seguir, 2 salir"))
 if seguir == 1:
       f = True
 elif seguir == 2:
      f = False

    


#----------------------------------------- inicio de tablero
filas = 10
columnas = 10

# tablero vacío
tablero = []
for i in range(filas):
    tablero.append([False]*columnas)
    
#----------------------------------------- oscilador de "vida"
# marcamos células vivas
tablero [4] [5] = True
tablero [5] [5] = True
tablero [6] [5] = True
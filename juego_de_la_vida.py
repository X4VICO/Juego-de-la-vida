#----------------------------------------- creamos tablero
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

#----------------------------------------- mostramos tablero
print('Estado inicial')
for y in range(filas):
    for x in range(columnas):
        if tablero [y] [x]:
            print('*', end='')
        else:
            print('.', end='')
    print()
    
#----------------------------------------- pulsos de reloj
pulsos = 6
# creamos nuevo tablero
for t in range(pulsos):
    nuevo=[]
    for i in range(filas):
        nuevo.append([False]*columnas)

#actualizamos el tablero
for y in range(filas):
    for x in range(columnas): # miramos la cantidad de "vida" que hay al rededor de la celda
        n= 0
        if y > 0 and x > 0 and tablero [y-1] [x-1]:
            n += 1
        if x > 0 and tablero [y] [x-1]:
            n += 1
        if y < filas-1 and x > 0 and tablero [y+1] [x-1]:
            n += 1
        if y > 0 and tablero [y-1] [x]:
            n += 1
        if y < filas-1 and tablero [y+1] [x]:
            n += 1
        if y > 0 and x < columnas-1 and tablero [y-1] [x-1]:
            n += 1
        if x < columnas-1 and tablero [y] [x+1]:
            n += 1
        if y < filas-1 and x < columnas-1 and tablero [y+1] [x+1]:
            n +=1
        
        # reglas del juego
        if tablero [y] [x] and (n == 2 or n == 3): # supervivencia
            nuevo [y] [x] = True
        elif not tablero [y] [x] and n == 3: # nacimiento
            nuevo [y] [x] = True
        else: # superpoblación y aislamiento
            nuevo [y] [x] = False

tablero = nuevo
print('Pulso', t+1)
for y in range(filas):
    for x in range(columnas):
        if tablero [y] [x]:
            print('*', end='')
        else:
            print('.', end='')
    print()

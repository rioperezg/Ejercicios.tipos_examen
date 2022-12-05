def bucle(t, n):
    k = int(input("Jugador 1,seleccione 2, 3 o 5 piedras a eliminar:"))
    for k in k:t
    n - k

def bucle2(o, n, t):
    L = int(input("Jugador 2,Seleccione 2, 3 o 5 piedras a eliminar:"))
    for L in L:o
    bucle(t, n) - L

def GameOfStones(n, t, o):
    resta = bucle(t, n)
    while True:
        if resta == 0:
           print("Jugador 1 gana")
           break
        elif resta == 1:
           print("Jugador 1 gana")
           break
        else:
            resta1 = bucle2(o, n, t)
            if resta1 == 0:
                print("Jugador 2 gana")
            elif resta1 == 1:
                print("Jugador 2 gana")
                break
            else:                
                continue
print(GameOfStones(12, 100, 100))


        
        
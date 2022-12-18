import random
def Laberinto(n, m, k):
    #Primero n y m deben ser < 20
    while n and m not in range(1, 20):
        print("Las dimensiones deben de n y m, deber ser menor que 20")
        break
    #Ahora continuamos, y deberiamos declarar una matriz nxm. o mejor veamos el tipo de opciones con los diferentes caracteres
    print("A denota una celda libre")
    print("# denota un obstáculo")
    print("M denota una celda con una mina")
    print("% denota una celda con una salida.")
    print("Y T denota una celda en la que se encuentra un tuenl bidireccional")
    #Podemos probar a crear una lista que albergue dichos caracteres 
    Caract = list("A#M%T")
    #Tendremos que randomear numero de veces que aparace cada caracter y donde
    # Declaramos la matriz para que en los bucles podamos referenciar
    Laberinto = [n , m]
    # Hemos de añadir a la matriz la posicion de A en laberinto[n], Hagamoslo con un input
    i = int(input("Ingrese la posicion que desee para A: "))
    if Laberinto[i:n]:#No sabemos si funciona
        j = int(input("Ingrese la posicion que desee para A: "))
        if Laberinto[j:m]:
            Laberinto.append[i:j, Caract[1]]
    # Lo mismo con # Si bien i1 tiene que ser != i
    i1 = int(input("ingrese la psociion que desee para #: "))
    if Laberinto[i1:n]:
        j1 = int(input("ingrese la psociion que desee para #: "))
        if Laberinto[j1:m]:
            Laberinto.append[i1:j1, Caract[2]]
    # vamos con M
    i2 = int(input("Ingrese la posicion que desee para M: "))
    if Laberinto[i2:n]:
        j2 = int(input("Ingrese la posicion que desee para M: "))
        if Laberinto[j2:m]:
            Laberinto.append[i2:j2, Caract[3]]        
    #Vamos con %
    i3 = int(input("Ingrese la posicion que desee para %: "))
    if Laberinto[i3:n]:
        j3 = int(input("Ingrese la posicion que desee para %: "))
        if Laberinto[j3:m]:
            Laberinto.append[i3:j3, Caract[4]]
    #Vamos con T
    i4 = int(input("Ingrese la psocion que desee para T: "))
    if Laberinto[i4:n]:
        j4 = int(input("Ingrese la psocion que desee para T: "))
        if Laberinto[j4:m]:
            Laberinto.append[i4:j4, Caract[5]]
    return Laberinto
print(Laberinto(5, 5, None))
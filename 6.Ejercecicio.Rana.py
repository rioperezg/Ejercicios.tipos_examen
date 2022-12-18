"""""
La rana Alef está en un laberinto bidimensional nxm representado como una mesa. El laberinto tiene las
siguientes características:
• Cada celda puede ser libre o contener un obstáculo, una salida o una mina .
• Dos celdas cualesquiera de la tabla se consideran adyacentes si comparten un lado.
• El laberinto está rodeado por una pared sólida hecha de obstáculos.
• Algunos pares de celdas libres están conectados por un túnel bidireccional.
• Cuando Alef está en cualquier celda, puede elegir al azar y con la misma probabilidad moverse
a una de las celdas adyacentes que no contengan ningún obstáculo. Si esta celda contiene una
mina, la mina explota y Alef muere. Si esta celda contiene una salida, Alef escapa del laberinto.
• Cuando Alef aterriza en una celda con una entrada a un túnel, es inmediatamente transportado
a través del túnel y arrojado a la celda en el otro extremo del túnel. A partir de entonces, no
volverá a caer y ahora volverá a moverse aleatoriamente a una de las celdas
adyacentes. (Posiblemente podría caer en el mismo túnel más tarde).
• Es posible que Alef se quede atascado en el laberinto en el caso de que la celda en la que fue
arrojado desde un túnel esté rodeada de obstáculos por todos lados.
• Su tarea es escribir un programa que calcule e imprima una probabilidad de que Alef escape del
laberinto.
Formato de entrada
La primera línea contiene tres enteros separados por espacios , n, m y k que denota las dimensiones del
laberinto y el número de túneles bidireccionales.
El siguiente n las líneas describen el laberinto. Los i's contienen una cadena de longitud m denotando
los i`s del laberinto. El significado de cada carácter es el siguiente:
• # denota un obstáculo.
• A denota una celda libre donde Alef está inicialmente.
• denota una celda con una mina.
• % denota una celda con una salida.
• denota una celda libre (que puede contener una entrada a un túnel).
El siguiente las líneas k describen los túneles. Los i contienen cuatro enteros separados por
espacios i1,i2,i3 ,i4 . Aquí, (i1,i2)y (i3,i4) denotan las coordenadas de ambas entradas del túnel. (i,j)
denota el número de fila y columna, respectivamente.
Restricciones
• n y m deben ser menores que 20
• i1 e i2 deben ser menores o iguales que n
• i1 e i2 deben ser menores o iguales que m
• n*m debe ser mayor a 2*k
• (i1,ji) y (i2,j2) son distintos.
• A aparece exactamente una vez.
• Cada celda libre contiene como máximo una entrada a un túnel.
• Si una celda contiene una entrada a un túnel, entonces no contiene un obstáculo, mío o de
salida, y Alef inicialmente no se para en ella.
• Los túneles no conectan celdas adyacentes.
Formato de salida
Imprime un número real que indique la probabilidad de que Alef escape del laberinto. Su respuesta se
considerará correcta si su diferencia (absoluta) de la respuesta verdadera no es mayor que 10-6
Explicación
A continuación, se muestra este caso de muestra:
En este caso, Alef elegirá al azar una de las cuatro celdas adyacentes. Si sube o baja, explotará y
morirá. Si va a la derecha, escapará. Si va a la izquierda, pasará por un túnel y se quedará atrapado en la
celda (2,1).. Entonces, la probabilidad de que Alef escape es 1/4.
"""
#Hemos de crear un programa que contenga por entradas el tamaño del laberinto y el numero de tuneles bidireccionales. La pregunta es 
#Debemos crear nosotros el laberinto o debe autocrearse? Es correcto debemos crearlo nosotros, pero si lo creamos nosotros, estara
# Pensado para un tamaño determinado del laberinto? y por lo tanto no tiene sentido estabelecer dichos numeros como entradas.
# Bueno veamos si somos capaces de hacer que se genere todo de forma aleatoria. 
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
    for Laberinto[1:n] in Laberinto[i]:#No sabemos si funciona
        j = input("Ingrese la posicion que desee para A: ")
        for Laberinto[1:m] in Laberinto[i:j]:
            Laberinto.append[i:j, Caract[1]]
    # Lo mismo con # Si bien i1 tiene que ser != i
    i1 = int(input("ingrese la psociion que desee para #: "))
    for Laberinto[1:n] in Laberinto[i1]:
        j1 = input("ingrese la psociion que desee para #: ")
        for Laberinto[1:m] in Laberinto[i1:j1]:
            Laberinto.append[i1:j1, Caract[2]]
    # vamos con M
    i2 = int(input("Ingrese la posicion que desee para M: "))
    for Laberinto[1:n] in Laberinto[i2]:
        j2 = input("Ingrese la posicion que desee para M: ")
        for Laberinto[1:m] in Laberinto[i2:j2]:
            Laberinto.append[i2:j2, Caract[3]]        
    #Vamos con %
    i3 = int(input("Ingrese la posicion que desee para %: "))
    for Laberinto[1:n] in Laberinto[i3]:
        j3 = input("Ingrese la posicion que desee para %: ")
        for Laberinto[1:m] in Laberinto[i3:j3]:
            Laberinto.append[i3:j3, Caract[4]]
    #Vamos con T
    i4 = int(input("Ingrese la psocion que desee para T: "))
    for Laberinto[1:n] in Laberinto[i4]:
        j4 = input("Ingrese la psocion que desee para T: ")
        for Laberinto[1:m] in Laberinto[i4:j4]:
            Laberinto.append[i4:j4, Caract[5]]
    return Laberinto
print(Laberinto(5, 5, None))



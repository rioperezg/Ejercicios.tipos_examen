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
import math
import os
import random
import re
import sys

first_multiple_input = input("ingrese un numero:").rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
k = int(first_multiple_input[2])
for n_itr in range(n):
    row = input()
#Escribamos que sucede en cada caso
    O = print("Aqui se encuentra un obstaculo, vuelve a la celda anterior")
    M = print("Aqui se encuentra una mina, Game Over")
    S = print("Aqui se encuentra una salida, Felicidades")
    B = print("Aqui se encuentra una celda libre, puede continuar")

# Write your code here
# #significa obstaculo; A una celda libre; M una mina; % una salida; y B una celda libre puede que con una entrada a un tunel
for k_itr in range(k):
    second_multiple_input = input().rstrip().split()
i1 = int(second_multiple_input[0])
j1 = int(second_multiple_input[1])
i2 = int(second_multiple_input[2])
j2 = int(second_multiple_input[3])

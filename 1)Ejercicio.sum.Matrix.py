import math
import os
import random
import re
import sys
"""""
Dada una matriz de números enteros N, encuentre la suma de sus elementos.
Función descriptiva
Complete la función simpleArraySum . Debe devolver la suma de los elementos de la matriz como un
número entero.
simpleArraySum tiene los siguientes parámetros:
ar : una matriz de números enteros
Formato de entrada
La primera línea contiene un número entero, N, que denota el tamaño de la matriz.
La segunda línea contiene N enteros separados por espacios que representan los elementos de la
matriz.
"""
def simpleArraySum(ar):
    "ar es la matriz de numeros enteros y N el numero que denota el tamaño de esta matriz"
    N = int(len(ar))
    return sum(ar)

A = [1, 2, 3, 4, 10, 11] 
print(A)   
print(simpleArraySum(A))
    



    
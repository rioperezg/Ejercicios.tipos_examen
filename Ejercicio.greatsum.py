"""""
En este desafío, debe calcular e imprimir la suma de los elementos en una matriz, teniendo en cuenta
que algunos de esos números enteros pueden ser bastante grandes.
Función descriptiva
Complete la función aVeryBigSum. Debe devolver la suma de todos los elementos de la matriz.
aVeryBigSum tiene los siguientes parámetros:
int ar [n] : una matriz de números enteros.
Salida
long : la suma de todos los elementos de la matriz
Formato de entrada
La primera línea de la entrada consta de un número entero .
La siguiente línea contiene enteros separados por espacios contenidos en la matriz.
"""
def simpleArraySum(ar):
    "ar es la matriz de numeros enteros y N el numero que denota el tamaño de esta matriz"
    N = int(len(ar))
    return sum(ar)

A = [1, 2, 3, 4, 10, 11] 
print(A)   
print(simpleArraySum(A))
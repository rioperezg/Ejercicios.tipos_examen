"""""
Dos jugadores llamados P1 Y P2 están jugando un juego con un número inicial de n piedras. Jugador1
siempre juega primero, y los dos jugadores se mueven en turnos alternos. Las reglas del juego son las
siguientes:
En un solo movimiento, un jugador puede eliminar ,2,3 o 5 , o piedras del tablero de juego.
Si un jugador no puede hacer un movimiento, ese jugador pierde el juego.
Dado el número inicial de piedras, busque e imprima el nombre del ganador.
Cada jugador juega de manera óptima, lo que significa que no harán un movimiento que les haga perder
el juego si existe un movimiento ganador.
• Por ejemplo, si n=4, P1 puede hacer los siguientes movimientos:
• P1 elimina 2 piedras quedando 2. P2 luego eliminará 2 piedras y ganar.
• P1 elimina 3 piedras quedando 1 . P2 no se puede mover y pierde.
Función descriptiva
Complete la función gameOfStones. Debería devolver una cadena, ya sea P1 o P2 winner.
gameOfStones tiene los siguientes parámetros:
n : un número entero que representa el número inicial de piedras
Formato de entrada
La primera línea contiene un número entero T , el número de casos.
Cada uno de los siguientes T lienas contiene un entero , el número de piedras en un caso de prueba.
Explicación
En la muestra tenemos T=8 Casos:
• Si n=1, P1 no puede hacer ningún movimiento y pierde el juego.
• Si n=2 , P1elimina piedras y gana el juego.
• Si n=3, P1 elimina piedras en su primer movimiento, dejando piedra en el tablero y ganando
el juego.
• Sin=4 ,P1 elimina piedras en su primer movimiento, dejando piedra en el tablero y ganando el
juego.
• Si n=5 , P1 elimina todo piedras del tablero de juego, ganando el juego.
• Si n=6, P1 elimina piedras en su primer movimiento, dejando piedra en el tablero y ganando
el juego.
• Si n=7,P1 puede realizar cualquiera de los siguientes tres movimientos:
o Eliminar 2 piedras, dejando 5 piedras en el tablero. P2 luego quita piedras, ganando el
juego.
o Eliminar 3 piedras , dejando 4 piedras en el tablero. P2 luego quita piedras,
dejando piedra dejada en el tablero y ganando el juego.
o Eliminar 5 piedras, dejando3 piedras en el tablero.P2 luego quita el piedras restantes
y gana el juego.
Todos los movimientos posibles dan como resultado victoria.
"""
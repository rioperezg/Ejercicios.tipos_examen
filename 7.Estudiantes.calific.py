"""""
La Universidad para el nuevo curso va a implementar una nueva poítica de calificación:
• Cada estudiante recibe una nota en el rango inclusivo de 0 a 100 .
• Si tienes una nota inferior a 40 o menos es una calificación suspensa.
Además a los profesores en la universidad nos gusta redondear los de acuerdo con estas reglas:
• Si la diferencia entre una nota y el siguiente múltiplo de es menos que 3 , se redondea hasta el
siguiente múltiplo de 5 .
• Si el valor de la nota es menorque 40 , no se produce redondeo ya que el resultado seguirá
siendo una calificación suspensa.
Ejemplos
• 84 redondear a (85 - 84 es menos de 3)
• 29 no redondear (el resultado es menos de 40)
• 57 no redondear (60 - 57 es 3 o más)
Dado el valor inicial de la nota para cada uno de los n estudiantes, escriban código para automatizar
el proceso de redondeo.
Función descriptiva
Complete la función calificando Estudiantes en el editor a continuación.
gradingStudents tiene los siguientes parámetros:
int calificaciones [n] : las calificaciones antes del redondeo
Devoluciones
int [n] : las calificaciones después de redondear según corresponda
Formato de entrada
La primera línea contiene un solo entero, n, el número de estudiantes.
Cada línea i de n notas contienen un solo entero, nota[i] .
Explicación
Estudiante 1recibió un 73 y el siguiente múltiplo de 5 de 73 es 75 . 75-73<3 Ya que, la calificación del
estudiante se redondea a 75.
Estudiante 2 recibió un 67 y el siguiente múltiplo de 5 de 67 es 70 .70-67=3 Ya que, la calificación no se
modificará y la calificación final del estudiante es 67 .
Estudiante 3 recibió un 38 y el siguiente múltiplo de5 de 38 es 40 . Ya que 40-38<3, la calificación del
estudiante se redondeará a 40.
Estudiante 4 recibió 33 una calificación por debajo de 40, por lo que la calificación no se modificará y la
calificación final del estudiante es 33 .
"""
def Grading_Students(Grades):
    #Primero de todo diferenciemos entre una calificacion suspensa y una que no lo es
    if Grades < 40:
        return("El alumno ha suspendidido")
    else:
    #Y ahora continuamos con el caso del aprobado. Necesitamos un metodo que considere los numeros que son multiplos de 5
    #Para empezar pasaremos dicho numero por un entero. Pasemos el numero como si fuera un rango de 40 a 100 ya que es la maxima
    #Puntuacion
        for i in range(40, 100):
            if i % 5:
                if i - Grades == + 3:
                   return("El alumno tiene", i,"de nota")
                else:
                   return("El alumno tiene", Grades,"de  nota")
            else:
                continue
print(Grading_Students(54))

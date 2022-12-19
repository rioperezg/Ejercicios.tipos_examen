def lunes(cumpleaños, fecha_actual):
    Edad = fecha_actual[0] - cumpleaños[0]
    if Edad >= 22 and Edad <= 78:
        return (Edad*365)/7
    else:
        return 0
print(lunes([1980, 4, 8], [2014, 6, 19]))
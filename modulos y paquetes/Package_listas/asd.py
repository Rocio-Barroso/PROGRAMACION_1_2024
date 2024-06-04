# Corregir el código y documentar los errores, para que el algoritmo permita ordenar los valores del vector de forma descendente.
#  Entregar link GDB.


vector = [3, 8, 1, 4, 7]

for i in range (1, len(vector)):
    for j in range(i, len(vector)):
        if vector[i] == vector[j]:
            vector[j] = auxiliar
            auxiliar = vector[j]
            vector[i] = auxiliar
    print(vector)
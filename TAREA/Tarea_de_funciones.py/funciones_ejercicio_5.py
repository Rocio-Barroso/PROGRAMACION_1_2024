'''
5-Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro 
y devolver el área.
'''
import math
###### DETERMINAR AREA ####
def determinar_area (radio):

    if radio != 0:
        area = math.pi * (radio * radio)
    else:
        pass

    return area

radio = input("Ingrese radio: ")
radio = float(radio)


area = determinar_area(radio)
print(f"El area del circulo es: {area}")
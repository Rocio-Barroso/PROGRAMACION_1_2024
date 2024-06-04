''' 
6-Crea una función que verifique si un número dado es par o impar. 
La función debe imprimir un mensaje indicando si el número es par o impar.
'''

##### PAR O IMPAR ################
def determinar_par(numero): #funcion en infinitivo
    if numero % 2 == 0:
        resultado = "numero es par"
    else:
        resultado = "numero es impar"

    return resultado

numero = input("ingrese numero: ")
numero = int(numero)

resultado = determinar_par(numero)
print(resultado) 
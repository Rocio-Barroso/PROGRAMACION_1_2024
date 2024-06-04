'''
1-Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

3-Crear una función que le solicite al usuario el ingreso de una cadena y la retorna. 
4-Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.
5-Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro 
y devolver el área.
6-Crea una función que verifique si un número dado es par o impar. 
La función debe imprimir un mensaje indicando si el número es par o impar.
7-Define una función que encuentre el máximo de tres números. 
La función debe aceptar tres argumentos y devolver el número más grande.
8-Diseña una función que calcule la potencia de un número. 
La función debe recibir la base y el exponente como argumentos y devolver el resultado.
'''
import math

####### numero entero ####
def determinar_entero(entero):

 return(entero)

entero = input("Ingrese numero: ")
entero = int(entero)

determinar_entero(entero)
print(entero)

###### numero flotante ####
def determinar_flotante(flotante): 
 return(flotante) 

flotante = input("Ingrese numero flotante: ")
flotante = float(flotante)

determinar_flotante(flotante)
print(flotante)

##### cadena de texto ####
def determinar_cadena(cadena):

    return(cadena)

cadena = input("Ingrese un texto: ")

determinar_cadena(cadena)
print(cadena)

######## punto 4 no se entiende#####

####################################
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

##### DETERMINAR MAXIMO #####
def determinar_maximo(numero_uno, numero_dos, numero_tres): 
        if numero_uno > numero_dos and numero_uno > numero_tres:
            maximo = numero_uno
        elif numero_dos > numero_tres:
            maximo = numero_dos
        else:
            maximo = numero_tres
        return maximo

numero_uno = input("Inrese su numero: ")
numero_uno = int(numero)
numero_dos = input("Inrese su numero: ")
numero_dos = int(numero)
numero_tres = input("Inrese su numero: ")
numero_tres = int(numero)

maximo = determinar_maximo(numero_uno, numero_dos, numero_tres)
print(f"El numero mayor ingresado fue: {maximo}")
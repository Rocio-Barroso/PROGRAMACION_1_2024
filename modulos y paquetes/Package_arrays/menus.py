from .input import *

def operaciones():

    opciones = input (
        "a. Ingrese 10 números enteros entre -1000 y 1000"
        "b. Cantidad de números positivos y negativos."
        "c. Mostrar la sumatoria de los números pares."
        "d. Informar el mayor de los números impares."
        "e. Listar todos los números ingresados."
        "f. Listar todos los números pares."
        "g. Listar los números de las posiciones impares."  
        "h. Salir")


    while bandera_seguir:
        match opciones:
            case "a":
                for i in range (10):
                    numero = get_int("Ingrese un numero entre -1000 y 1000", -1000, 1000)
                    

#for input import *
#import .input
#from input import *

from .input import *

def validate_number(mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:

    for i in range(0, reintentos):
        numero = get_int(f"ingrse un numero entre {minimo} y {maximo}, tiene {reintentos} reintentos: ") 
        
        if numero < minimo or numero > maximo:
            print(f"{mensaje_error}, de {minimo} a {maximo}: ")
        else: 
            print(numero) 
            break


entero = validate_number("El numero no esta en rango", 2, 5, 3)

def validate_length(mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:

    for i in range (0, reintentos):
        cadena = get_string(f"Ingrese una cadena de caracteres entre {minimo} y {maximo} tiene {reintentos} reintentos: ")

        if len(cadena) < minimo or len(cadena) > maximo:
            print(f"{mensaje_error}, de {minimo} a {maximo}: ")
        else:
            print(cadena)
            break

#cadena = validate_length("La cadena no esta en rango", 2, 6, 3)
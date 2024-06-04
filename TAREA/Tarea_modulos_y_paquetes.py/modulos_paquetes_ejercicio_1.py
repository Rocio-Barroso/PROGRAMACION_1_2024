'''
Realizar una función para pedir un número por consola. La misma deberá seguir el siguiente prototipo:
def get_int(mensaje:str, mensaje_error: str, minimo: int, maximo: int, reitentos: int) -> int|none

En donde:
mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
mínimo: valor mínimo admitido (inclusive)
máximo: valor máximo admitido (inclusive)
reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.

'''


def get_int(mensaje: str, mensaje_error: str, minimo: int , maximo: int , reitentos: int) -> int|None:
#def get_int(mensaje: str, mensaje_error: str, minimo: int , maximo: int , reitentos: int):

    print(mensaje)

    numero = input("Ingrese numero: ")
    numero = int(numero)

    for i in range(1, reitentos):
        while numero < minimo or numero > maximo:
            numero = input(mensaje_error)
            numero = int(numero)
            
            if i == reitentos:
                numero = None
                break
        
    return numero

#from Package_funciones.funciones import *

def pedir_x_numeros(rango : int) -> list:
    lista_numeros = []
    for i in range (rango):
            numero = get_int("Ingrese un numero entre -1000 y 1000: ", -1000, 1000)
            #numero = [numero]
            lista_numeros += [numero]
    return lista_numeros
        
# lista = pedir_x_numeros(10)
# print(lista)

def mostrar_positivos(lista_de_numeros: list) -> list:
    if len(lista_de_numeros) == 0:
        print("Necesita ingresar los datos primero elija opcion 'a' ") 

    for i in range(len(lista_de_numeros)):
        if lista_de_numeros[i] >= 0:
                print(lista_de_numeros)
        return numero

# resultado = mostrar_positivos()
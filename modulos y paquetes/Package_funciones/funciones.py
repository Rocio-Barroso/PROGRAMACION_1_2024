import math
from Package_input.input import *
####### numero entero ####

def get_int (mensaje: str, minimo: int, maximo: int) -> int:

    numero = input(mensaje)
    if numero.isdigit():
            numero = int(numero)
            while numero < minimo or numero > maximo:
                numero = input(f"Error, {mensaje}")
                numero = int(numero)
            return numero
    else:
            print("el digito ingresado no es valido")

    return numero

###### numero flotante ####

def get_float(mensaje: str, minimo: float, maximo: float) -> float:

    flotante = input(mensaje)
    flotante = float(flotant)

    while flotante < minimo or flotante > maximo:
        flotante = input(f"Error, {mensaje}")
        flotante = float(flotante)

    return flotante 

##### cadena de texto ####

def determinar_cadena(mensaje: str, minimo: int, maximo: int) -> str:

    cadena = input(mensaje)

    while len(cadena) < minimo or len(cadena) > maximo:
        cadena = input(f"Error, {mensaje}")

    return(cadena)




###### DETERMINAR AREA ####
def determinar_area (radio):


    if radio != 0:

        area = math.pi * (radio * radio)

    else:

        pass

    return area

    # area = determinar_area(radio)

    # print(f"El area del circulo es: {area}")


##### PAR O IMPAR ################

def determinar_par(numero: int) -> bool: #funcion en infinitivo

    if numero % 2 == 0:

        resultado = True

    else:

        resultado = False


    return resultado

# numero = int(input("ingrese numero: "))


# if determinar_par(numero):

#     print("es par")

# else:

#     print ("impar") 

#### DETERMINAR MAXIMO #####

def determinar_maximo(numero_uno, numero_dos, numero_tres): 

        if numero_uno > numero_dos and numero_uno > numero_tres:

            maximo = numero_uno

        elif numero_dos > numero_tres:

            maximo = numero_dos

        else:

            maximo = numero_tres

        return maximo


# numero_uno = input("Inrese su numero: ")
# numero_uno = int(numero)

# numero_dos = input("Inrese su numero: ")
# numero_dos = int(numero)

# numero_tres = input("Inrese su numero: ")
# numero_tres = int(numero)


# maximo = determinar_maximo(numero_uno, numero_dos, numero_tres)

# print(f"El numero mayor ingresado fue: {maximo}")

#######################################################################

def sumar_dos_numeros (un_numero: int, otro_numero: int) -> int:

 suma = un_numero + otro_numero
 return suma

########## POTENCIA ############
def determinar_potencia (pedir_base: str, pedir_exponente: str) -> int:
    potencia = 1

    base = input(pedir_base)
    base = int(base)
    exponente = input(pedir_exponente)
    exponente = int(exponente)
    
    for i in range(0, exponente):

        potencia = potencia * base
        

    return potencia

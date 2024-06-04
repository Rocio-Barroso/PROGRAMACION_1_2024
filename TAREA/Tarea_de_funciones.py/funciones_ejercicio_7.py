''' 
7-Define una función que encuentre el máximo de tres números. 
La función debe aceptar tres argumentos y devolver el número más grande.

'''

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
numero_uno = int(numero_uno)
numero_dos = input("Inrese su numero: ")
numero_dos = int(numero_dos)
numero_tres = input("Inrese su numero: ")
numero_tres = int(numero_tres)

maximo = determinar_maximo(numero_uno, numero_dos, numero_tres)
print(f"El numero mayor ingresado fue: {maximo}")
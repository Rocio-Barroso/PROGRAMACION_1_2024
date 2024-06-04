#Realizar un menú de opciones en donde el usuario pueda realizar las siguientes operaciones:
#Pedir el ingreso de 10 números enteros entre -1000 y 1000. 
#Mostrar la cantidad de números positivos y negativos.
#Mostrar la sumatoria de los números pares.
#Informar el mayor de los números impares.
#Listar todos los números ingresados.
#Listar todos los números pares.
#Listar los números de las posiciones impares.  
#Salir

# def determinar_tipo(numero: int, positivo: str, negavito: str, suma_pares: int, mayor_impar: int)
    
#     for i in range 10:
#         numero = int(input("Ingrese numero"))
def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    print(f"{mensaje}, tiene {reintentos} reintentos para ingresar su numero")

    numero = input(f"ingrese un minimo de {minimo} y un maximo de {maximo}: ")
    numero = int(numero)

    
    for i in range(0, reintentos):
        if numero == None:
            break     #
        elif numero < minimo or numero > maximo:
            numero = input(f"{mensaje_error}, de {minimo} a {maximo}: ")
            numero = int(numero)
        else: 
            print(numero) 
            break

#numero = get_int(f"Hola, bienvenido a esta funcion", f"Error, el numero no esta en el rango", 2, 6, 3)

def get_string (longitud: int, mensaje_error) -> str|None:
    while True:
        contador = 0
        cadena = input(f"Ingrese texto de maximo {longitud} caracteres: ")
        for i in (cadena):
            contador = contador + 1
            #print(contador)

        if cadena == None:
            break     #
        elif contador <= longitud:
            return cadena
        else:
                cadena = print(f"{mensaje_error}, de {longitud} caracteres")
                #print(f"error{contador}")

                
                # for i in (cadena):
                #     contador = contador + 1
                #     print(contador)

        # else:
                #contador <= longitud
            
            #   print(cadena) 
            #    break

# resultado = get_string(3, "Error, la cadena no debe ser mayor")
# print(resultado)

def get_float(mensaje: str, minimo: float, maximo: float) -> float:

    flotante = input(mensaje)
    flotante = float(flotant)

    while flotante < minimo or flotante > maximo:
        flotante = input(f"Error, {mensaje}")
        flotante = float(flotante)

    return flotante 
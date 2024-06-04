# # from os import system

# # badera_seguir = True
# # bandera_numeros_ingresados = False

# # while bandera_seguir:
# #     opcion = int(input("1.Ingresar datos\n2.sumar\n3.restar\4.Multiplicacion\n5.Dividir\n6.salir\nElija una opocion"))
    
# #     match opcion:
# #         case 1:
# #             numero_1 = int(input("Ingrese el primer numero"))
# #             numero_2 = int(input("Ongrese el segundo numero: "))
# #             bandera_numeros_ingresados = True
# #         case 2:
# #             resultado = funcion_sumar(numero_1, numero_2)
# #             print(f"El resultado de la suma es: {resultado}")
# #         case 3:
# #             print("Estoy restando")
# #         case 4:
# #             print("Estoy multiplicando")
# #         case 5: 
# #             print("estoy dividiendo")
# #         case 6:
# #             seguir == "si":
# #             badera_seguir = False
    
# # system("pausa")



# # #Desarrollar una función que reciba como parametros 
# # # el precio de un producto,la cantidad y el porcentaje de descuento que se aplicara 
# # #si la cantidad de productos supera las 10 unidades.
# # #La funcion retornara el precio de la compra con descuento (si corresponde).  (Enviar aqui link de GDB)

# # def determinar_descuento (precio:  int, cantidad: int, porcentaje_descuento: int) -> int

# #     if cantidad > 10:
# #         precio_total = precio 


# # from Package_funciones.funciones import determinar_potencia

# # resultado = determinar_potencia("Ingrese base: ", "Ingrese exponente: ")
# # print(resultado)
#from Package_input.validate import *
# from Package_input.input import *



# def validate_number(mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:

#     for i in range(0, reintentos):
#         numero = get_int(f"ingrse un numero entre {minimo} y {maximo}, tiene {reintentos} reintentos: ") 
        
#         if numero < minimo or numero > maximo:
#             print(f"{mensaje_error}, de {minimo} a {maximo}: ")
#         else: 
#             print(numero) 
#             break

# entero = validate_number("El numero no esta en rango", 2, 5, 3)

# def validate_length(mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:

#     for i in range (0, reintentos):
#         cadena = get_string(f"Ingrese una cadena de caracteres entre {minimo} y {maximo} tiene {reintentos} reintentos: ")

#         if len(cadena) < minimo or len(cadena) > maximo:
#             print(f"{mensaje_error}, de {minimo} a {maximo}: ")
#         else:
#             print(cadena)
#             break

# cadena = validate_length("La cadena no esta en rango", 2, 6, 3)

from Package_funciones.funciones import *
from Package_listas.generales import *
bandera_seguir = True



while bandera_seguir:
    opciones = input (
        "a. Ingrese 10 números enteros entre -1000 y 1000"
        "\nb. Cantidad de números positivos y negativos."
        "\nc. Mostrar la sumatoria de los números pares."
        "\nd. Informar el mayor de los números impares."
        "\ne. Listar todos los números ingresados."
        "\nf. Listar todos los números pares."
        "\ng. Listar los números de las posiciones impares."  
        "\nh. Salir"
        "\nElija una opcion: ")

    match opciones:
        case "a":
            for i in range (10):
                numero = pedir_x_numeros(10)
        case "b":
            numeros_positivos = mostrar_positivos(numero)



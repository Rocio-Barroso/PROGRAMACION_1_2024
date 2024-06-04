################### DESARROLLO FUNCION ######################

def sumar_1():


    un_numero = input("ingrese un numero: ")
    un_numero = int(numero)
    otro_numero = input("ingrese otro numero: ")
    otro_numero = int(otro_numero)

    suma = un_numero + otro_numero

    print(f"La suma es: {suma}")

#######################################################
def sumar_2(un_numero, otro_numero):
    suma = un_numero + otro_numero

    print(f"La suma es: {suma}")

#######################################################

def sumar_3():
    numero_uno = input("Ingrese numero: ")
    numero_uno = int(numero_uno)
    numero_dos = input("Ingrese numero: ")
    numero_dos = int(numero_dos)

    suma = numero_uno + numero_dos
    return suma

###########################################################

def sumas_4(un_numero, otro_numero): #INDEPENDIENTE Y REUTILIZABLE
    suma = un_numero + otro_numero

    return suma


################## LLAMADA FUNCION #########################



print("Bienvenidos a mi programa")
# sumar_1() #no recibe parametros no devulve nada
#sumar_2(numero)

#resultado = sumar_3()

#otra_variable = resultado + 500

#print(f"La suma es: {resultado}")
#print(f"La suma es: {otra_variable}")

resultado = sumar_4(8, 99) #recibe parametros y retorna el resultado
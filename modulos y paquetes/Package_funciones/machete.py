# #se modifica solo de manera local porque estoy creando una nueva variable que apunta a otro lado 
# #la unica manera de modificar un valor x referencia inmutable 
# # es devolviendo el resultado (return) y asignandolo a la variable original

# def modificar_numero (numero_1):         #si quiero pasar un valor a una funncion y que esa funcion la modifique
#                                          # no se puede porque se creoa una variable nueva
#     print(id(numero_1))

#     numero_1 = 25
#     print(id(numero_1))
                                       
# numero = 5
# print(id(numero))
# modificar_numero(numero)
# print(id(numero))
# print(numero)

# #si quiero pasar un valor a una funncion y que esa funcion la modifique
# #necesito que la funcion retorne el valor que modifique
# #entonces tengo que guardar la funcion en la variable que quiero modificar
# def modificar_numero (numero_1) -> int:

#     numero_1 = 25
#     return numero_1

# numero = 5
# numero = modificar_numero(numero)  #entonces tengo que guardar la funcion en la variable que quiero modificar (esto)

# print(numero)
# ####################################################################################################################
# #Las listas son mutables por lo que si yo modifico el valor de una lista en vez de crear otro espacio en memoria
# # se usa el mismo porque al pasarlo x referencia los dos objetos apunan al mismo lugar

# def modificar_lista (lista_modificada: list) -> None:
#     lista_modificada[3] = "valor modificado" #indico que se modifique el valor de la posicion 3

# lista = [5, 9, 8, 7, 6]
# print(lista) #imprimo la lista tal cual la escribi
# modificar_lista(lista) #llamo a la funcion y le paso el espacio de memoria de lista
# print(lista) #e imprimo la lista modificada

#los id van a ser los mismos porque al modificar la lista en la funcion tambien modifico la original, 
# porque paso un valor x parametro mutable
############################# importar funciones dentro del mismo paquete ##########################################
####### importo funciones y escribo funciones .(punto) y llamo explicitamente a la funcion que necesito ############
            # import funciones
            # maximo = funciones.determinar_maximo(2, 5, 3)
            # print(maximo)
######### otra manera importando todo el modulo o sea que trae todo lo que esta defifido en el modulo ###############
# from funciones import *

# resultado = sumar_dos_numeros(2, 3)
# print(resultado)
################### puedo traer la funcion o el componente especifico que necesito usar ###########################
# from funciones import determinar_par 
# resultado = determinar_par (5)
# print(resultado)

################################# Importar funciones de un paquete en el main ######################################
######### Del modulo funciones que esta en el paquete funciones traeme la funcion determinar area ##########
# from Package_funciones.funciones import determinar_area #tambien se puede usar impor * que traeria todo
# #aca no funciona porque estamos dentro del paquete
# area = determinar_area(12)
# print(area)
################
# from Package_funciones.funciones import get_int

# edad = get_int("Ingrese edad: ", 18, 60)
################### se puede usar un alias tambien, pero hay que importan primero###############################
# import Package_funciones.funciones as ALIAS

# resultado = ALIAS.determinar_cadena("Hola")
# print(resultado)
##################################################################################################################
#el factorial de un numero es ese numero multiplicado por si mismo menos 1 ej 5*4 5*3 5*2 5*1
# numero = 5
# factorial = 1
# for i in range(1, numero + 1):
#     factorial = factorial * 1
#     print(f"El factorial de {numero} es: {factorial}")

# def calcular_factorial(numero) -> int:
#     if numero == 0:     establezco un limite para no pasarme a los negativos porque si no sigo restando 1
#         resultado = 1   salgo
#     else:
#       resultado = numero * calcular_factorial(numero - 1) si no es 0 llamo a la funcion recursivamente
      
#       return resultado

# numero = 5
# factorial = calcular_factorial(numero)
# print(f"El factorial de {numero} es: {factorial}")

########################################################################################################## 
#recorer listas
# vector = [2, 5, 4, 8, 3]

# for i in range(len(vector)): # la forma correcta de recorrer un vecto es con un for s
# se usa el len porque para poder recorrer el vector se necesita saber cuantos elementos tiene y el len sirce pára eso
#     print(vector[i]) si pongo i va  amostrar del 1 al 5 porque tengo 5 elementos si pongo vector [i]
                        # va a mostrar 2 5 4 y 8 o sea el valor uno abajo del otro
#     print(vector[i], end = "/") los va a mostrar 2/5/4/8 y si dejo un espacio en blanco igual pero sin la barra
# lo puedo condicionar para que muestres solo los pares con
# if vector[i]  % 2 == 0 si pongo solo vector hago alusion a todo el vector, si pongo i es a cada uno de los componentes
# CARGA SECUENCIAL
# mi_lista [-1] * 5 creo un espacio en memoria con 5 elementos todos los elementos tienen -1 y al cargar secuencialmente 
                    # los valores se van a reemplazar por lo que ingrese el usuario
# for i in range(len(mi_lista)):
#   mi_lista[i] = int(input("ingrese un numero")) me va a pedir un numero 5 veces
# para mostrarla hago un for con un print
# for i in range (len(mi_lista)):
#   print(mi_lista[i]) va a imprimir los 5 numeros que ingrese
#  mi_lista = [i] * 5
#  bandera_salida = True    # creo una bandera en true para que se cumpla aunque sea una vez
#  while bandera salida == True:  # se cumple la bandera y entra al while
#    index = int(input("inrgese la posicion")) # pido la posicion donde quiero guardar el numero
#       if index < 1 or index es > len(mi_lista): # tengo que condicionar el codigo para que no eliga una posicion inexistente
#            index = int(input("Reinrgese la posicion"))
#    numero = int(input("ingrese un numero"))
#    mi_lista[index-1] = numero
#    seguir = input(continua? si/no)
#        if bandera_seguir == "no"  # tengo que condicionar condicionar el bucle wile para que salga, si no es infinito
#           bandera_salida = False
#tambien podria usar un break hacer while true sin las banderas y poner un break abajo del if
# for i in range (len(mi_lista)):
#   if mi_lista[i] != -1
#       print(f"(i+1) -- (mi_lista[i]"))
# lista = [45, 9, 3, -3, 10, -2, 3]
# suma = 0
# for i in range(len(lista)):
#   if lista[i] > 0:
#      suma = suma + lista[i]
# print(f"La suma es: {suma}")
#######calcular maximo##########
# lista = [45, 9, 3, -3, 10, -2, 3]
# bandera_maximo = True
# for i in range(len(lista)):
#    if bandera_maximo == True or lista[i] > maximo_numero:
#       maximo_numero = lista[i]
#       bandera_maximo = False
#   print(f"El numero maximo es {maximo_numero}")
###########encontrar negativo##############
#bandera_negativo = False    #Las banderas son chekpointa, en este caso la uso para verificar si hay un negativo
# for i in range(len(lista)):  #para cada iteracion dentro de la lista
#   if lista[i] < 0:            #si la interacion de lista es menor a 0...
#       bandera_negativo = True #la bandera o chekpoint pasa a ser verdadero
#        break
# if bandera_negativo == True:  #si la bandera es verdadera digo que hay por lo menos un negativvo
#   print("Hay por lo menos un numero negativo")
# else: 
#   print("no hay numeros negativos")
##########buscar y reemplazar###########
# lista = [45, 9, 3, -3, 10, -2, 3]
# numero buscado = 3    #declaro el numero que quiero buscar
# reemplazo = 1000      #declaro el numero por el cual va a ser reeemplazado
# for i in range(len(lista)):     #recorro la lista
#   if lista[i] == numero_buscado   #condiciono que si la iteracion de la lista tiene el valor que estoy buscando
#       lista[i] = reemplazo        #sea reemplazado por el numero que guarde en mi variable reemplazo
            #aca estoy reemplazando todos los 3 que aparezcan pero le puedo poner un break y en ese caso solo reemplazara el primero que encuentre
# for i in range(len(lista)):     #muestro toda la lista
#############funcioones con listas################################################
# def sumar_positivos(lista: list) -> int: # declaro la funcion sumar positivos y le paso la lista declarando que es una lista
#   retorno = -2 #devuelvo False si no me estan pasando lista o sea si no se cumple la linea que sigue
#   if type(lista) is list: ##si el tipo de dato es una lista
#       retorno = -1 # devuelvo-1 si se cumple lo anterior pero no lo que sigue 
#       if len(lista) > 0:  #si el largo de la lista es mayor a 0...
#            retorno = 0
#              for i in range (len(lista)): #para cada elemento de la lista...
#                   if lista[i] > 0:  # si el valor de la lista por iteracion es mayor a 0..
#                       retorno += lista[i]  #guardo el numero de la iteracion y sumo el siguiente si hay otro positivo
#  return retorno
# lista[2, 3]
# resultado = sumar_positivos(lista)
# if suma ==- 2:
#   print("El valor no es lista")
# elif suma == -1:
#   print("La lista esta vacia")
# else:
#   print(suma)

# def buscar_maximo(lista: list) -> int|None|str:
#   retorno = None #devuelvo none si no me estan pasando lista o sea si no se cumple la linea que sigue
#   bandera_maximo = True

#   if type(lista) is list: ##si el tipo de dato es una lista
#       retorno = "lista_vacia" # devuelvo no si se cumple lo anterior pero no lo que sigue 
#       if len(lista) > 0:  #si el largo de la lista es mayor a 0...
#         for i in range(len(lista)): #para cada elemento de la lista
#             if bandera_maximo == True or lista[i] > maximo_numero: #si bandera maximo = true guardar en maximo si no comparar si el valor de la iteracion es mayo a maximo numermo
#                 maximo_numero = lista[i]  #si es mayor lo guardo y vuelvo a iterar
#                 #print(maximo_numero)
#                 bandera_maximo = False
#         return maximo_numero

# lista = [2, 3, 0, 1]
# maximo = buscar_maximo(lista)
# if maximo == None:
#     print("no pasaste lista")
# elif maximo == "lista_vacia":
#     print("La lista esta vacia")
# else:
#     print(maximo) 
#
# def buscar_negativos(lista: list) -> bool:
#   bandera_negativo = False
#   for i in range(len(lista)):
#       if lista[i] < 0:
#           bandera_negativo = True
#           break
#   return bandera_negativo

# if buscar_negativo(lista):
#   print("hay un negativo")
# else:
#   print("nohay negativos") 
############################## menu de opciones iteractivo ######################################
# from os import system
# bandera_seguir = True
# while bandera_seguir: 
#   opcion = int(input("1. ingresar datos
#               \n2. Sumar 
#               \n3. Restar
#               \n4. Multiplicar
#               \n5. Dividir
#               \n6. Salir
#               \nElija una opcion: "))
#   match opcion:
#       case 1:
#           print("Ingrese los numeros")
#                                         aca van funciones que resulvan las sumas                  
#       case 2:
#           print("sumando los numeros")
#       case 3:
#           print("estoy restando")
#       case 4:
#           print("Estoy multiplicando")
#       case 5:
#           print("Estoy dividiendo")
#       case 6:
#           seguir = input("Seguro que quiere salir?")
#           if seguir == "si"
#               bandera_seguir = False
#
# system("pause") #pausa el sistema y escribe el presione una tecla pára continuar
# system("cls") #borra la consola t¿y vuelve a iterar


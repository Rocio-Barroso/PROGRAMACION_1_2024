def sumar_positivos(lista: list) -> int | bool:
    devuelve = None
    if type(lista) == list:
        devuelve = True
        if len(lista) > 0:
            devuelve = 0
            for i in range(len(lista)):
                if lista[i] > 0:
                    devuelve += lista[i]
    return devuelve

# lista = [4, -5, 6]
# suma = sumar_positivos(lista)
# if suma == None:
#     print("El valor ingresado no es una lista")
# elif suma == True:
#     print("La lista esta vacia")
# else:
#     print(suma)

def buscar_maximo(lista: list) -> int|None|str:
  retorno = None #devuelvo none si no me estan pasando lista o sea si no se cumple la linea que sigue
  bandera_maximo = True
  contador = 0

  if type(lista) is list: ##si el tipo de dato es una lista
      retorno = "lista_vacia" # devuelvo no si se cumple lo anterior pero no lo que sigue 
      if len(lista) > 0:  #si el largo de la lista es mayor a 0...
        for i in range(len(lista)): #para cada elemento de la lista
            if bandera_maximo == True or lista[i] > maximo_numero: #si bandera maximo = true guardar en maximo si no comparar si el valor de la iteracion es mayo a maximo numermo
                maximo_numero = lista[i]  #si es mayor lo guardo y vuelvo a iterar
                contador += 1
                #print(maximo_numero)
                bandera_maximo = False            

        return maximo_numero, contador

lista = [2, 3, 4, 1]
maximo = buscar_maximo(lista)
if maximo == None:
    print("no pasaste lista")
elif maximo == "lista_vacia":
    print("La lista esta vacia")
else:
    print(f" El maximo numero Y su pusicion es {maximo}") 

# def buscar_maximo(lista: list) -> bool:
#     bandera_negativo = False
#     for i in range(len(lista)):
#         if lista[i] > 0:
#             bandera_negativo == True
#             break
#     return bandera_negativo

# maximo = buscar_maximo(lista)
# print(maximo)

def buscar_remplazar(lista: list, buscar: int, remplazo: int, remplazo_todo: bool):
    retorno = False
    if type(lista) == list and type(buscar) == int and type(remplazo) == int:
        retorno = True
        for i in range(len(lista)):
            if lista[i] == buscar:
                lista[i] = remplazo
                if remplazo_todo == False:
                    break
    return retorno

# lista = [44, -9, 77, 44]
# if buscar_remplazar(lista, 44, 1000, True):
#     for i in range(len(lista)):
#         print(lista[i])
#     else:
#         print("Hubo un error, no pasaste lista")

def calcular_promedio(lista: list) -> int | bool:
    contador = 0
    retorno = None

    if type(lista) == list: 
        retorno = True
        # print(len(lista))
        if len(lista) > 0:
            # print("entra en el if")
            retorno = 0
            for i in range(len(lista)):
                # print("for")
                retorno += lista[i]
                contador += 1
        
              

    if retorno == True:
        return retorno
        print("La lista esta vacia")
    else:
        promedio = retorno / contador
        promedio = float(promedio)
        return promedio


# lista = []
# resultado = calcular_promedio(lista)
# # print(f"Res {resultado}")
# if resultado == None:
#     print("El valor ingresado no es una lista")
# elif resultado == True and resultado != 1:
#     print("La lista esta vacia")
# else:
#     print(resultado)

def calcular_promedio_positivos(lista: list) -> int | bool:
    contador = 0
    retorno = None

    if type(lista) == list: 
        retorno = True
        # print(len(lista))
        if len(lista) > 0:
            # print("entra en el if")
            retorno = 0
            for i in range(len(lista)):
                if lista[i] > 0:
                # print("for")
                    retorno += lista[i]
                    contador += 1
            
              

    if retorno == True:
        return retorno
        print("La lista esta vacia")
    elif retorno > 0 and contador > 0: 
        promedio = retorno / contador
        promedio = float(promedio)
        return promedio
    else:
        print("Esta funcion no promedia numeros negativos")
        return retorno

# lista = [-5, -2]
# resultado = calcular_promedio_positivos(lista)
# # print(f"Res {resultado}")
# if resultado == None:
#     print("El valor ingresado no es una lista")
# elif resultado == True and resultado != 1:
#     print("La lista esta vacia")
# else:
#     print(resultado)

def calcular_producto_acumulado(lista: list) -> int | bool:
    contador = 1
    retorno = None
    negativos = False
    if type(lista) == list: 
        retorno = True
        # print(len(lista))
        if len(lista) > 0:
            # print("entra en el if")
            retorno = 1
            for i in range(len(lista)):
                retorno *= lista[i]
                print(retorno)
                if lista [1] < 0:
                    negativos = True
            
    if negativos == True and lista[1] % 2 != 0:
        producto = -producto

              

    if retorno == True:
        return retorno
        print("La lista esta vacia")
    else:
        multiplicacion = retorno * contador
        #promedio = float(promedio)
        return multiplicacion
  

# lista = [-5, 10, -2]
# resultado = calcular_producto_acumulado(lista)
# # print(f"Res {resultado}")
# if resultado == None:
#     print("El valor ingresado no es una lista")
# elif resultado == True and resultado != 1:
#     print("La lista esta vacia")
# else:
#     print(resultado)

def remplazar_nombres(lista: list, reemplazar: str, reemplazo: str):
    retorno = False
    contador = 0
    if type(lista) == list:
        retorno = True
        for i in range(len(lista)):
            if lista[i] == reemplazar:
                lista[i] = reemplazo
                contador += 1
                #print(contador)     
    if retorno == False:        
        return retorno
    else:
        return contador

lista = ["Ana", "Juan", "Pedro", "Maria", "Ana"]
resultado = remplazar_nombres(lista, "Ana", "Pedro")
   
# if resultado == False:
#     print("no pasaste lista")
# else:
#     print(lista)
#     print(resultado)
    #else:
    #    print("Hubo un error, no pasaste lista")
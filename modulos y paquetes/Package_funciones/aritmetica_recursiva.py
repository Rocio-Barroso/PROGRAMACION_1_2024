import Package_input.validate as ALIAS

def sumar_naturales(numero: int) -> int:
    
    if numero == 1:
        return 1
        
    else:
        suma = numero + sumar_naturales(numero - 1) 
        print(suma)
    
    return suma

# numero = 5
# suma = sumar_naturales(numero)

def calcular_potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1
    else:
        potencia = base * calcular_potencia(base, exponente - 1)
    return potencia

# base = 2
# exponente = 5
# resultado = calcular_potencia(base, exponente)
# print(resultado)

#123 % 10 = 3 saco el ultimo numero
#123 // 10 = 12 saco los  que siguen
def sumar_digitos(numero: int) -> int:
    if numero < 10:
        return numero
    else:
        suma = numero % 10 #agarro el ulrimo
        numero //= 10 #// es un operador de division entera o sea, que elimina el numero que ya guardamos
        suma_digitos = suma + sumar_digitos(numero) #cuando se repite el que estaba atras pasa a ser el ultimo y se suman

        return suma_digitos

# numero = 457
# resultado = sumar_digitos(numero)
# print(resultado)
def calcular_fibonacci(numero: int) -> int:
    numero = ALIAS("El numero no esta en rango", 0, 5, 3)
    suma = suma + numero
    print(numero)

    return suma


# resultado = calcular_fibonacci(numero)
# print(resultado)
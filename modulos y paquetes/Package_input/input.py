def get_only_int(mensaje: str, ) -> int | None:
    
    while True:
        numero = input(mensaje)

        if numero.isdigit():
            numero = int(numero)
            return numero
        else:
            print("el digito ingresado no es valido")
            

# numero = get_int(f"Hola, ingrese un numero entero: ")
# print(numero)

def get_string (mensaje: str) -> str | None:
    while True:
        cadena = input(mensaje)
        #cadena = str(cadena)
    
        if cadena.isalpha():
            return cadena
        else:
            print("El digito es invalido")
         

# resultado = get_string("Hola, ingrese una cadena de caracteres: ")
# print(resultado)

def get_float(mensaje: str, mensaje_error) -> float | None:
   
            
   
    while True:
        flotante = input(mensaje)
        if flotante.isdigit():
            flotante = float(flotante)
            return flotante
            break


        contador = 0
        for i in (flotante):
            if i == '.':
                contador += 1
                if contador > 1:
                    print(mensaje_error)
                    break
        else: 
            if i.isdigit():    
                return flotante        
                break
            else:
                print(mensaje_error)

# resultado = get_float("Hola, ingrese un numero con punto: ", "El digito no es valido")
# print(resultado)

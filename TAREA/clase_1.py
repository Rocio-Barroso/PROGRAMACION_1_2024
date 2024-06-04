'''

 UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para
 su proximo desarrollo en python, que promete revolucionar el mercado. 

 Las posibles aplicaciones son las siguientes: 
 # Inteligencia artificial (IA),
 # Realidad virtual/aumentada (RV/RA), 
 # Internet de las cosas (IOT) 

 Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

 Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

 cargar por terminal 10 encuestas

 Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, 
    cuya edad este entre 25 y 50 años inclusive.
    #!X 2) Porcentaje de empleados que no votaron por IA,
    siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
    #!X 3) - Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.

'''
contador_masculinos_IOT_IA = 0    
contador_empleados_no_ia = 0
porcentaje_empleados_no_ia = 0

for i in range (5):
    #nombre del empleado
        nombre = input("ingrese nombre del empleado: ")
    #edad (no menor a 18)
        edad = input("Ingrese edad no menor a 18: ")
        edad = int(edad)
        while edad < 18:
            edad = input("REINGRESE EDAD: ")
            edad = int(edad)
    #genero (Masculino - Femenino - Otro)
        genero = input("Ingrese genero: ")
        while genero != "Femenino" and genero != "Masculino" and genero != "Otro":
            genero = input("El genero debe ser Femenino, Masculino u Otro, reingrese: ")
    #tecnologia (IA, RV/RA, IOT)
        tecnologia = input("Ingrese tecnolgia: ")
        while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
            tecnologia = input("REINGRESE TECNOLOGIA, IA, RV/RA o IOT: ")

    # Cantidad de empleados de género masculino que votaron por IOT o IA, 
    #cuya edad este entre 25 y 50 años inclusive.
        if genero  == "Masculino" and tecnologia != "RV/RA" and edad >= 25 and edad <= 50:
            contador_masculinos_IOT_IA += 1

    #Porcentaje de empleados que no votaron por IA,
    #siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
        if tecnologia != "IA" and genero != "Femenino" or edad > 33 and edad < 40:
            contador_empleados_no_ia += 1 
        
        #Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.
        #(la consigna esta rara redactada, no se si habla en plural o singular)
        #(asi que voy a buscar solo uno :P )
        if i == 0 or edad > mayor_edad_masculino:
            mayor_edad_masculino = edad
            nombre_masculino_mayor = nombre 
            tecnologia_masculino_mayor = tecnologia
#Porcentaje de empleados que no votaron por IA,
#siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.            
porcentaje_empleados_no_ia = contador_empleados_no_ia / 10 * 100 

print(f"Los empleados masculinos que votaron por IOT O IA de edad entre 25 y 40 fueron {contador_masculinos_IOT_IA}")
print(f"El porcentaje de empleados que no votaron por IA excluyendo femeninos y edad entre 33 y 40 fueron {porcentaje_empleados_no_ia}%")
print(f"El nombre del empleado masculino con mayor edad es {nombre_masculino_mayor} la tecnologia votada fue {tecnologia_masculino_mayor}")

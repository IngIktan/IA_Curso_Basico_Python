# Daniel Alejandro Flores Sepulveda 21310203
# Programa que crea y llama funciones con argumentos, *args y **kwargs.

 # Función que toma argumentos fijos (nombre y edad) y los imprime
def saludar_persona(nombre, edad): #Deffinimos el el nombre y la edad para saludar a la persona 
    print(f"Hola, {nombre}. Tienes {edad} años.") #de imprime el nombre de la funcion para saludar a la persona 

# toma *args para sumar números arbitrarios y muestra el resultado
#todo esto para poder usar los *agrs 
def suma_numeros(*args): 
    resultado = sum(args)
    print(f"La suma de los números es: {resultado}")

# Función que toma **kwargs para imprimir información sobre un diccionario arbitrario
def imprimir_info_diccionario(**kwargs):
    print("Información del diccionario:")
    for clave, valor in kwargs.items(): #se crea un metodo for
        print(f"{clave}: {valor}")

# Llamadas a las funciones con diferentes argumentos y parámetros
saludar_persona("Juan", 25) #Llaamos  a la función de  saludar_persona utilizando los  argumentos "Juan" y 25.

suma_numeros(1, 2, 3, 4, 5) #Llama a la función suma_numeros con los argumentos 1, 2, 3, 4 y 5.

info = {"Nombre": "Sofía", "Edad": 30, "Ciudad": "Cali"}
imprimir_info_diccionario(**info) # se le llama a la función imprimir_info_diccionario con el diccionario info desempaquetado usando **info.

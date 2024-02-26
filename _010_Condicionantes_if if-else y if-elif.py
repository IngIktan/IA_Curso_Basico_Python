# Daniel Alejandro Flores Sepulveda 21310203
# Ejemplo simple de uso de las estructuras de control if, if-else y if-elif usando un Imput para obtener la edad.

# Solicitar al usuario que ingrese su edad
edad = int(input("Ingresa tu edad: "))  # La función input() obtiene una cadena, y se convierte a entero usando int()

#Uso basico de If 
if edad >= 18: #Si la edad es mayor o igual a 18 Años  entonces e ejecutara y se mostrata el mensaje 
    print("Eres mayor de edad.")
    print("Puedes votar y realizar otras actividades para adultos.")
# Fin del bloque if
#Vamos a utilizar un if-else 
# Ejemplo de if-else: Verificar si la edad es mayor o igual a 21
if edad >= 21: #Si la edad es mayot o igual a 21 entonces se moestrara el mensaje 
    print("Eres legalmente autorizado para consumir alcohol.")
else: #En caso de no ser mayor o igual a 21 se condiciona a aparecer el siguiente mensaje 
    print("No eres legalmente autorizado para consumir alcohol.")
# Fin del bloque if-else
#En el caso de los if-elif tenemos una cantidad de opciones que nosotros queramos para poder poner condicionantes 
# Ejemplo de if-elif: Clasificar la edad en categorías
if edad < 13:
    print("Eres un niño.")
elif 13 <= edad < 18:
    print("Eres un adolescente.")
elif 18 <= edad < 65:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")
# Fin del bloque if-elif

#Lo malo de utilizar este codigo sin usar un bucle es que hay que compilar cada vez para que pregunte nuevamente la edad 
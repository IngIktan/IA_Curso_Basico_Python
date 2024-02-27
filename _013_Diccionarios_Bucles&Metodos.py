# Daniel Alejandro Flores Sepulveda 21310203
# Definición de diccionarios para marcas de carros con modelos y años asociados. Se uan metodos de consulta, bucles y eliminar elementos dentro del diccionario 
#Diccionario 1
Ford = {
    "Focus": "2002",
    "Escort": "1996",
    "Explorer": "2005"
}
#Diccionario 2
VW = {
    "Pointer": "2000",
    "Jetta": "2012"
}
#Diccionario 3
Volvo = {
    "S40": "2007",
    "S60": "2009"
}

# Consultar el año del modelo "Focus" en el diccionario Ford
Consulta = Ford["Focus"] #el metodo consulta y entre [] se usa para buscar los atributos
print("El año del Ford Focus dentro de nuestro diccionario es:", Consulta)

# Crear una copia del diccionario Ford utilizando el constructor dict
Muestra_marca = dict(Ford) #Ussando el metodo dict se  imprime todo lo existente dentro de ese diccionario 
print("Vamos a imprimir lo que hay en Ford con el método dict:", Muestra_marca)

# Imprimir la lista de modelos de carros VW utilizando un bucle for
print("La lista de carros VW usando el método for es:") #Se usa el metodo for para poder determinar la canntidad de carros que hay 
for x in VW:
    print(x)

# Imprimir la lista de modelos de carros VW utilizando un bucle for
print("La lista de carros VW usando el método for es:")#Se usa este seguindo metodo for para encontrar los años que hay dentro de VW 
for x in VW:
    print(VW[x])

# Obtener la cantidad de modelos y años en el diccionario Volvo utilizando la función len()
print("Vamos a ver ahora en el diccionario Volvo cuántos modelos y años tenemos:", len(Volvo))

# Intento incorrecto: Usar dict como si fuera una función en lugar de un constructor
# Corregido: Utilizar dict(Volvo) para crear una copia del diccionario Volvo
dame = dict(Volvo)
print("Vamos a imprimir la lista total de los elementos que hay dentro de Volvo:", dame)

# Eliminar el modelo "S40" del diccionario Volvo
del Volvo['S40']
print("Eliminamos el S40 de Volvo porque ya se vendió. Nuevo contenido de Volvo:", Volvo)


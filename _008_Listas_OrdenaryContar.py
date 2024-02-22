# Daniel Alejandro Flores Sepulveda 21310203
# Este programa demuestra cómo trabajar con listas de marcas de carros y utilizar algunos métodos como .short, .short reveres = true y obtener la longitud de la lista .

m = ["Toyota", "Honda", "Ford", "Chevrolet", "Tesla"]  # Crear una lista de marcas de carros

print("Lista original de marcas de carros: \n", m) # Imprimir la lista original de marcas de carros

m.sort()  # Ordenar la lista de marcas de carros alfabéticamente utilizando el método .sort()
print("\nLista de marcas de carros ordenada alfabéticamente:\n", m)#se imprime la lista de las marcas de carros 

m.sort(reverse=True)  # Ordenar la lista de marcas de carros en orden inverso utilizando el método .sort(reverse=True)
print("\nLista de marcas de carros ordenada en orden inverso:\n", m) #se ordena la lista de las marcas de carros 

longitud_lista = len(m)  # Obtener la longitud de la lista de marcas de carros utilizando el método len()
print("\nNúmero total de marcas de carros:", longitud_lista) #se imprime la longitud de la lista de marcas de carros

if len(m) > 0: # Utilizar el método len() para verificar si la lista está vacía
    print("\nLa lista de marcas de carros no está vacía.") 
else:
    print("\nLa lista de marcas de carros está vacía.")

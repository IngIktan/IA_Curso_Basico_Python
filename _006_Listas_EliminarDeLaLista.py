# Daniel Alejandro Flores Sepulveda 21310203
# Esta práctica se borraran elementos de un arreglo con diferentes metodos del, remove y pop 
superheroes = ["Spider-Man", "Iron Man", "Wonder Woman", "Batman", "Superman"]  # Crear una lista de superhéroes

print("Lista de Superhéroes:", superheroes)#Se imprime la lista de superheroes

del superheroes[0]#Con el metodo delete se borra la posicion que se da en los corchetes 
print("Se borra la primera posicion de el arreglo ", superheroes)#se imprime que efectivamente se borra 

if "Batman" in superheroes:#se agrega un if en caso de que no se encuentre el valor buscado dentro de la lista si es asi continua 
    superheroes.remove("Batman")  # Eliminar un superhéroe por su valor
    print("Se borra Batman. ", superheroes) #se imprime la lista de que se borra batman 
else:
    print("Batman no está en la lista de superhéroes.")#si no se encuentra el valor dentro del arreglo se muestra el error de que no se encuentra en la lista

superheroes.pop()#con el metodo pop se borra el ultimo de la cadena 
print ("Se borra el ultimo de la cadena", superheroes)#se imprime que se borro el ultimo de la cadena 


# Daniel Alejandro Flores Sepulveda 21310203
# Este programa muestra el uso de las tuplas y como se utilizan. Las tuplas son como la lista pero estas no se pueden modificar  

tupla =('Focus', 2001, 'Escort', 1996, 'Contur', 2000) #se crea una tupla de carrros y sus respectivos años  
print(tupla)#se imprime la tupla 

print("Se imprime la primera posición de la tupla:\t", tupla[0]) #Se imprime una posicion en especifico de dicha tupla 

print("La diferencia entre años del", tupla[0], "y de", tupla[2], "es de:\t", tupla[1] - tupla[3])#Tambien se imprime la posicion de dicha tupla pero tambien se puede operar con los numeros dentro de de la tuplas

#ahora vamos a convertir la tupla a una lista solo por que podemos hacerlo 
lista = list (tupla) #se crea una variable lista con la cual se almacena la informacion de la tupla creando una lista con la informacion 
print ("Ahora haz hecho una lista con los valores de la tupla \n\t ", lista)#se imprime el valor de la lista 
lista. append ("Ya modifique la lista ") #se modifica la lista como comprovacion

#Ahora con la lista vamos a crear una segunda tupla pero con los valore de la lista 
tupla_convertida = tuple(lista) #ahora en la variable de tupla convertida se guarda la informacion de la lista 
print("Ahora ya tienes una tupla modificada con la lista: \n\t", tupla_convertida)#se imprime la tupla ya modificada


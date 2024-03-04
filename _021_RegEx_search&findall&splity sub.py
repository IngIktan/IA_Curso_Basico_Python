#Daniel Alejandro Flores Sepulveda 2131203
#En esta practica tenemos que utilizar diferenes patrones de textos a través de los cuales podemos establecer la estructura que debe poser una cadena de texto.

import re

# Cadena de texto de ejemplo
texto = "Flor azul, espina roja, flor azul, espina roja. ¡Esto sería más fácil si no fuera daltónico 12345!" #Esta frase la utilizamos para poder jugar y probar las funciones que vamos apresentar a continuyacion 

# Buscamos una palabra que tenga 'p' y 't'
s = re.findall("p.t.", texto)
print(s)

# se cuarfa la oraciuone con caracteres dadops 
s = re.findall("^esp", texto)
print("Guardamos el valor si la oración empieza con 'esp' refiriendonos a espinas en la frase a buscar \n",s)
# se suprimen los nuemros que haya 
res = re.findall("\D", texto)
print("Suprimimos donde haya números \n", res)

# Imprimimos todos los caracteres alfanuméricos
res = re.findall("\w", texto)
print("Se imprimen todos los caracteres alfanumericos \n", res)

# Se eli9minan todoas los caracteres alfanumericos en este caso tenemos hasta el final numeros 
res = re.findall("\W", texto)
print("Sin caracteres: \n", res)
# Si acaba con 'roja' lo guardamos
s = re.findall("oja$", texto)
print("Si acaba con 'roja' lo guardamos \n", s)

# si se tienen coincidencias se imprime 
s = re.findall("pa+", texto)
print("Buscamos coincidencias donde se tenga una 'a' y una o más coincidencias de 's'", s)

#  al buscar la palabnra se imprime como respuesta 
res = re.findall(r"\broja\b", texto)
print("Buscamos la palabra completa 'roja'\n", res)



#Se meustra la ultima palabra 
res = re.findall("\w+\Z", texto)
print("La ultima palanbra es: \n", res)
#buscamos las palabras que esten desde la letra d a o 
res = re.findall("[d-o]", texto)
print(res)

# Daniel Alejandro Flores Sepulveda 21310203
# Ejemplo de uso de bloques while y for, se usa while 2 for 2. 

# Ejemplo con while
c_while = 0
l_while = 5
#vamos a hacer el primer ejemplo con el metodo de bucle while 
while c_while < l_while:  # Mientras el contador sea menor al límite
    print(f"Usando while: Iteración {c_while}")#se imprime la iteracion de la variable contador while 
    c_while += 1  # Incrementar la variable contador

# Segundo ejemplo con el metodo de  while True
c_while_true = 0#se crea la variable de contador while true 
l_while_true = 5#se crea la variable de limite while true

while True:  # Bucle infinito
    print(f"Usando while True: Iteración {c_while_true}")
    c_while_true += 1  # Incrementar el contador
    if c_while_true >= l_while_true:
        break  # Salir del bucle cuando se alcanza el límite
# Tercer ejemplo con el metodo de bucle for 
limite_for = 5 #se crea un limite para la va0riable for 
for contador_for in range(limite_for):  # Iterar sobre un rango de 0 a limite for - 1
    print(f"Usando for: Iteración {contador_for}")#se imprime el resultado 
# Cuarto ejemplo con el metodo de bucle for to
limite_for_to = 5#Se crea un limite para nuestra condicionente for to 
for_to_contador = 0 #se crea un inicio de nuestroi contador 
for_to_limite = 5#se crea un liimite pera nuesttro contador for to limit 
for _ in range(for_to_limite):  # Utilizando for to con una variable de control externa
    print(f"Usando for to: Iteración {for_to_contador}") #se imprime el resultado 
    for_to_contador += 1  # Incrementar la variable de control hasta llegar al limite 
# Daniel Alejandro Flores Sepulveda 21310203
# Programa que pregunta al usuario su fecha de nacimiento y nombre, y verifica si están en las listas ya sea en Tulpa o en lista.

# Lista de años de nacimiento del 2000 al 2010
nacimiento = list(range(2000, 2011))

# Tupla de nombres
tupla_nombres = ("Juan", "Daniel", "Alejandra", "Chava", "Aldo", "Victor")

# Cuestionario utilizando un bucle for
for _ in range(1):  # Se repite el cuestionario 1 ves 
    # Solicitar al usuario su fecha de nacimiento
    print("\t******Bienvenido a los juegos del Hambre*****\n")
    print("\t----Quieres saber si estas dentro de ellos?----\n")
    fecha_nacimiento = int(input("Ingresa tu año de nacimiento (2000-2010): "))#se elije hasta el 2010 por que aun recuerdo esos años como buenos años
    # Verificar si la fecha de nacimiento está en la lista 
    if fecha_nacimiento in nacimiento: #Si esta en la lista se imprime que estas dentro de la lista 
        print("Estás dentro de la lista de años de nacimiento.") #Con este mensaje se comprueba que estas dentro de la lista que hice 
    else:#En caso de que no es te entonces se muestra el mensaje de que no esta dentro de la lista de los seleccionados 
        print("No estás en la lista de años de nacimiento.")#\

    nombre = input("Ingresa tu nombre: ") # Solicitar al usuario su nombre para ver si es candidato a los jeugos del hambre  
    # Verificar si el nombre está en la tupla
    if nombre in tupla_nombres:#Con esto se comprueba que esten dentro de la tupla lo siguente a verificar dentro de la practica 
        print("¡Estás dentro de la Tupla de sorteados!")#en caso de que tu nombre aparezca dara el siguiente mensaje 
    else:
        print("No estás dentro de la Tupla de sorteados.") #En caso de que no aparezca el nombre dara este mensaje

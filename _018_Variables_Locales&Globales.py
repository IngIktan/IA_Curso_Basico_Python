# Daniel Alejandro Flores Sepulveda 21310203
# Programa de ejemplo con variables globales y locales en Python.

# Variable global
global_variable = "Soy sumamente importante en el mundo y todos me conocen" #se crea una variable global dentro de esta se encurnta un mensaje para definir que es glonbal 

def funcion_con_variable_local(): # definicmos una funcion de la variable local
    # Variable local
    local_variable = "Apenas estoy creciendo, no soy tan famoso, soy famosillo"
    print(local_variable)

# Imprimir la variable global
print(global_variable)

# Llamar a la función que imprime la variable local
funcion_con_variable_local()
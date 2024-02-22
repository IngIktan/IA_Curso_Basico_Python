# Daniel Alejandro Flores Sepulveda 21310203
# Esta práctica realiza operaciones básicas (suma, resta, multiplicación, división y exponencial) con un número entero y un número flotante.

numero_entero = 10      # Definir los dos números a utilizar
numero_flotante = 5.5

suma = numero_entero + numero_flotante  # Realizar la suma de los dos números
print("Suma:", suma)   # Imprimir el resultado de la suma

resta = numero_entero - numero_flotante # Realizar la resta del número entero menos el número flotante
print("Resta:", resta) # Imprimir el resultado de la resta

multiplicacion = numero_entero * numero_flotante  # Realizar la multiplicación de los dos números
print("Multiplicación:", multiplicacion)# Imprimir el resultado de la multiplicación
exponente = numero_entero ** numero_flotante  # Realizar la exponencial de los dos números
print("Exponente:", exponente)# Imprimir el resultado de la exponencial

if numero_flotante != 0:# Verificar si el número flotante es diferente de cero antes de realizar la división
    division = numero_entero / numero_flotante  # Realizar la división del número entero entre el número flotante
    print("División:", division)# Imprimir el resultado de la división
else:
    print("Error: No se puede dividir por cero.")  # Imprimir un mensaje de error en caso de intentar dividir por cero

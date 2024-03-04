#Daniel Alejandro Flores Sepulveda  21310203
# Utiliza un bucle while True para repetir el proceso hasta que el usuario decida dejar de llenar el formulario. 

while  True: # Se inicia un bucle infinito
     

    try: # Intenta realizar las siguientes acciones
        # Solicitar un número al usuario
        
        numero = input("Dime un numero que numero estas pensando : ")
        
        numero = int(numero) # Intentar convertir la entrada a un número entero
        
        print("El número que pensaste es:", numero)# Imprimir el mensaje con el número ingresado
    except ValueError:
        
        print("Error: Ese no es un número, intenta nuevamente .") # Capturar la excepción si la entrada no es un número

    finally:
        # Se ejecuta siempre, independientemente de si hubo una excepción o no
        # Preguntar al usuario si quiere seguir llenando el formulario
        respuesta = input("¿Quieres seguir llenando el formulario? (Sí/No): ").lower()
        if respuesta != 'si':
            # Si la respuesta no es 'si', salir del bucle
            print("¡Gracias por participar!")
            break


# Daniel Alejandro Flores Sepulveda 21310203
# Programa que importa el módulo math y utiliza funciones lambda para calcular el volumen de una esfera.
import math  # Importar el módulo math mediante la palabra clave Import
radio = 40# Definir el radio de la esfera en este caso 40 pero puede ser cualquiera 
calcular_volumen = lambda r: (4/3) * math.pi * pow(r, 3) # Función lambda para calcular el volumen de la esfera
# Calcular el volumen utilizando la función lambda
volumen_esfera = calcular_volumen(radio)
# Imprimir el resultado
print(f"El volumen de la esfera con radio {radio} cm es: {volumen_esfera} cm³")
# se usan idealmente cuando necesitamos hacer algo simple y estamos más interesados en hacer el trabajo rápidamente en lugar de nombrar formalmente la función
# Daniel Alejandro Flores Sepulveda 21310203
# Clase Carros que define un modelo y año, con método de impresión de datos.

class Carros:
    def __init__(self, modelo='', year=''): #self en el método __init__ hace referencia a la instancia actual de la clase
        # Método especial de inicialización (__init__) que se llama cuando se crea una nueva instancia de la clase.
        # Permite inicializar los atributos de la instancia.
        self.modelo = modelo 
        self.year = year

    def imprime_datos(self):
        # Método que imprime los datos del carro.
        print('Nombre:', self.modelo, '\nApellidos:', self.year)
#una instancia es un objeto específico creado a partir de una clase. Una clase es una plantilla o un "molde" que define las propiedades 
#y comportamientos comunes que tendrán los objetos de ese tipo.
# Crear una instancia de la clase Carros utilizando el método __init__
carro = Carros(modelo='Ford', year='2001')
carro.imprime_datos()
# Daniel Alejandro Flores Sepulveda 21310203
# Programa de ejemplo con clases, método __init__, herencia y eliminación de objetos con ejemplo de clase vehiculo .

# Clase base que define un vehículo
class Vehiculo:  # Define una clvase llamada Vehiculo, que servirá como plantialla para crear objetos relacionados con vehículos.

    def __init__(self, marca='', modelo='', año=0): # Método especial de inicialización (__init__) que se llama automáticamente al crear una nueva instancia de la clase.
        # Permite inicializar los atributos del objeto.
        self.marca = marca # asigna el valosr del parámetro 'marca' al atributo 'marca' de la instancia (objeto) actual.
        self.modelo = modelo # asigna el valorr del parámetro 'modelo' al atributo 'modelo' de la instancia actual.
        self.año = año # asigna el valor del parámetro 'año' al atributo 'año' de la instancia actual.


    def imprimir_info(self): 
        # Método que imprime la informacaión del vehícsulo.
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}")

# Clase derivada que hereda de la clase Vehiculo
class Automovil(Vehiculo):
    def __init__(self, marca='', modelo='', año=0, puertas=0):
        # Llamada al método __init__ de la clase base para inicializar atribautos comunes.
        super().__init__(marca, modelo, año)
        # Nuevo atributo especíafico para Automovil
        self.puertas = puertas

# Clase derivada que hereda de la clase Vehiculo (sin agregar nuevos atributos)
class Motocicleta(Vehiculo): 
    pass  # La palabra clave 'pass' se utiliza para indicar ques la clase está vacía, ya que no se agregan atributos ni métodos adicionales.

# Crear instancias de las clases
auto = Automovil(marca='Toyota', modelo='Corolla', año=2022, puertas=4) #se instaasncia la clase Automovil con la variable auto se le da  a los atributos de la clase datos para despues interactuar con ellos 
moto = Motocicleta(marca='Honda', modelo='CBR', año=2021)

# Imprimir información de los vehículos
auto.imprimir_info() #se imprimre ala informacion de la un auto 
moto.imprimir_info() #se imprime la informacion de sla moto


del auto # Eliminar una insutancia (objeto)

    # Daniel Alejandro Flores Sepulveda 21310203
    # Ahora entramos a POO vamos a definir una clase con sus objetos y mediante instanciacion vamos a mandarlos llamar para otorgarles un valor
class Carros: #Se crea la clase Carros 
    modelo = '' #se define un moedlo 
    year = ''  #se define un año de fabricacion
    #se definden vacios ya que mas adelante se les dara un dato 

    def imprime_datos(self): # el self se usa para referirse al objeto actual de una clase
        print('Modelo del carro:', self.modelo, '\nAño del carro:', self.year) #En este caso se refiere al objetoo modelo y al ofjeto carro 

# Crear una instancia de la clase Carros
carro = Carros() #se crea una variable para instanciar a los objetos de la clase Carros  
carro.modelo = 'Ford' #a la variable variable carros se instancia de la clase el objeto modelo y se le asigna un vlaor 
carro.year = '2001' #ahora se instancia el objeto de la clase para darle el valor de 2001 
carro.imprime_datos() #se imprimen los valores 



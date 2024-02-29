# Daniel Alejandro Flores Sepulveda 21310203
# En este programa vamos a colocar fechas pro datatime y por strftime 

import datetime #Se importa la liberia 

fecha = datetime.datetime.now ()   #Con esta manera se imprime la fehca pero de una manera poco agradable  
print ("Asi se ve la fehca por defoult" ,fecha) #se imprime la fecha pero no nos gusta 
fecha1= datetime.datetime(2024,2,27,20,5) #se crea una variable con el formato que nosotros queramos que se imprima y se ve asi 
 #se impirme la fehca con el formato pedido 
print ("Como no nos gusta como se ve esto vamos a mejorarlo y se vera como Año/Mes/Dia Hr/mm    ", fecha1)

# Formatear la fecha específica utilizando strftime
fecha2 = fecha1.strftime("%Y/%B/%A %R")
print("Fecha específica mas perrona:", fecha2)
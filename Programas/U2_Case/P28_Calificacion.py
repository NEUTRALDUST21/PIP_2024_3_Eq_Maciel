
archivo = open("../Archivos/datos_sensor_temperaturas.csv")

contenido = archivo.readlines()
print(contenido)

datos = [float(i) for i in contenido] # y
print(datos)

x = [i for i in range(1, 16, 1)]

from matplotlib import pyplot as plt
plt.plot(x,datos, marker="o", color="green") #visualiza datos, signo y  colores
plt.xticks(x) #visualiza numeros de abajo
plt.grid(True) #visualiza el grid
plt.show() #visualiza la grafica

nombre_instancia = "../Archivos/Datos_Calificaciones.csv" #ruta del archivo
archivo = open(nombre_instancia) #abre el archivo
contenido_archivo = archivo.readlines() #lee el contenido del archivo
print(contenido_archivo)

instancia = [linea.split(',') for linea in contenido_archivo] # separa cada linea en columnas
del instancia[0] #elimina el encabezado
instancia = [[registro[0], int(registro[1])] for registro in instancia] #convierte segunda columna en int
print(instancia)

instancia.sort(key=lambda x: x[1], reverse=True) ##ordenamiento lambda por la segunda columna
print(instancia)

print("Alumnos con calificaciones más alta: ")
print("Alumno con calificacion más alta: " + instancia[0][0])
for i in range(1, len(instancia)):
    calificacion = instancia[i][1]
    if instancia[0][1] == calificacion:
        print("Alumno con calificacion más alta: " + instancia[i][0])
    else:
        break
    del instancia[0]



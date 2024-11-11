def cargar_preguntas():
    archivo = open("../Archivos/Preguntas.txt")
    contenido_archivo = archivo.readlines()
    #print(contenido_archivo)
    preguntas = [i.split(",") for i in contenido_archivo]
   # print(preguntas)
    #for i in preguntas:
        #print(i)
    estructura_preguntas = [[i[0], i[1], i[2:len(i)]] for i in preguntas]
    #print(estructura_preguntas)
    #for i in estructura_preguntas:
       # print(i)
    return estructura_preguntas

if __name__ == "__main__":
    preguntas = cargar_preguntas()
    print("Preguntas Cargadas")
    for i in preguntas:
        print(i)


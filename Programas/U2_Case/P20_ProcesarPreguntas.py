import P19_LeerPreguntas as p

preguntas = p.cargar_preguntas()
print("Preguntas Cargadas")
for i in preguntas:
    print(i)

print("Preguntas Desordenadas Con Opciones Desordenas:")
import random as rnd
rnd.shuffle(preguntas) # desordena las preguntas
for pregunta in preguntas: # desordena las opciones
    rnd.shuffle(pregunta[2])
    print(pregunta)

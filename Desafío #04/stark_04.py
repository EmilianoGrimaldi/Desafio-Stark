from data_stark import *
from funciones_stark import *


heroes = []
copiar_datos(lista_personajes,heroes)
stark_normalizar_datos(heroes,"altura",float)
stark_normalizar_datos(heroes,"peso",float)
stark_normalizar_datos(heroes,"fuerza",float)


# 1.1. Crear la función ‘extraer_iniciales’ que recibirá como parámetro:
# ● nombre_heroe: un string con el nombre del personaje
# La función deberá devolver a partir del parámetro recibido un nuevo string con
# las iniciales del nombre del personaje seguidos por un punto (.)
# ● En el caso que el nombre del personaje contenga el artículo ‘the’ se
# deberá omitir de las iniciales
# ● Se deberá verificar si el nombre contiene un guión ‘-’ y sólo en el caso
# que lo tenga se deberá reemplazar por un espacio en blanco
# La función deberá validar:
# ● Que el string recibido no se encuentre vacío
# Devolver ‘N/A’ en caso de no cumplirse la validación
# Ejemplo de la salida de la función para Howard the Duck:
# H.D.

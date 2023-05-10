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
def extraer_iniciales(nombre_heroe:str)->str:
    
    if type(nombre_heroe) == str and len(nombre_heroe) > 0:
        
        partes_nombre = nombre_heroe.split()
        nombre_sin_articulo = ""
        iniciales = ""
        for palabra in partes_nombre:
            if palabra == "the" or palabra == "The":
                palabra = " "

            nombre_sin_articulo += palabra
        
        for letra in nombre_sin_articulo:
            if letra == "-":
                letra = " "

            if letra >= "A" and letra <= "Z":
                iniciales += letra + "."
        
        nombre_actualizado = iniciales.strip()
                
        return nombre_actualizado
    
    else:
        return "N/A"
    


# 1.2. Crear la función ‘definir_iniciales_nombre’ la cual recibirá como parámetro:
# ● heroe: un diccionario con los datos del personaje
# La función deberá agregar una nueva clave al diccionario recibido como
# parámetro. La clave se deberá llamar ‘iniciales’ y su valor será el obtenido de
# llamar a la función ‘extraer_iniciales’
# La función deberá validar:
# ● Que el dato recibido sea del tipo diccionario
# ● Que el diccionario contengan la clave ‘nombre’
# En caso de encontrar algún error retornar False, caso contrario retornar True

def definir_iniciales_nombre(heroe:dict, clave_nueva:str)->bool:
    
    if type(heroe) == dict and "nombre" in heroe and type(clave_nueva) == str:
        heroe[clave_nueva.lower()] = extraer_iniciales(heroe["nombre"])
        flag_salio_bien = True
    else:
        flag_salio_bien = False
    
    return flag_salio_bien    

#1.3. Crear la función ‘agregar_iniciales_nombre’ la cual recibirá como
# parámetro:
# ● lista_heroes: lista de personajes
# Se deberá validar:
# ● Que lista_heroes sea del tipo lista
# ● Que la lista contenga al menos un elemento
# La función deberá iterar la lista_heroes pasándole cada héroe a la función
# definir_iniciales_nombre.
# En caso que la función definir_iniciales_nombre() retorne False entonces se
# deberá detener la iteración e informar por pantalla el siguiente mensaje:
# ‘El origen de datos no contiene el formato correcto’
# La función deberá devolver True en caso de haber finalizado con éxito o False
# en caso de que haya ocurrido un error

def agregar_iniciales_nombre(lista_heroes:list):
    if type(lista_heroes) == list and len(lista_heroes) >= 1:
        flag_salio_bien = True
        for heroe in lista_heroes:
            if not definir_iniciales_nombre(heroe,"iniciales"):
                flag_salio_bien = False
                break
        
        if not flag_salio_bien:
            print("El origen de datos no contiene el formato correcto")
        else:
            return flag_salio_bien


# nombre_heroe = "Howard the Duck"
# print(definir_iniciales_nombre(heroes[0],"iniciales"))
# print(heroes[0])
# if agregar_iniciales_nombre(heroes):
#     for heroe in heroes:
#         print(heroe)

# 1.3. Crear la función ‘stark_imprimir_nombres_con_iniciales’ la cual recibirá como parámetro:
# ● lista_heroes: la lista de personajes
# La función deberá utilizar la función agregar_iniciales_nombre’ para añadirle las iniciales a los diccionarios contenidos en la lista_heroes Luego deberá imprimir la lista completa de los nombres de los personajes seguido de las iniciales encerradas entre paréntesis ()
# Se deberá validar: 
# ● Que lista_heroes sea del tipo lista
# ● Que la lista contenga al menos un elemento
# Delante de cada nombre se deberá agregar un asterisco ‘*’ (de forma de
# viñeta) seguido de un espacio.
# Ejemplo de salida:
# * Howard the Duck (H.D.)
# * Rocket Raccoon (R.R.)
# …
# La función no retorna nada

def stark_imprimir_nombres_con_iniciales():
    pass
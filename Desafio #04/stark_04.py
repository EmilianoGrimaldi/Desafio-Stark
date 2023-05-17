#FUNCIONES
from funciones_stark import *
import re
import json


"""
1. Primera Parte
1.1. Crear la función "imprimir_menu_desafio_5" que imprima el menú de
opciones por pantalla (las opciones son las que se van a utilizar para
acceder a la funcionalidad de los puntos A hasta el O y Z para salir).
Reutilizar la función 'imprimir_dato' realizada en una práctica anterior.
"""

def imprimir_menu_desafio_5()->None:
    
    imprimir_dato(" A -> Imprimir por consola el nombre de cada superhéroe de género M\n B -> Imprimir por consola el nombre de cada superhéroe de género F\n C -> El superhéroe más alto de género M\n D -> El superhéroe más alto de género F\n E -> El superheroe mas bajo de genero M\n F -> El superheroe mas bajo de genero F\n G -> Altura promedio de los superheroes genero M\n H -> Altura promedio de los superheroes genero F\n I -> El nombre de los superheroes mas altos y mas bajos de cada genero\n J -> Superheroes con cada tipo de color de ojos\n K -> Superheroes con cada tipo de color de pelo\n L -> Superheroes con cada tipo de inteligencia\n M -> Superheroes agrupados por color de ojos\n N -> Superheroes agrupados por color de pelo\n O -> Superheroes agrupados por inteligencia\n Z -> Salir")
    
""" 
1.2. Crear la funcion 'stark_menu_principal_desafio_5' la cual se encargará
de imprimir el menú de opciones y le pedirá al usuario que ingrese la
letra de una de las opciones elegidas, deberá validar la letra usando
RegEx y en caso de ser correcta tendrá que retornarla, Caso contrario
retornará -1. El usuario puede ingresar tanto letras minúsculas como
mayúsculas y ambas se deben tomar como válidas
Reutilizar la función 'imprimir_menu_Desafio_5'
"""

def stark_menu_principal_desafio_5()->None:
    imprimir_menu_desafio_5()
    opcion = input("Ingresar una opcion\n")
    patron_min_mayus = re.compile(r"[A-Za-z]")
    if re.match(patron_min_mayus,opcion):
        return opcion
    else:
        return -1

""" 
1.3. Crear la función 'stark_marvel_app_5' la cual recibirá por parámetro la
lista de héroes y se encargará de la ejecución principal de nuestro
programa. (usar if/elif o match según prefiera) Reutilizar las funciones
con prefijo 'stark_' donde crea correspondiente
"""
def stark_marvel_app_5(lista_heroes:list)->None:
    
    while True:
        if stark_menu_principal_desafio_5() != -1:
            match stark_menu_principal_desafio_5().upper():
                case "A":
                    pass
                case "B":
                    pass
                case "C":
                    pass
                case "D":
                    pass
                case "E":
                    pass
                case "F":
                    pass
                case "G":
                    pass
                case "H":
                    pass
                case "I":
                    pass
                case "J":
                    pass
                case "K":
                    pass
                case "L":
                    pass
                case "M":
                    pass
                case "N":
                    pass
                case "O":
                    pass
                case "Z":
                    break
                
""" 
1.4. Crear la función 'leer_archivo' la cual recibirá por parámetro un string
que indicará el nombre y extensión del archivo a leer (Ejemplo:
archivo.json). Dicho archivo se abrirá en modo lectura únicamente y
retornará la lista de héroes como una lista de diccionarios.
"""
def leer_archivo(nombre_archivo:str):
    with open(nombre_archivo, "r") as archivo:
        contenido = json.load(archivo)
        
    return contenido["heroes"]

heroes = leer_archivo("Desafio #04\data_stark.json")

""" 
1.5. Crear la función 'guardar_archivo' la cual recibirá por parámetro un
string que indicará el nombre con el cual se guardará el archivo junto
con su extensión (ejemplo: 'archivo.csv') y como segundo parámetro
tendrá un string el cual será el contenido a guardar en dicho archivo.
Debe abrirse el archivo en modo escritura+, ya que en caso de no
existir, lo creara y en caso de existir, lo va a sobreescribir La función
debera retornar True si no hubo errores, caso contrario False, además
en caso de éxito, deberá imprimir un mensaje respetando el formato:
.Se creó el archivo: nombre_archivo.csv
En caso de retornar False, el mensaje deberá decir: ‘Error al crear el
archivo: nombre_archivo’
Donde nombre_archivo será el nombre que recibirá el archivo a ser
creado, conjuntamente con su extensión.
"""
def guardar_archivo(nombre_archivo:str, contenido:str):
    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.writelines(contenido)

        print(f"Se creó el archivo: {nombre_archivo}")
        return True
    except:
        print(f"Error al crear el archivo: {nombre_archivo}")
        return False

""" 
1.6. Crear la función 'capitalizar_palabras' la cual recibirá por parámetro un
string que puede contener una o muchas palabras. La función deberá
retornar dicho string en el cual todas y cada una de las palabras que
contenga, deberán estar capitalizadas (Primera letra en mayúscula).
"""

def capitalizar_palabras(string:str):
    palabras = string.split()
    palabras_capitalizadas = []
    for palabra in palabras:
        palabras_capitalizadas.append(palabra.title())
    
    return " ".join(palabras_capitalizadas)

# print(capitalizar_palabras("hola como estas amigo"))

""" 
1.7. Crear la función 'obtener_nombre_capitalizado' la cual recibirá por
parámetro un diccionario el cual representará a un héroe y devolverá
un string el cual contenga su nombre formateado de la siguiente
manera:
Nombre: Venom
Reutilizar 'capitalizar_palabras'
"""

def obtener_nombre_capitalizado(heroe:dict)->str:
    nombre_capitalizado = capitalizar_palabras(heroe['nombre'])
    return nombre_capitalizado

"""
1.8. Crear la función 'obtener_nombre_y_dato' la cual recibirá por
parámetro un diccionario el cual representará a un héroe y una key
(string) la cual representará la key del héroe a imprimir. La función
devolverá un string el cual contenga el nombre y dato (key) del héroe a
imprimir.
El dato puede ser 'altura', 'fuerza', 'peso' O CUALQUIER OTRO DATO.
El string resultante debe estar formateado al estilo: (suponiendo que la
key es fuerza)
Nombre: Venom | Fuerza: 500
Reutilizar 'obtener_nombre_capitalizado'
"""
def obtener_nombre_y_dato(heroe:dict, key:str):
    nombre = obtener_nombre_capitalizado(heroe)
    nombre_dato = f"Nombre: {nombre:20s} | key: {heroe[key]}"
    return nombre_dato


# for heroe in heroes:
#     print(obtener_nombre_y_dato(heroe,"altura"))

""" 
2.1. Crear la función 'es_genero' la cual recibirá por parámetro un
diccionario que representará un héroe y un string el cual será usado
para evaluar si el héroe coincide con el género buscado (El string
puede ser M, F o NB). retornará True en caso de que cumpla, False
caso contrario.
"""

def es_genero(heroe:dict, genero_buscado:str):
    genero_buscado = genero_buscado.upper()
    if genero_buscado == "M" or genero_buscado == "F" or genero_buscado == "NB":
        if genero_buscado == heroe["genero"]:
            return True
    else:
        return False
    
""" 
2.2. Crear la función 'stark_guardar_heroe_genero' la cual recibira por
parámetro la lista de héroes y un string el cual representará el género
a evaluar (puede ser M o F). 
Deberá imprimir solamente los héroes o
heroínas que coincidan con el género pasado por parámetro y
además, deberá guardar dichos nombres en un archivo con extensión
csv (cada nombre deberá ir separado por una coma)
Reutilizar las funciones 'es_genero', 'obtener_nombre_capitalizado',
'imprimir_dato' y 'guardar_archivo'.
En el caso de 'guardar_archivo', cuando se llame a esta función el
nombre de archivo a guardar deberá respetar el formato:
heroes_M.csv, heroes_F.csv o heroes_NB según corresponda.
La función retornará True si pudo guardar el archivo, False caso
contrario.
"""
def stark_guardar_heroe_genero(lista_heroes:list, genero_evaluar:str):
    nombres_filtrados = []
    
    for heroe in lista_heroes:
        if es_genero(heroe,genero_evaluar):
            match genero_evaluar:
                case "M":
                    nombre_archivo = "heroes_M.csv"
                    nombre_capitalizado = obtener_nombre_capitalizado(heroe)
                    nombres_filtrados.append(nombre_capitalizado)
                    imprimir_dato(nombre_capitalizado)
                case "F":
                    nombre_archivo = "heroes_F.csv"
                    nombre_capitalizado = obtener_nombre_capitalizado(heroe)
                    nombres_filtrados.append(nombre_capitalizado)
                    imprimir_dato(nombre_capitalizado)
   
    if guardar_archivo(nombre_archivo,"\n".join(nombres_filtrados)):
        return True
    else:
        return False
print(stark_guardar_heroe_genero(heroes,"F"))

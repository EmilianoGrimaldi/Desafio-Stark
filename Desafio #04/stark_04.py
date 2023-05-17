#FUNCIONES
from funciones_stark import *
from funciones_calculos_stark import *
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

stark_normalizar_datos(heroes,"altura",float)
stark_normalizar_datos(heroes,"peso",float)
stark_normalizar_datos(heroes,"fuerza",int)

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
        with open(f"Desafio #04\{nombre_archivo}", "w") as archivo:
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
    nombre_dato = f"Nombre: {nombre:20s} | {key}: {heroe[key]}"
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
    
# print(stark_guardar_heroe_genero(heroes,"F"))

""" 
3.1. Basandote en la función 'calcular_min', crear la función
'calcular_min_genero' la cual recibirá como parámetro extra un string
que representa el género de la heroína/héroe a buscar. modificar un
poco la lógica para que dentro no se traiga por defecto al primer héroe
de la lista sino que mediante un flag, se traiga el primer héroe que
COINCIDA con el género pasado por parámetro. A partir de allí, podrá
empezar a comparar entre héroes o heroínas que coincidan con el
género pasado por parámetro. La función retornará el héroe o heroína
que cumpla la condición de tener el mínimo (peso, altura u otro dato)
"""
def calcular_min_genero(lista_heroes:list,key_heroe:str, genero:str)->dict:
    
    flag_primer_heroe_gen = False
    
    if len(lista_heroes) > 0 and type(key_heroe) == str and type(genero) == str:
        try:
            for heroe in lista_heroes:
                if heroe["genero"] == genero and not flag_primer_heroe_gen:
                    heroe_completo = heroe
                    flag_primer_heroe_gen = True
                    break
                
            for heroe in lista_heroes:
                if heroe["genero"] == genero:  
                    if heroe[key_heroe] <= heroe_completo[key_heroe]:
                        heroe_completo = heroe
    
            return heroe_completo
        except KeyError:
            print("Error! Esa clave no existe en el diccionario")
    else:
        print("Error! Los parametros son invalidos")
        

# print(calcular_min_genero(heroes, "altura", "F"))

""" 
3.2. Basandote en la función 'calcular_max', crear la función
'calcular_max_genero' la cual recibirá como parámetro extra un string
que representará el género de la heroína/héroe a buscar. modificar un
poco la lógica para que dentro no se traiga por defecto al primer héroe
de la lista sino que mediante un flag, se traiga el primer héroe que
COINCIDA con el género pasado por parámetro. A partir de allí, podrá
empezar a comparar entre héroes o heroínas que coincidan con el
género pasado por parámetro. La función retornará el héroe o heroína
que cumpla la condición de tener el máximo (peso, altura u otro dato)
"""

def calcular_max_genero(lista_heroes:list,key_heroe:str, genero:str)->dict:
    flag_primer_heroe_gen = False
    
    if len(lista_heroes) > 0 and type(key_heroe) == str and type(genero) == str:
        try:
            for heroe in lista_heroes:
                if heroe["genero"] == genero and not flag_primer_heroe_gen:
                    heroe_completo = heroe
                    flag_primer_heroe_gen = True
                    break
                
            for heroe in lista_heroes:
                if heroe["genero"] == genero:  
                    if heroe[key_heroe] >= heroe_completo[key_heroe]:
                        heroe_completo = heroe
                    
            return heroe_completo
        except KeyError:
            print("Error! Esa clave no existe en el diccionario")
    else:
        print("Error! Los parametros son invalidos")

# print(calcular_max_genero(heroes, "altura", "F"))

""" 
3.3. Basandote en la funcion 'calcular_max_min_dato', crear una funcion
con la misma lógica la cual reciba un parámetro string que
representará el género del héroe/heroína a buscar y renombrarla a
'calcular_max_min_dato_genero'. La estructura será similar a la ya
antes creada, salvo que dentro de ella deberá llamar a
'calcular_max_genero' y 'calcular_min_genero', pasandoles el nuevo
parámetro. Esta función retornará el héroe o heroína que cumpla con
las condiciones pasados por parámetro. Por ejemplo, si se le pasa 'F' y
'minimo', retornará la heroína que tenga el mínimo (altura, peso u otro
dato)
"""

def calcular_max_min_dato_genero(lista_heroes:list,calculo_realizar:str,key_heroe:str, genero:str)->dict:
    
    if len(lista_heroes) > 0 and type(key_heroe) == str and type(calculo_realizar) == str and type(genero) == str:
       if calculo_realizar == "minimo" or calculo_realizar == "maximo":
            match calculo_realizar:
                case "minimo":
                    heroe = calcular_min_genero(lista_heroes,key_heroe,genero)
                    return heroe
                case "maximo":
                    heroe = calcular_max_genero(lista_heroes,key_heroe,genero)
                    return heroe
       else:
           print("Error! No se indico correctamente el calculo a realizar")
    else:
        print("Error! Los parametros son invalidos")

# print(calcular_max_min_dato_genero(heroes,"minimo","altura","F"))

""" 
3.4. Basandote en la función 'stark_calcular_imprimir_heroe' crear la
función ‘stark_calcular_imprimir_guardar_heroe_genero’ que además
reciba un string el cual representará el género a evaluar. El formato de
mensaje a imprimir deberá ser estilo:
Mayor Altura: Nombre: Gamora | Altura: 183.65
Además la función deberá guardar en un archivo csv el resultado
obtenido.

Reutilizar: 'calcular_max_min_dato_genero', 'obtener_nombre_y_dato',
'imprimir_dato' y 'guardar_archivo'.

En el caso de 'guardar_archivo' el nombre del archivo debe respetar el
formato:
heroes_calculo_key_genero.csv
Donde:
● cálculo: representará el string máximo o mínimo
● key: representará cual es la key la cual se tiene que hacer el
cálculo
● genero: representará el género a calcular.
Ejemplo: para calcular el héroe más alto femenino, el archivo se
deberá llamar:
heroes_maximo_altura_F.csv
Esta función retornará True si pudo guardar el archivo, False caso
contrario
"""

def stark_calcular_imprimir_guardar_heroe_genero(lista_heroes:list,calculo_realizar:str,key_heroe:str,genero:str)->int:
           
    match calculo_realizar:
        case "maximo":
            mensaje = f"Mayor {key_heroe}"
        case "minimo":
            mensaje = f"Menor {key_heroe}"

    heroe_max_o_min = calcular_max_min_dato_genero(lista_heroes,calculo_realizar,key_heroe,genero)
    heroe_imprimir = obtener_nombre_y_dato(heroe_max_o_min,key_heroe)
    imprimir_dato(f"{mensaje}: {heroe_imprimir}")
    
    
    if guardar_archivo(f"heroes_{calculo_realizar}_{key_heroe}_{genero}.csv",heroe_imprimir):
        return True
    else:
        return False
    

# stark_calcular_imprimir_guardar_heroe_genero(heroes,"minimo", "peso", "M")

""" 
4.1. Basandote en la función 'sumar_dato_heroe', crear la función llamada
'sumar_dato_heroe_genero' la cual deberá tener un parámetro extra
del tipo string que representará el género con el que se va a trabajar.
Esta función antes de realizar la suma en su variable sumadora,
deberá validar lo siguiente:
A. El tipo de dato del héroe debe ser diccionario.
B. El héroe actual de la iteración no debe estar vacío (ser
diccionario vacío)
C. El género del héroe debe coincidir con el pasado por
parámetro.
Una vez que cumpla con las condiciones, podrá realizar la suma. La
función deberá retornar la suma del valor de la key de los héroes o
heroínas que cumplan las condiciones o -1 en caso de que no se
cumplan las validaciones
"""
def sumar_dato_heroe_genero(lista_heroes:list,key_heroe:str, genero:str)->int:
    sumador = 0
    
    if len(lista_heroes) > 0 and type(key_heroe) == str and type(genero) == str:
        for heroe in lista_heroes:
            if type(heroe) == dict and heroe != {}:
                if heroe['genero'] == genero:
                    sumador += heroe[key_heroe]
            else:
                return -1
        
        return sumador 
    else:
        print("Error! Los parametros son invalidos")
        

# print(sumar_dato_heroe_genero(heroes,"fuerza","F"))

""" 
4.2. Crear la función 'cantidad_heroes_genero' la cual recibirá por
parámetro la lista de héroes y un string que representará el género a
buscar. La función deberá iterar y sumar la cantidad de héroes o
heroínas que cumplan con la condición de género pasada por
parámetro, retornará dicha suma.
"""

def cantidad_heroes_genero(lista_heroes:list, genero:str):
    contador_genero = 0
    
    for heroe in lista_heroes:
        if genero in heroe["genero"]:
            contador_genero += 1
    
    return contador_genero

# print(cantidad_heroes_genero(heroes,"F"))

""" 
4.3. Basandote en la función 'calcular_promedio', crear la función
'calcular_promedio_genero' la cual tendrá como parámetro extra un
string que representará el género a buscar. la lógica es similar a la
función anteriormente mencionada en el enunciado. Reutilizar las
funciones: 'sumar_dato_heroe_genero', 'cantidad_heroes_genero' y
'dividir'.
retornará el promedio obtenido, según la key y género pasado por
parámetro.
"""

def calcular_promedio_genero(lista_heroes:list,key_heroe_calcular:str,genero:str)->float:
    
    if len(lista_heroes) > 0 and type(key_heroe_calcular) == str and type(genero) == str:
        total = sumar_dato_heroe_genero(lista_heroes,key_heroe_calcular,genero)
        divisor = cantidad_heroes_genero(heroes,genero)
        resultado = dividir(total,divisor)
        return f"{resultado:.2f}"      
    else:
        print("Error! Los parametros son invalidos")

# print(calcular_promedio_genero(heroes, "fuerza", "F"))

""" 
4.4. Basandote en la función ‘stark_calcular_imprimir_promedio_altura',
desarrollar la función 'stark_calcular_imprimir_guardar_
promedio_altura_genero' la cual tendrá como parámetro extra un string
que representará el género de los héroes a buscar.

La función antes de hacer nada, deberá validar que la lista no esté
vacía. En caso de no estar vacía: calculará el promedio y lo imprimirá
formateado al estilo:
Altura promedio género F: 178.45

En caso de estar vacía, imprimirá como mensaje:
Error: Lista de héroes vacía.

Luego de imprimir la función deberá guardar en un archivo los mismos
datos. El nombre del archivo debe tener el siguiente formato:
heroes_promedio_altura_genero.csv
Donde:
A. genero: será el género de los héroes a calcular, siendo M y F
únicas opciones posibles.
Ejemplos:
heroes_promedio_altura_F.csv
heroes_promedio_altura_M.csv
Reutilizar las funciones: 'calcular_promedio_genero', 'imprimir_dato' y
'guardar_archivo'.
Esta función retornará True si pudo la lista tiene algún elemento y pudo
guardar el archivo, False en caso de que esté vacía o no haya podido
guardar el archivo.
"""
def stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes:list, genero:str)->int:
    tiene_elementos = False
    if len(lista_heroes) > 0:
        altura_promedio = calcular_promedio_genero(lista_heroes,"altura", genero)
        imprimir_dato(f"Altura promedio género {genero}: {altura_promedio}")
        tiene_elementos = True
    else:
        print("Error: Lista de héroes vacía")

    if genero == "M" or genero == "F":
        if guardar_archivo(f"heroes_promedio_altura_{genero}.csv", altura_promedio) and tiene_elementos:
            return True
        else:
            return False
        

# print(stark_calcular_imprimir_guardar_promedio_altura_genero(heroes, "F"))

""" 
5.1. Crear la función 'calcular_cantidad_tipo' la cual recibirá por parámetro
la lista de héroes y un string que representará el tipo de dato/key a
buscar (color_ojos, color_pelo, etc)

Antes de hacer nada, deberá validar que la lista no esté vacía. En caso
de estarlo devolver un diccionario con la siguiente estructura:
{
    "Error": “La lista se encuentra vacía”
}

La función deberá retornar un diccionario con los distintos valores del
tipo de dato pasada por parámetro y la cantidad de cada uno (crear un
diccionario clave valor).
Por ejemplo, si el tipo de dato fuese color_ojos, devolverá un
diccionario de la siguiente manera:
{
    "Celeste": 4,
    "Verde": 8,
    "Marron": 6
}
Reutilizar la función 'capitalizar_palabras' para capitalizar los valores
de las keys.
"""

def calcular_cantidad_tipo(lista_heroes:list, tipo_key:str):
    
    
    if len(lista_heroes) > 0:
        dic_clave_valor = {}
        for heroe in lista_heroes:
            
            palabra_cap = capitalizar_palabras(heroe[tipo_key])
            
            if palabra_cap in dic_clave_valor:
                dic_clave_valor[palabra_cap] += 1
            else:
                dic_clave_valor[palabra_cap] = 0
                
        dic_formateado_clave_valor = json.dumps(dic_clave_valor, indent = 4)
        return dic_formateado_clave_valor
    else:
        diccionario_error = {"Error":"La lista se encuentra vacia"}
        diccionario_formateado = json.dumps(diccionario_error,indent = 4)
        print(diccionario_formateado)
    
# print(calcular_cantidad_tipo(heroes,"color_ojos"))
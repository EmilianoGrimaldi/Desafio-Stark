from data_stark import *
from funciones_stark import *

import os

heroes = []
copiar_datos(lista_personajes,heroes)
# stark_normalizar_datos(heroes,"altura",float)
# stark_normalizar_datos(heroes,"peso",float)
# stark_normalizar_datos(heroes,"fuerza",float)

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

def stark_imprimir_nombres_con_iniciales(lista_heroes:list):
    if type(lista_heroes) == list and len(lista_heroes) >= 1:
        agregar_iniciales_nombre(lista_heroes)
        for heroe in lista_heroes:
            print(f"* {heroe['nombre']} ({heroe['iniciales']})")
        
        
#2.1. Crear la función ‘generar_codigo_heroe’ la cual recibirá como parámetros:
# ● id_heroe: un entero que representa el identificador del héroe.
# ○ NOTA: el valor de id_heroe lo vamos a generar recién el punto
# 2.3. Para probar la función podes pasarle cualquier entero
# ● genero_heroe: un string que representa el género del héroe ( puede
# tomar los valores ‘M’, ‘F’ o ‘NB’)
# La función deberá generar un string con el siguiente formato:
# GENERO-000…000ID
# Es decir, el género recibido por parámetro seguido de un ‘-’ (guión) y por
# último el identificador recibido. Todos los códigos generados deben tener
# como máximo 10 caracteres (contando todos los caracteres, inclusive el
# guión). Se deberá completar con ceros para que todos queden del mismo
# largo
# Algunos ejemplos:
# F-00000001
# M-00000002
# NB-0000010
# La función deberá validar:
# ● El identificador del héroe sea numérico.
# ● El género no se encuentre vacío y este dentro de los valores esperados
# (‘M’, ‘F’ o ‘NB’)
# En caso de no pasar las validaciones retornar ‘N/A’. En caso de verificarse
# correctamente retornar el código generado

def generar_codigo_heroe(id_heroe:int, genero_heroe:str):
    
    if type(id_heroe) == int and (genero_heroe == "M" or genero_heroe == "F" or genero_heroe == "NB") and len(genero_heroe.strip()) > 0:
        codigo_heroe = f"{genero_heroe}-{id_heroe}"
        ceros = ""
        
        while len(codigo_heroe) < 10:
            ceros += "0"
            codigo_heroe = f"{genero_heroe}-{ceros}{id_heroe}"
            if len(codigo_heroe) == 10:
                break
            
        return codigo_heroe
    else:
        return "N/A"
        
            
# 2.2. Crear la función ‘agregar_codigo_heroe’ la cual recibirá como parámetro:
# ● heroe: un diccionario con los datos del personaje
# ● id_heroe: un entero que representa el identificador del héroe.
# ○ NOTA: el valor de id_heroe lo vamos a generar recién el punto
# 2.3. Para probar la función podes pasarle cualquier entero
# La función deberá agregar una nueva clave llamada ‘codigo_heroe’ al
# diccionario ‘heroe’ recibido como parámetro y asignarle como valor un código
# utilizando la función ‘generar_codigo_heroe’
# La función deberá validar:
# ● Que el diccionario recibido como parámetro no se encuentre vacío.
# ● Que el código recibido mediante generar_codigo_heroe tenga
# exactamente 10 caracteres
# En caso de pasar las validaciones correctamente la función deberá retornar
# True, en caso de encontrarse un error retornar False

def agregar_codigo_heroe(un_heroe:dict,id_heroe:int):
    if len(un_heroe) > 0:
        codigo = generar_codigo_heroe(id_heroe,un_heroe["genero"])
        if len(codigo) == 10:
            un_heroe["codigo_heroe"] = codigo
            flag_salio_bien = True
    else:
        flag_salio_bien = False
    
    return flag_salio_bien 


#2.3. Crear la función ‘stark_generar_codigos_heroes’ la cual recibirá como
# parámetro:
# ● lista_heroes: la lista de personajes
# La función deberá iterar la lista de personajes y agregarle el código a cada
# uno de los personajes.
# El código del héroe (id_heore) surge de la posición del mismo dentro de la
# lista_heroes (comenzando por el 1).
# Reutilizar la función agregar_codigo_heroe pasándole como argumentos el
# héroe que se está iterando y el id_heroe
# Una vez finalizado imprimir por pantalla un mensaje como el siguiente:
# (## representa la cantidad de códigos generados):
# Se asignaron ## códigos
# * El código del primer héroe es: M-00000001
# * El código del del último héroe es: M-00001224
# La función deberá validar::
# ● La lista contenga al menos un elemento
# ● Todos los elementos de la lista sean del tipo diccionario
# ● Todos los elementos contengan la clave ‘genero’
# En caso de encontrar algún error, informar por pantalla: ‘El origen de datos no
# contiene el formato correcto’
# La función no retorna ningún valor.

def stark_generar_codigos_heroes(lista_heroes:list):
    flag_todo_ok = False
    contador_codigos = 0
    
    if len(lista_heroes) >= 1:
        for heroe in range(len(lista_heroes)):
            if type(lista_heroes[heroe]) == dict and "genero" in lista_heroes[heroe]:
                if agregar_codigo_heroe(lista_heroes[heroe],heroe+1):
                    flag_todo_ok = True
                    contador_codigos += 1
        
    if not flag_todo_ok:
        print("El origen de datos no contiene el formato correcto")
    else:
        print(f"Se asignaron {contador_codigos} codigos\nEl codigo del primer heroe es {lista_heroes[0]['codigo_heroe']}\nEl codigo del ultimo heroe es {lista_heroes[-1]['codigo_heroe']}")
        
"""
3.1. Crear la función ‘sanitizar_entero’ la cual recibirá como parámetro:
● numero_str: un string que representa un posible número entero
La función deberá analizar el string recibido y determinar si es un número
entero positivo. La función debe devolver distintos valores según el problema
encontrado:
● Si contiene carácteres no numéricos retornar -1
● Si el número es negativo se deberá retornar un -2
● Si ocurren otros errores que no permiten convertirlo a entero entonces
se deberá retornar -3
También deberá quitar los espacios en blanco de atras y adelante del string
en caso que los tuviese
En caso que se verifique que el texto contenido en el string es un número
entero positivo, retornarlo convertido en entero
"""

def sanitizar_entero(numero_str:str)->int:
    numero_str = numero_str.strip()
    if not numero_str.isdigit() and numero_str[0] != "-":
        return -1
    else:
        try:
            numero = int(numero_str)
            if numero < 0:
                return -2
            else:
                return numero
        except:
            return -3

# print(sanitizar_entero("0"))
"""
3.2. Crear la función ‘sanitizar_flotante’ la cual recibirá como parámetro:
● numero_str: un string que representa un posible número decimal
La función deberá analizar el string recibido y determinar si es un número
flotante positivo. La función debe devolver distintos valores según el
problema encontrado:
● Si contiene carácteres no numéricos retornar -1
● Si el número es negativo se deberá retornar un -2
● Si ocurren otros errores que no permiten convertirlo a entero entonces
se deberá retornar -3
También deberá quitar los espacios en blanco de atras y adelante del string
en caso que los tuviese
En caso que se verifique que el texto contenido en el string es un número
flotante positivo, retornarlo convertido en flotante
"""
def sanitizar_flotante(numero_str:str)-> int:
    numero_str = numero_str.strip()
    
    tiene_punto = False
    
    for caracter in numero_str:
        if caracter == ".":
            tiene_punto = True
            break
    
    if not numero_str.isdigit() and not tiene_punto:
        return -1
    else:   
        try:
            flotante = float(numero_str)
            if flotante < 0:
                return -2
            else:
                return flotante
        except:
            return -3
    
"""
3.3. Crear la función ‘sanitizar_string’’ la cual recibirá como parámetro
● valor_str: un string que representa el texto a validar
● valor_por_defecto: un string que representa un valor por defecto
(parámetro opcional, inicializarlo con ‘-’)
La función deberá analizar el string recibido y determinar si es solo texto (sin
números). En caso de encontrarse números retornar “N/A”
En el caso que valor_str contenga una barra ‘/’ deberá ser reemplazada por un
espacio
El espacio es un caracter válido
En caso que se verifique que el parámetro recibido es solo texto, se deberá
retornar el mismo convertido todo a minúsculas
En el caso que el texto a validar se encuentre vacío y que nos hayan pasado
un valor por defecto, entonces retornar el valor por defecto convertido a
minúsculas
Quitar los espacios en blanco de atras y adelante de ambos parámetros en
caso que los tuviese
"""

def sanitizar_string(valor_str:str, valor_por_defecto:str = "-"):
    
    if len(valor_str) > 0:
        valor_str = valor_str.strip()
        sin_barra = ""
        str_final = ""
        for caracter in valor_str:
            if caracter.isdigit():
                return "N/A"
             
            if caracter == "/":
                caracter = " "
                sin_barra += caracter
            else:
                sin_barra += caracter
                
        for caracter in sin_barra:
            if (caracter >= "A" and caracter <= "Z") or (caracter >= "a" and caracter <= "z") or (caracter == " "):
                str_final += caracter.lower()
        
        return str_final
    else:
        return valor_por_defecto.lower()

""" 
3.4. Crear la función ‘sanitizar_dato’ la cual recibirá como parámetros:
● heroe: un diccionario con los datos del personaje
● clave: un string que representa el dato a sanitizar (la clave del
diccionario). Por ejemplo altura
● tipo_dato: un string que representa el tipo de dato a sanitizar. Puede
tomar los valores: ‘string’, ‘entero’ y ‘flotante’
La función deberá sanitizar el valor del diccionario correspondiente a la clave
y al tipo de dato recibido
Para sanitizar los valores se deberán utilizar las funciones creadas en los
puntos 3.1, 3.2, 3.3 y 3.4
Se deberá validar:
● Que tipo_dato se encuentre entre los valores esperados (‘string, ‘entero,
‘flotante)’ la validación debe soportar que nos lleguen mayúsculas o
minúsculas. En caso de encontrarse un valor no válido informar por
pantalla: ‘Tipo de dato no reconocido’
● Que clave exista como clave dentro del diccionario heroe. En caso de
no encontrarse, informar por pantalla: ‘La clave especificada no
existe en el héroe’. (en este caso la validación es sensible a
mayúsculas o minúsculas)
Ejemplo de llamada a la función válida:
sanitizar_dato(dict_personaje, “altura”, “Flotante”)
La función deberá devolver True en caso de haber sanitizado algún dato y
False en caso contrario.
"""

def sanitizar_dato(heroe:dict, clave:str, tipo_dato:str)->bool:
    tipo_dato = tipo_dato.lower()
    salio_bien = False
    if tipo_dato == "string" or tipo_dato == "entero" or tipo_dato == "flotante":
        if clave.lower() in heroe:
            match tipo_dato:
                case "entero":
                    if sanitizar_entero(heroe[clave]) != -1 and sanitizar_entero(heroe[clave]) != -2 and sanitizar_entero(heroe[clave]) != -3:
                        heroe[clave] = sanitizar_entero(heroe[clave])
                        salio_bien = True 
                case "string":
                    if sanitizar_string(heroe[clave]) != "N/A" and sanitizar_string(heroe[clave]) != "-":
                        heroe[clave] = sanitizar_string(heroe[clave])
                        salio_bien = True 
        
                case "flotante":
                    if sanitizar_flotante(heroe[clave]) != -1 and sanitizar_flotante(heroe[clave]) != -2 and sanitizar_flotante(heroe[clave]) != -3:
                        heroe[clave] = sanitizar_flotante(heroe[clave])
                        salio_bien = True 
        else:
            print("La clave especificada no existe en el héroe")
    else:
        print("Tipo de dato no reconocido")
    
    return salio_bien
        
"""
3.5. Crear la función 'stark_normalizar_datos’ la cual recibirá como parámetros:
● lista_heroes: la listas personajes
La función deberá recorrer la lista de héroes y sanitizar los valores solo de las
siguientes claves: ‘altura’, ‘peso’, ‘color_ojos’, ‘color_pelo’, ‘fuerza’ e
‘inteligencia’
● Un vez finalizado el proceso mostrar el mensaje ‘Datos normalizados’,
● Validar que la lista de héroes no esté vacía para realizar sus acciones,
caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”
● La función no retorna nada
● Reutilizar la función sanitizar_dato
"""

def stark_normalizar_datos(lista_heroes:list):
    if len(lista_heroes) > 0:
        altura_normalizada = False
        peso_normalizado = False
        color_ojos_normalizado = False
        color_pelo_normalizado = False
        inteligencia_normalizado = False
        fuerza_normalizado = False
        
        for heroe in lista_heroes:
            if sanitizar_dato(heroe,"altura","flotante"):
                altura_normalizada = True
                
            if sanitizar_dato(heroe,"peso","flotante"):
                peso_normalizado = True
                
            if sanitizar_dato(heroe,"color_ojos","string"):
                color_ojos_normalizado = True
                
            if sanitizar_dato(heroe,"color_pelo","string"):
                color_pelo_normalizado = True
                
            if sanitizar_dato(heroe,"inteligencia","string"):
                inteligencia_normalizado = True

            if sanitizar_dato(heroe,"fuerza","entero"):
                fuerza_normalizado = True
        
        if altura_normalizada and peso_normalizado and color_ojos_normalizado and color_pelo_normalizado and inteligencia_normalizado and fuerza_normalizado:
            print("Datos normalizados")
    else:
        print("Error: Lista de héroes vacía")

""" 
4.1. Crear la función ‘generar_indice_nombres’ la cual recibirá como parámetro:
● lista_heroes: la lista de personajes
La función deberá iterar la lista de personajes y generar una lista donde cada
elemento es cada palabra que componen el nombre de los personajes.
Por ejemplo la lista que se deberá retornar tiene la siguiente forma:
[‘Howard’, ‘the’, ‘Duck’, ‘Rocket’, ‘Raccoon’, ‘Wolverine’, … ]
La función deberá validar que:
● La lista contenga al menos un elemento
● Todos los elementos de lista_heroes sean del tipo diccionario
● Todos los elementos contengan la clave ‘nombre’
En caso de encontrar algún error, informar por pantalla: ‘El origen de datos no
contiene el formato correcto’
"""
def generar_indice_nombres(lista_heroes:list)->list:
    
    salio_bien = False
    
    if len(lista_heroes) > 0:
        sublista = []
        nombre_personajes_partes = []

        for heroe in lista_heroes:
            if type(heroe) == dict and "nombre" in heroe:
                salio_bien = True
                
        if salio_bien:
            for heroe in lista_heroes:
                heroe["nombre"] = heroe["nombre"].replace("-", " ")
                dividir_nombre = heroe["nombre"].split(" ")
                sublista.append(dividir_nombre)
            
            for nombre in sublista:
                nombre_personajes_partes.extend(nombre)
                
            return nombre_personajes_partes
        else:
            print("El origen de datos no contiene el formato correcto") 
    else:
        print("El origen de datos no contiene el formato correcto")     

""" 
4.2. Crear la función ‘stark_imprimir_indice_nombre’ la cual recibirá como
parámetro:
● lista_heroes: la lista de personajes
La función deberá mostrar por pantalla el índice generado por la función
generar_indice_nombres con todos los nombres separados con un guión.
Por ejemplo:
Howard-the-duck-Rocket-Raccoon-Wolverine…
"""
#CODIGO
def stark_imprimir_indice_nombre(lista_heroes:list):
    lista_nombres = generar_indice_nombres(lista_heroes)
    separador = "-"
    nombres_con_separador = separador.join(lista_nombres)
    print(nombres_con_separador)
        
# stark_imprimir_indice_nombre(heroes)

""" 
5.1. Crear la función ‘convertir_cm_a_mtrs’ la cual recibirá como parámetro:
● valor_cm: Un número que representa una medida en centímetros
La función deberá retornar el número recibido, pero convertido a la unidad
metros. La función deberá validar que el número recibido sea un número
flotante positivo, en caso de no serlo retornar -1
"""
#CODIGO
def convertir_cm_a_mtrs(valor_cm:str):
    try:
        valor_cm = float(valor_cm)
        if valor_cm < 0:
            return -1
        else:
            valor_m = valor_cm / 100
            return valor_m
    except:
        return -1

""" 
5.2. Crear la función ‘generar_separador’ la cual recibirá como parámetro
● patron: un carácter que se utilizará como patrón para generar el
separador
● largo: un número que representa la cantidad de caracteres que va
ocupar el separador.
● imprimir: un parámetro opcional del tipo booleano (por default definir
en True)
La función deberá generar un string que contenga el patrón especificado
repitiendo tantas veces como la cantidad recibida como parámetro (uno junto
al otro, sin salto de línea)
Si el parámetro booleano recibido se encuentra en False se deberá solo
retornar el separador generado. Si se encuentra en True antes de retornarlo,
imprimirlo por pantalla
La función deberá validar:
● Que el parámetro patrón tenga al menos un carácter y como máximo
dos
● Que el parámetro largo sea un entero entre 1 y 235 inclusive
En caso de no verificarse las validaciones devolver ‘N/A’
Ejemplo de llamada:
generar_separador(‘*’, 10)
Ejemplo de salida:
**********
"""
#CODIGO
def generar_separador(patron:str, largo:int, imprimir:bool = True)->str:
    if (len(patron) >= 1 and len(patron) <= 2) and (largo >= 1 and largo <= 235):
        contador = 0
        separador = ""
        while contador < largo:
            separador += patron
            contador += 1
        if imprimir:
            print(separador)
        
        return separador
    else:
        return "N/A"

# generar_separador("*",10)


""" 
5.3. Crear la función ‘generar_encabezado’ la cual recibirá como parámetro
● titulo: un string que representa el título de una sección de la ficha
La función deberá devolver un string que contenga el título envuelto entre dos
separadores (estimar el largo requerido para tu pantalla).
Ejemplo de salida:
********************************************************************************
PRINCIPAL
********************************************************************************
La función deberá convertir el titulo recibido en todas letras mayúsculas
"""

def generar_encabezado(titulo:str):
    generar_separador("*",160,imprimir=True)
    print(titulo.upper())
    generar_separador("*",160,imprimir=True)
    
# generar_encabezado("Menu stark")

"""
5.4. Crear la función ‘imprimir_ficha_heroe’ la cual recibirá como parámetro:
● heroe: un diccionario con los datos del héroe
La función deberá a partir los datos del héroe generar un string con el
siguiente formato e imprimirlo por pantalla::
***************************************************************************************
PRINCIPAL
***************************************************************************************
NOMBRE DEL HÉROE: Spider-Man (S.M.)
IDENTIDAD SECRETA: Peter Parker
CONSULTORA: Marvel Comics
CÓDIGO DE HÉROE : M-00000001
***************************************************************************************
FISICO
***************************************************************************************
ALTURA: 1,78 Mtrs.
PESO: 74,25 Kg.
FUERZA: 55 N
***************************************************************************************
SEÑAS PARTICULARES
***************************************************************************************
COLOR DE OJOS: Hazel
COLOR DE PELO: Brown
"""
def imprimir_ficha_heroe(heroe:dict)->None:
    generar_encabezado("Principal")
    print(f"NOMBRE DEL HÉROE: {heroe['nombre']} ({heroe['iniciales']})\nIDENTIDAD SECRETA: {heroe['identidad']}\nCONSULTORA: {heroe['empresa']}\nCÓDIGO DE HÉROE: {heroe['codigo_heroe']}")
    generar_encabezado("Fisico")
    print(f"ALTURA: {heroe['altura']}\nPESO: {heroe['peso']}\nFUERZA: {heroe['fuerza']}")
    generar_encabezado("Señas particulares")
    print(f"COLOR DE OJOS: {heroe['color_ojos']}\nCOLOR DE PELO: {heroe['color_pelo']}")
    
# stark_normalizar_datos(heroes)
# stark_generar_codigos_heroes(heroes)
# stark_imprimir_nombres_con_iniciales(heroes)
# imprimir_ficha_heroe(heroes[0])

""" 
5.5. Crear la función 'stark_navegar_fichas’ la cual recibirá como parámetros:
● lista_heroes: la listas personajes
La función deberá comenzar imprimiendo la ficha del primer personaje de la
lista y luego solicitar al usuario que ingrese alguna de las siguientes opciones:
[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir
● Si el usuario ingresa ‘1’: se debe mostrar el héroe que se encuentra en
la posición anterior en la lista (en caso de estar en el primero, ir al
último)
● Si el usuario ingresa ‘2’: se debe mostrar el héroe que se encuentra en
la posición siguiente en la lista (en caso de estar en el último, ir al
primero)
● Si ingresa ‘S’: volver al menú principal
● Si ingresa cualquier otro valor, volver a mostrar las opciones hasta que
ingrese un valor válido
"""
def stark_navegar_fichas(lista_heroes:list, ):

    indice = 0
    imprimir_ficha_heroe(lista_heroes[0])
    while True:
        
        while True:
            opcion = input("\n[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir\n").upper()
            if opcion == "1" or opcion == "2" or opcion == "S":
                break
            else:
                imprimir_ficha_heroe(lista_heroes[indice])
        match opcion:
            case "1":
                    indice -= 1
                    if indice < 0:
                        indice = len(lista_heroes) - 1
                    imprimir_ficha_heroe(lista_heroes[indice])
            case "2":
                indice += 1
                if indice >= len(lista_heroes):
                    indice = 0
                imprimir_ficha_heroe(lista_heroes[indice])
            case "S":
                print("Volviendo al menu principal...")
                break
    
        
            
        
    
stark_normalizar_datos(heroes)
stark_generar_codigos_heroes(heroes)
stark_imprimir_nombres_con_iniciales(heroes)
stark_navegar_fichas(heroes)
from data_stark import *
from funciones_calculos_stark import *
import os 

def copiar_datos(lista_actual:list,lista_nueva:list)->None:
    """Copia los datos originales en una lista nueva

    Args:
        lista_actual (list): Lista origen\n
        lista_nueva (list): Lista destino
    """
    if len(lista_actual) > 0:
        for item in lista_actual:
            lista_nueva.append(item)
    else:
        print("ERROR! Lista vacia")


# 0. Crear la función 'stark_normalizar_datos' la cual recibirá por parámetro la lista de héroes. La función deberá:
# ● Recorrer la lista y convertir al tipo de dato correcto las keys (solo con las keys que representan datos numéricos)
# ● Validar primero que el tipo de dato no sea del tipo al cual será casteado. Por ejemplo si una key debería ser entero (ejemplo edad) verificar antes que no se encuentre ya en ese tipo de dato.
# ● Si al menos un dato fue modificado, la función deberá imprimir como mensaje ‘Datos normalizados’, caso contrario no imprimirá nada.
# ● Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”
def stark_normalizar_datos(lista_heroes,campo,tipo_nuevo):
    
    datos_normalizados = False
    
    if len(lista_heroes) > 0:
        try:
            for heroe in lista_heroes:
                if type(heroe[campo]) != tipo_nuevo:
                    heroe[campo] = tipo_nuevo(heroe[campo])
                    datos_normalizados = True
        except ValueError:
            print("Error! Intentaste convertir a un tipo de dato que no se puede")
    else:
        print("Error! Lista de heroes vacia")
    
    if datos_normalizados:
        print("Datos normalizados")

# 1.1. Crear la función 'obtener_nombre' la cual recibirá por parámetro un
# diccionario el cual representara a un héroe y devolverá un string el cual
# contenga su nombre formateado de la siguiente manera:
# Nombre: Howard the Duck

def obtener_nombre(un_heroe:dict)->str:
    
    if not len(un_heroe) == 0:
        nombre_heroe = f"Nombre: {un_heroe['nombre']}"
        return nombre_heroe
    else:
        print("ERROR! El diccionario esta vacio")

# 1.2. Crear la función 'imprimir_dato' la cual recibirá por parámetro un string y
# deberá imprimirlo en la consola. La función no tendrá retorno.

def imprimir_dato(dato:any)->None:
    print(f"{dato:2}")
    

# 1.3. Crear la función 'stark_imprimir_nombres_heroes' la cual recibirá por
# parámetro la lista de héroes y deberá imprimirla en la consola. Reutilizar las
# funciones hechas en los puntos 1.1 y 1.2. Validar que la lista no esté vacía
# correspondientes
# para realizar sus acciones, caso contrario no hará nada y retornara -1.
# Con este se resuelve el Ej 1 del desafío #00

def stark_imprimir_nombres_heroes(lista_heroes:list)->int:
    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            nombre_heroe = obtener_nombre(heroe)
            imprimir_dato(nombre_heroe)
    else:
        return -1

# 2. Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un diccionario el cual representara a un héroe y una key (string) la cual representará el dato que se desea obtener.
# ● La función deberá devolver un string el cual contenga el nombre y dato (key) del héroe a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O
# CUALQUIER OTRO DATO.
# ● El string resultante debe estar formateado de la siguiente manera: (suponiendo que la key es fuerza)
# Nombre: Venom | fuerza: 500

def obtener_nombre_y_dato(un_heroe:dict,key_heroe:str)->str:
    if not len(un_heroe) == 0 and type(key_heroe) == str:
        try:
            nombre_altura = f"Nombre: {un_heroe['nombre']:18s} | {key_heroe}: {un_heroe[key_heroe]}"
            return nombre_altura
        except KeyError:
           print("Error! Esa clave no existe en el diccionario")
    else:
        print("Error! Los parametros son invalidos")

# 3. Crear la función 'stark_imprimir_nombres_alturas' la cual recibirá por
# parámetro la lista de héroes, la cual deberá iterar e imprimir sus nombres y
# alturas USANDO la función creada en el punto 2. Validar que la lista de héroes
# no esté vacía para realizar sus acciones, caso contrario no hará nada y
# retornara -1.
# Con este se resuelve el Ej 2 del desafío #00

def stark_imprimir_nombres_alturas(lista_heroes:list)->int:
    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            print(obtener_nombre_y_dato(heroe,"altura"))
    else:
        return -1

# 4.4. Crear la función 'stark_calcular_imprimir_heroe' la cual recibirá tres
# parámetros:
# ● La lista de héroes
# ● El tipo de cálculo a realizar: es un valor string que puede tomar los
# valores ‘maximo’ o ‘minimo’
# ● Un string que representa la key del dato a calcular, por ejemplo: ‘altura’,
# ‘peso’, ‘edad’, etc.

# Con este se resuelve el Ej 3, Ej 4, Ej 6 y Ej 7 del desafío #00
# La función deberá obtener el héroe que cumpla dichas condiciones, imprimir
# su nombre y el valor calculado. Reutilizar las funciones de los puntos:
# punto 1.2, punto: 2 y punto 4.3
# Validar que la lista de héroes no esté vacía para realizar sus acciones, caso
# contrario no hará nada y retornara -1.
# Ejemplo de llamada:
# stark_calcular_imprimir_heroe (lista, "maximo", "edad")
# Ejemplo de salida:
# Mayor altura: Nombre: Howard the Duck | altura: 79.34

def stark_calcular_imprimir_heroe(lista_heroes:list,calculo_realizar:str,key_heroe:str)->None:
     
    if len(lista_heroes) > 0 and type(key_heroe) == str and type(calculo_realizar) == str:
        heroe_max_o_min = calcular_max_min_dato(lista_heroes,calculo_realizar,key_heroe)
        heroe_imprimir = obtener_nombre_y_dato(heroe_max_o_min,key_heroe)
        imprimir_dato(heroe_imprimir)
    else:
        return -1

# 5.4. Crear la función 'stark_calcular_imprimir_promedio_altura' la cual recibirá
# una lista de héroes y utilizando la función del punto 5.3 calcula y mostrará la
# altura promedio. Validar que la lista de héroes no esté vacía para realizar sus
# acciones, caso contrario no hará nada y retornara -1.
# IMPORTANTE: hacer uso de las las funciones creadas en los puntos 1.2, 5.1 y
# 5.3
# Con este se resuelve el Ej 5 del desafío #00

def stark_calcular_imprimir_promedio_altura(lista_heroes):
    if len(lista_heroes) > 0:
        altura_promedio = calcular_promedio(lista_heroes,"altura")#5.3
        imprimir_dato(altura_promedio)
    else:
        return -1

# 6.1. Crear la función "imprimir_menu" que imprima el menú de opciones por
# pantalla, el cual permite utilizar toda la funcionalidad ya programada. Se
# deberá reutilizar la función antes creada encargada de imprimir un string (1.2)
def imprimir_menu()->None:
    print("####             STARK INDUSTRIES             ####\n")
    print("-----------------------------------------------------\n")
    imprimir_dato(" 1 --> Normalizar datos\n 2 --> Imprimir nombre de todos los heroes\n 3 --> Imprimir nombre y altura de los heroes\n 4 --> El heroe mas alto\n 5 --> El heroe mas bajo\n 6 --> Altura promedio de los heroes\n 7 --> Nombre del heroe mas alto\n 8 --> Nombre del heroe mas bajo\n 9 --> Heroe mas pesado\n 10 --> Heroe menos pesado\n11 --> Sub menu\n12 --> Salir\n\n")


# 6.3. Crear la función 'stark_menu_principal' la cual se encargará de imprimir el
# menú de opciones y le pedirá al usuario que ingrese el número de una de las
# opciones elegidas y deberá validarlo. En caso de ser correcto dicho número,
# lo retornara casteado a entero, caso contrario retorna -1. Reutilizar las
# funciones del ejercicio 6.1 y 6.2

def stark_menu_principal():
    imprimir_menu()
    opcion = input("Ingrese una opcion\n")
    if validar_entero(opcion):
        opcion = int(opcion)
        return opcion
    else:
        return -1
    
# 7. Crear la función 'stark_marvel_app' la cual recibirá por parámetro la lista de
# héroes y se encargará de la ejecución principal de nuestro programa.
# Utilizar if/elif o match según prefiera (match solo para los que cuentan con
# python 3.10+). Debe informar por consola en caso de seleccionar una opción
# incorrecta y volver a pedir el dato al usuario. Reutilizar las funciones con
# prefijo 'stark_' donde crea correspondiente.
def stark_marvel_app(lista_heroes:list):
    flag_normalizar_datos = False
    
    if len(lista_heroes) > 0:
        while True:
            os.system("cls")
            while True:
                opcion = stark_menu_principal()
                if opcion >= 1 and opcion <= 12:
                    break
                else:
                    print("Opcion opcion incorrecta")
                
            match opcion:
                case 1:
                    if not flag_normalizar_datos:
                        stark_normalizar_datos(lista_heroes,"altura",float)
                        stark_normalizar_datos(lista_heroes,"peso",float)
                        stark_normalizar_datos(lista_heroes,"fuerza",float)
                        flag_normalizar_datos = True
                    else:
                        print("Los datos ya fueron normalizados")
                case 2:
                    print("\t LISTA DE NOMBRES DE SUPERHEROES\n")
                    stark_imprimir_nombres_heroes(lista_heroes)
                case 3:
                    print("\t NOMBRES Y ALTURAS DE HEROES\n")
                    stark_imprimir_nombres_alturas(lista_heroes)
                case 4:
                    if flag_normalizar_datos:
                        print("\t EL HEROE MAS ALTO\n")
                        stark_calcular_imprimir_heroe(lista_heroes,"maximo","altura")
                    else:
                        print("Se deben normalizar los datos primero antes de calcular")
                case 5:
                    if flag_normalizar_datos:
                        print("\t EL HEROE MAS BAJO\n")
                        stark_calcular_imprimir_heroe(lista_heroes,"minimo","altura")
                    else:
                        print("Se deben normalizar los datos primero antes de calcular")
                case 6:
                    if flag_normalizar_datos:
                        print("\t ALTURA PROMEDIO DE LOS SUPERHEROES\n")
                        stark_calcular_imprimir_promedio_altura(lista_heroes)
                    else:
                        print("Se deben normalizar los datos primero antes de calcular")
                case 7:
                    if flag_normalizar_datos:    
                        print("\t NOMBRE DEL HEROE MAS ALTO\n")
                        mas_alto = calcular_max(lista_heroes,"altura")
                        nombre_mas_alto = obtener_nombre(mas_alto)
                        imprimir_dato(nombre_mas_alto)
                    else:
                        print("Se deben normalizar los datos primero antes de calcular")
                case 8:
                    if flag_normalizar_datos:
                        print("\t NOMBRE DE HEROE MAS BAJO\n")
                        mas_bajo = calcular_min(lista_heroes,"altura")
                        nombre_mas_bajo = obtener_nombre(mas_bajo)
                        imprimir_dato(nombre_mas_bajo)
                    else:
                        print("Se deben normalizar los datos primero antes de calcular")
                case 9:
                    if flag_normalizar_datos:
                        print("\t HEROE MAS PESADO\n")
                        stark_calcular_imprimir_heroe(lista_heroes,"maximo","peso")
                    else:
                        print("Se deben normalizar los datos primero antes de calcular")
                case 10:
                    if flag_normalizar_datos:
                        print("\t HEROE MENOS PESADO\n")
                        stark_calcular_imprimir_heroe(lista_heroes,"minimo","peso")
                    else:
                        print("Se deben normalizar los datos primero antes de calcular")
                case 11:
                    #sub menu
                    pass
                case 12:
                    break
            os.system("pause")
    else:
        print("Error! Lista vacia")
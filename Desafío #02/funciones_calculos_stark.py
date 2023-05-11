from modulo_validaciones import *
# 4.1. Crear la función 'calcular_max' la cual recibirá por parámetro la lista de
# héroes y una key (string) la cual representará el dato que deberá ser evaluado
# a efectos de determinar cuál es el máximo de la lista. Por ejemplo la función
# deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe
# que tenga el dato más alto.
# Ejemplo de llamada:
# calcular_max(lista, 'edad')


def calcular_max(lista_heroes:list,key_heroe:str)->dict:
    """Calcular el maximo en un campo del diccionario

    Args:
        lista_heroes (list): Lista de diccionario de heroes\n
        key_heroe (str): Key/campo a obtener el maximo

    Returns:
        dict: El diccionario del heroe que contiene el maximo
    """
    flag_max = True
    
    if len(lista_heroes) > 0 and type(key_heroe) == str:
        try:
            for heroe in lista_heroes:
                if flag_max or heroe[key_heroe] >= heroe_dato_max:
                    heroe_dato_max = heroe[key_heroe]
                    heroe_completo = heroe
                    flag_max = False
                    
            return heroe_completo
        except KeyError:
            print("Error! Esa clave no existe en el diccionario")
    else:
        print("Error! Los parametros son invalidos")


# 4.2. Crear la función 'calcular_min' la cual recibirá por parámetro la lista de
# héroes y una key (string) la cual representará el dato que deberá ser evaluado
# a efectos de determinar cuál es el mínimo de la lista. Por ejemplo la función
# deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe
# que tenga el dato más bajo.
# Ejemplo de llamada:
# calcular_min(lista, 'edad')

def calcular_min(lista_heroes:list,key_heroe:str)->dict:
    """Calcular el minimo en un campo del diccionario

    Args:
        lista_heroes (list): Lista de diccionario de heroes\n
        key_heroe (str): Key/campo a obtener el minimo

    Returns:
        dict: El diccionario del heroe que contiene el minimo
    """
    flag_min = True
    
    if len(lista_heroes) > 0 and type(key_heroe) == str:
        try:
            for heroe in lista_heroes:
                if flag_min or heroe[key_heroe] <= heroe_dato_min:
                    heroe_dato_min = heroe[key_heroe]
                    heroe_completo = heroe
                    flag_min = False
                    
            return heroe_completo
        except KeyError:
            print("Error! Esa clave no existe en el diccionario")
    else:
        print("Error! Los parametros son invalidos")

# 4.3. Crear la funcion 'calcular_max_min_dato' la cual recibira tres parámetros:
# ● La lista de héroes
# ● El tipo de cálculo a realizar: es un valor string que puede tomar los
# valores ‘maximo’ o ‘minimo’
# ● Un string que representa la key del dato a calcular, por ejemplo: ‘altura’,
# ‘peso’, ‘edad’, etc.
# La función deberá retornar el héroe que cumpla con la condición pedida.
# Reutilizar las funciones hechas en los puntos 4.1 y 4.2
# Ejemplo de llamada:
# calcular_max_min_dato(lista, "maximo", "edad")

def calcular_max_min_dato(lista_heroes:list,calculo_realizar:str,key_heroe:str)->dict:
    """Calcular el maximo o minimo de un campo en un diccionario

    Args:
        lista_heroes (list): Lista de diccionarios de heroes\n
        calculo_realizar (str): Toma valores 'maximo' o 'minimo'\n
        key_heroe (str): Key del heroe a obtener el minimo o maximo

    Returns:
        dict: El diccionario del heroe que contiene el maximo o el minimo
    """
    if len(lista_heroes) > 0 and type(key_heroe) == str and type(calculo_realizar) == str:
       if calculo_realizar == "minimo" or calculo_realizar == "maximo":
            match calculo_realizar:
                case "minimo":
                    heroe = calcular_min(lista_heroes,key_heroe)
                    return heroe
                case "maximo":
                    heroe = calcular_max(lista_heroes,key_heroe)
                    return heroe
       else:
           print("Error! No se indico correctamente el calculo a realizar")
    else:
        print("Error! Los parametros son invalidos")

# 5.1. Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una
# lista de héroes y un string que representara el dato/key de los héroes que se
# requiere sumar. Validar que cada héroe sea tipo diccionario y que no sea un
# diccionario vacío antes de hacer la suma. La función deberá retorna la suma
# de todos los datos según la key pasada por parámetro

def sumar_dato_heroe(lista_heroes:list,key_heroe:str)->int:
    """Adquiere el total de un campo de diccionario

    Args:
        lista_heroes (list): Lista de diccionarios de heroes\n
        key_heroe (str): Campo a obtener el total

    Returns:
        int: El total
    """
    sumador = 0
    
    if len(lista_heroes) > 0 and type(key_heroe) == str:
        for heroe in lista_heroes:
            if type(heroe) == dict and heroe != {}:
                sumador += heroe[key_heroe]
                
        return sumador        
    else:
        print("Error! Los parametros son invalidos")

# 5.2. Crear la función ‘dividir’ la cual recibirá como parámetro dos números
# (dividendo y divisor). Se debe verificar si el divisor es 0, en caso de serlo,
# retornar 0, caso contrario realizar la división entre los parámetros y retornar el
# resultado

def dividir(dividendo:int|float,divisor:int|float)->float:
    """Valida que el divisor no sea 0 y realiza la division

    Args:
        dividendo (int | float): Entero o flotante dividendo\n
        divisor (int | float): Entero o flotante divisor

    Returns:
        float: Resultado de la division
    """
    
    if (type(dividendo) == int or type(dividendo) == float) and (type(divisor) == int or type(divisor) == float):
        if not divisor == 0:
            resultado = dividendo / divisor
            return resultado
        else:
            return 0
    else:
        print("Error! Los parametros son invalidos")

# 5.3. Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una
# lista de héroes y un string que representa el dato del héroe que se requiere
# calcular el promedio. La función debe retornar el promedio del dato pasado
# por parámetro
# IMPORTANTE: hacer uso de las las funciones creadas en los puntos 5.1 y 5.2

def calcular_promedio(lista_heroes:list,key_heroe_calcular:str)->float:
    """Calcula el promedio

    Args:
        lista_heroes (list): Lista de diccionarios de heroes
        key_heroe_calcular (str): Campo a calcular el promedio

    Returns:
        float: El promedio formateado a 2 decimales
    """
    if len(lista_heroes) > 0 and type(key_heroe_calcular) == str:
        total = sumar_dato_heroe(lista_heroes,key_heroe_calcular)
        divisor = len(lista_heroes)
        resultado = dividir(total,divisor)
        return f"{resultado:.2f}"      
    else:
        print("Error! Los parametros son invalidos")

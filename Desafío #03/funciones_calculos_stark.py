from modulo_validaciones import *
# 4.1. Crear la función 'calcular_max' la cual recibirá por parámetro la lista de
# héroes y una key (string) la cual representará el dato que deberá ser evaluado
# a efectos de determinar cuál es el máximo de la lista. Por ejemplo la función
# deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe
# que tenga el dato más alto.
# Ejemplo de llamada:
# calcular_max(lista, 'edad')


def calcular_max(lista_heroes:list,key_heroe:str)->dict:
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
    if len(lista_heroes) > 0 and type(key_heroe_calcular) == str:
        total = sumar_dato_heroe(lista_heroes,key_heroe_calcular)
        resultado = dividir(total,len(lista_heroes))
        return resultado      
    else:
        print("Error! Los parametros son invalidos")

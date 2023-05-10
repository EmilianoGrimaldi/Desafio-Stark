def acumulador(lista:list, clave:str)->int:
    """Calcula el valor total de un campo en especifico 

    Args:
        lista (list): La lista de datos\n
        clave (str): La clave que quiero calcular

    Returns:
        int: El total
    """
    acumulador = 0
    for item in lista:
        acumulador += item[clave]
    return acumulador

def sacar_promedio(total:int, cantidad:int)->float:
    """Calcular el promedio

    Args:
        total (int): El dividendo\n
        cantidad (int): El divisor

    Returns:
        float: El resultado
    """
    promedio = total / cantidad
    return promedio

def buscar_maximo(lista:list, campo:str)->int:
    """Calcular el maximo de una lista en un campo

    Args:
        lista (list): La lista de datos\n
        campo (str): La clave que quiero calcular el max

    Returns:
        int: El maximo
    """
    flag_max = True
    for item in lista:
        if flag_max or item[campo] >= maximo:
            maximo = item[campo]
            flag_max = False

    return maximo

def buscar_minimo(lista:list, campo:str)->int:
    """Calcular el minimo de una lista en un campo

    Args:
        lista (list): La lista de datos\n
        campo (str): La clave que quiero calcular el min

    Returns:
        int: El minimo
    """
    flag_min = True
    for item in lista:
        if flag_min or item[campo] <= minimo:
            minimo = item[campo]
            flag_min = False

    return minimo

def calcular_max_min(lista:list, campo:str, maximo=True)->int:
    """Calcula el maximo o el minimo de una lista en un campo 

    Args:
        lista (list): La lista de datos\n
        campo (str): La clave a calcular el max o min\n
        maximo (bool, optional): True para calcular Maximo, False para minimo. Predeterminado en True.

    Returns:
        int: El valor minimo o maximo
    """
    if maximo:
        max = buscar_maximo(lista,campo)
        return max
    else:
        min = buscar_minimo(lista,campo)
        return min
    

def calcular_los_maxs_mins(lista:list, campo:str, calculo_realizar:bool)->list:
    """Calcula si hay mas de un minimo o maximo y se guarda en una lista

    Args:
        lista (list): La lista de datos\n
        campo (str): La clave a calcular el min o max\n
        calculo_realizar (bool): True para calcular Maximo, False para minimo. Predeterminado en True.

    Returns:
        list: La lista con los maximos o minimos
    """
    lista_maxs_mins = []
    aux_maxs_mins = calcular_max_min(lista, campo, calculo_realizar)
    for item in lista:
        if item[campo] == aux_maxs_mins:
            lista_maxs_mins.append(item)

    return lista_maxs_mins
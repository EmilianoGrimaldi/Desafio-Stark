import os
from modulo_calculos_stark import *
from modulo_funciones_imprimir import *

def cambiar_tipo_campo_dic(lista:list, clave_a_cambiar:str, tipo_nuevo_clave:type)->None:
    """Modifica un tipo de dato a otro, en un campo del diccionario

    Args:
        lista (list): Lista de diccionarios\n
        clave_a_cambiar (str): La clave a modificar\n
        tipo_nuevo_clave (type): El nuevo tipo
    """
    for item in lista:
        if type(item[clave_a_cambiar]) != tipo_nuevo_clave:
            item[clave_a_cambiar] = tipo_nuevo_clave(item[clave_a_cambiar])
            
def inicializar_clave_vacia(lista:list,clave:str,cadena_inicializar:str)-> None:
    """
        Inicializar un valor de una clave del diccionario que este vacio
    Args:
        lista (list): Lista de diccionarios\n
        clave (str): La clave del diccionario a modificar\n
        cadena_inicializar (str): El nuevo valor de la clave
    """
    for heroe in lista:
        if heroe[clave] == "":
            heroe[clave] = cadena_inicializar

def filtrar_heroes(lista:list, clave:str, valor:str)-> list:
    """Filtra la lista de heroes por clave y valor

    Args:
        lista (list): Lista de diccionarios\n
        clave (str): Clave del diccionario\n 
        valor (str): Valor del diccionario

    Returns:
        list: La lista filtrada
    """
    lista_filtrada = []
    for item in lista:
        if item[clave] == valor:
            lista_filtrada.append(item)
    return lista_filtrada

def listar_nombre_genero(lista:list, genero:str)->None:
    """Lista los nombres de los heroes por genero

    Args:
        lista (list): Lista de diccionarios\n
        genero (str): Genero que quiero mostrar
    """
    heroes = filtrar_heroes(lista,"genero",genero)
    if genero == "M":
        print("\t NOMBRE DE CADA HEROE\n")
    else:
        print("\t NOMBRE DE CADA HEROINA\n")
        
    imprimir_lista_por_campo(heroes,"nombre")

def calcular_listar_mas_alto_genero(lista:list, genero:str)->None:
    """Calcula y lista la maxima altura de los heroes por genero

    Args:
        lista (list): Lista de diccionarios\n
        genero (str): Genero a obtener la altura maxima
    """
    heroes = filtrar_heroes(lista,"genero",genero)
    mas_altos = calcular_los_maxs_mins(heroes,"altura",True)
    
    if len(mas_altos) == 1:
        if genero == "M":
            print("\n\t HEROE MAS ALTO")
        else:
            print("\n\t HEROINA MAS ALTA")
    else:
        if len(mas_altos) > 1:
            if genero == "M":
                print("\n\t HEROES MAS ALTOS")
            else:
                print("\n\t HEROINAS MAS ALTAS")
                
    encabezado_campos_heroes()    
    imprimir_heroes(mas_altos)

def calcular_listar_mas_bajo_genero(lista:list, genero:str)->None:
    """Calcula y lista la minima altura de los heroes por genero

    Args:
        lista (list): Lista de diccionarios\n
        genero (str): Genero a obtener la altura minima
    """
    heroes = filtrar_heroes(lista,"genero",genero)
    mas_bajos = calcular_los_maxs_mins(heroes, "altura",False)
    if len(mas_bajos) == 1:
        if genero == "M":
            print("\n\t HEROE MAS BAJO")
        else:
            print("\n\t HEROINA MAS BAJA")
    else:
        if len(mas_bajos) > 1:
            if genero == "M":
                print("\n\t HEROES MAS BAJOS")
            else:
                print("\n\t HEROINAS MAS BAJAS")
                
    encabezado_campos_heroes()
    imprimir_heroes(mas_bajos)
                    

def promediar_altura_genero(lista:list,genero:str)->None:
    """Calcula el promedio de altura de los heroes por genero

    Args:
        lista (list): Lista de diccionarios\n
        genero (str): El genero a obtener el promedio altura
    """
    heroes = filtrar_heroes(lista,"genero",genero)
    acumulador_edad = acumulador(heroes,"altura")
    promedio = sacar_promedio(acumulador_edad, len(heroes))
    
    if genero == "M":
        print("\t ALTURA PROMEDIO HEROES\n")
        print("La altura promedio de los heroes es {:.2f}".format(promedio))
    else:
        print("\t ALTURA PROMEDIO HEROINAS\n")
        print("La altura promedio de las heroinas es {:.2f}".format(promedio))


def calcular_nombrar_mayor_altura_genero(lista:list,genero:str)->None:
    """Calcula el maximo de altura de los heroes y muestra el nombre del heroe o los heroes

    Args:
        lista (list): Lista de diccionarios\n
        genero (str): Genero a obtener el nombre de altura maxima
    """
    heroes = filtrar_heroes(lista,"genero",genero)
    lista_alturas = calcular_los_maxs_mins(heroes, "altura",True)

    if len(lista_alturas) == 1:
        if genero == "M":
            print("\t NOMBRE DE HEROE MAS ALTO\n")
        else:
            print("\t NOMBRE DE HEROINA MAS ALTA\n")    
    else:
        if len(lista_alturas) > 1:
            if genero == "M":
                print("\n\t NOMBRES DE HEROES MAS ALTOS")
            else:
                print("\n\t NOMBRES DE HEROINAS MAS ALTAS")
                
    imprimir_lista_por_campo(lista_alturas,"nombre")
                    

def calcular_nombrar_menor_altura_genero(lista:list,genero:str)->None:
    """Calcula el minimo de altura de los heroes y muestra el nombre del heroe o los heroes

    Args:
        lista (list): Lista de diccionarios\n
        genero (str): Genero a obtener el nombre de altura minima
    """

    heroes = filtrar_heroes(lista,"genero",genero)
    lista_alturas = calcular_los_maxs_mins(heroes, "altura",False)

    if len(lista_alturas) == 1:
        if genero == "M":
            print("\t NOMBRE DE HEROE MAS BAJO\n")
        else:
            print("\t NOMBRE DE HEROINA MAS BAJA\n")         
    else:
        if len(lista_alturas) > 1:
            if genero == "M":
                print("\n\t NOMBRES DE HEROES MAS BAJOS")
            else:
                print("\n\t NOMBRES DE HEROINAS MAS BAJAS")
                
    imprimir_lista_por_campo(lista_alturas,"nombre")
                
                    

def contar_cantidad_campo(lista:list,clave:str)->dict:
    """Cuenta la cantidad de valores iguales que hay dentro de ese campo en una lista de diccionarios

    Args:
        lista (list): Lista de diccionarios\n
        clave (str): Clave del diccionario a obtener la cantidad de valores iguales dentro del campo

    Returns:
        dict: Diccionario con los valores dentro del campo y sus cantidades
    """
    dic_aux = {}
    
    for heroe in lista:
        valor_atributo = heroe[clave].capitalize() 
        if valor_atributo in dic_aux:
            dic_aux[valor_atributo] += 1
        else:
            dic_aux[valor_atributo] = 1
    
    return dic_aux
    
def listar_cantidad_por_criterio(lista:list, clave:str):
    """Muestra la cantidad de valores iguales dentro de un campo en la lista de diccionarios

    Args:
        lista (list): Lista de diccionarios\n
        clave (str): Clave del campo a obtener cantidad de los valores
    """
    tipo_cantidad = contar_cantidad_campo(lista, clave)
    for key,valor in tipo_cantidad.items():
        print("|    {:26s}|\t {:2d}\t|".format(key,valor))

def filtrar_heroe_categoria(lista:list, clave:str)-> dict:
    """Filtra los heroes segun el valor de su campo/clave

    Args:
        lista (list): Lista de diccionarios\n
        clave (str): Clave del campo a obtener los heroes con el mismo valor

    Returns:
        dict: Diccionario filtrado con los heroes que tienen el mismo valor dentro del campo
    """
    dic = {}
    
    for heroe in lista:
        criterio = heroe[clave].capitalize()
        if criterio in dic:
            dic[criterio].append(heroe)
        else:
            dic[criterio] = [heroe]
            
    return dic

def mostrar_heroe_categoria(diccionario:dict)-> None:
    """Imprime los heroes filtrados por los valores iguales dentro de un campo

    Args:
        diccionario (dict): Diccionario filtrado
    """
    for clave, valores in diccionario.items():
        print(f"\n\t {clave}")
        encabezado_campos_heroes()
        imprimir_heroes(valores)
           
def filtrar_mostrar_heroe_categoria(lista:list,clave:str):
    """Muestra los heroes filtrados por categoria

    Args:
        lista (list): Lista de diccionarios\n
        clave (str): Clave a filtrar
    """
    heroe_filtrado = filtrar_heroe_categoria(lista,clave)
    mostrar_heroe_categoria(heroe_filtrado)
    

def menu_desafio_01(lista:list, opcion:str)->None:
    """Menu de opciones con sus acciones a realizar

    Args:
        lista (list): Lista de diccionarios con los heroes\n
        opcion (str): Numero de opcion a realizar
    """
    cambiar_tipo_campo_dic(lista,"altura",float)
    cambiar_tipo_campo_dic(lista,"peso",float)
    inicializar_clave_vacia(lista,"color_pelo","No tiene")
    inicializar_clave_vacia(lista,"inteligencia","No tiene")
    
    match opcion:   
        case "1":
            listar_nombre_genero(lista,"M")
        case "2":
            listar_nombre_genero(lista,"F")
        case "3":
            calcular_listar_mas_alto_genero(lista,"M")
        case "4":
            calcular_listar_mas_alto_genero(lista,"F")
        case "5":
            calcular_listar_mas_bajo_genero(lista,"M")
        case "6":
            calcular_listar_mas_bajo_genero(lista,"F")
        case "7":
            promediar_altura_genero(lista,"M")
        case "8":
            promediar_altura_genero(lista,"F")
        case "9":
            calcular_nombrar_mayor_altura_genero(lista,"M")
        case "10":
            calcular_nombrar_mayor_altura_genero(lista,"F")
        case "11":
            calcular_nombrar_menor_altura_genero(lista,"M")
        case "12":
            calcular_nombrar_menor_altura_genero(lista,"F")
        case "13":
            print("      CANTIDAD DE TIPOS DE COLOR DE OJOS\n")
            listar_cantidad_por_criterio(lista,"color_ojos")   
        case "14":
            print("      CANTIDAD DE TIPOS DE COLOR DE PELO\n")
            listar_cantidad_por_criterio(lista,"color_pelo") 
        case "15":
            print("      CANTIDAD DE TIPOS DE INTELIGENCIA\n") 
            listar_cantidad_por_criterio(lista,"inteligencia") 
        case "16":
            print("\t LISTA HEROES POR COLOR DE OJOS")
            filtrar_mostrar_heroe_categoria(lista,"color_ojos")
        case "17":
            print("\t LISTA HEROES POR COLOR DE PELO")
            filtrar_mostrar_heroe_categoria(lista,"color_pelo")
        case "18":
            print("\t LISTA HEROES POR INTELIGENCIA")
            filtrar_mostrar_heroe_categoria(lista,"inteligencia")
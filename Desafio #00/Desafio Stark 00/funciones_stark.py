from modulo_calculos_stark import *
from modulo_funciones_imprimir import *

def cambiar_tipo_campo_dic(lista:list, clave_a_cambiar:str, tipo_nuevo_clave:type)->None:
    """Modifica un tipo de dato a otro, en un campo del diccionario

    Args:
        lista (list): La lista de datos\n
        clave_a_cambiar (str): La clave a modificar\n
        tipo_nuevo_clave (type): El nuevo tipo
    """
    for item in lista:
        if type(item[clave_a_cambiar]) != tipo_nuevo_clave:
            item[clave_a_cambiar] = tipo_nuevo_clave(item[clave_a_cambiar])


def imprimir_lista_nombres_heroes(lista:list)->None:
    """Imprimir los nombres de los heroes

    Args:
        lista (list): La lista de datos a imprimir
    """
    print("\t LISTA DE NOMBRES DE SUPERHEROES\n")
    imprimir_lista_por_campo(lista,"nombre")
    
def imprimir_nombre_altura_heroes(lista:list)->None:
    """Imprime la lista de nombres con alturas de heroes

    Args:
        lista (list): La lista de datos a imprimir
    """
    print("\t    NOMBRES Y ALTURAS DE HEROES\n")
    print("|\t    HEROE\t   |\t   ALTURA\t|\n")
    for heroe in lista:
        print(f"|{heroe['nombre']:^26}|{heroe['altura']:^20}|")

def mostrar_promedio(promedio:float)->None:
    """Muestra el promedio

    Args:
        promedio (float): El promedio calculado a mostrar
    """
    print("{:.2f}".format(promedio))


def calcular_mostrar_heroe_mas_alto(lista:list)->None:
    """Calcula y muestra el heroe mas alto o los heroes mas altos si hay igualdad

    Args:
        lista (list): La lista de datos
    """
    
    lista_mas_altos = calcular_los_maxs_mins(lista, "altura",True)
    if len(lista_mas_altos) == 1:
        print("\n\tEL HEROE MAS ALTO")
    else:
        if len(lista_mas_altos) > 1:
            print("\n\tLOS HEROES MAS ALTOS")

    encabezado_campos_heroes()
    imprimir_heroes(lista_mas_altos)
    
def calcular_mostrar_heroe_mas_bajo(lista:list)->None:
    """Calcula y muestra el heroe mas bajo o los heroes mas bajos si hay igualdad

    Args:
        lista (list): La lista de datos
    """
    lista_mas_bajos = calcular_los_maxs_mins(lista, "altura", False)
    if len(lista_mas_bajos) == 1:
        print("\n\tEL HEROE MAS BAJO")
    else:
        if len(lista_mas_bajos) > 1:
            print("\n\tLOS HEROES MAS BAJOS")

    encabezado_campos_heroes()
    imprimir_heroes(lista_mas_bajos)

def calcular_mostrar_promedio_alturas_heroes(lista:list)->None:
    """
        Calcula y muestra el promedio de altura de los heroes
    Args:
        lista (list): La lista de datos
    """
    print("\n\tALTURA PROMEDIO DE LOS SUPERHEROES\n")
    altura_total = acumulador(lista,"altura")
    promedio_altura = sacar_promedio(altura_total, len(lista))
    print("La altura promedio de los heroes es {:.2f}".format(promedio_altura))

def calcular_mostrar_nombre_heroe_mas_alto(lista:list)->None:
    """Calcula y muestra el nombre del heroe mas alto o los nombres de los heroes mas altos si hay igualdad

    Args:
        lista (list): La lista de datos
    """
    
    lista_aux = calcular_los_maxs_mins(lista, "altura",True)
    
    if len(lista_aux) == 1:
        print("\n\tNOMBRE DEL HEROE MAS ALTO\n")
    else:
        if len(lista_aux) > 1:
            print("\n\tNOMBRES DE LOS HEROES MAS ALTOS\n")
    imprimir_lista_por_campo(lista_aux,"nombre")

def calcular_mostrar_nombre_heroe_mas_bajo(lista:list)->None:
    """Calcula y muestra el nombre del heroe mas bajo o los nombres de los heroes mas bajos si hay igualdad

    Args:
        lista (list): La lista de datos
    """
    lista_mas_bajos = calcular_los_maxs_mins(lista, "altura",False)
    
    if len(lista_mas_bajos) == 1:
        print("\n\tNOMBRE DE HEROE MAS BAJO\n")
    else:
        if len(lista_mas_bajos) > 1:
            print("\n\tNOMBRES DE LOS HEROES MAS BAJOS\n")

    imprimir_lista_por_campo(lista_mas_bajos,"nombre")

def calcular_mostrar_maximo_peso_heroe(lista:list)->None:
    """Calcula y muestra el heroe mas pesado o los heroes mas pesados si hay igualdad

    Args:
        lista (list): La lista de datos
    """
    lista_mas_pesados = calcular_los_maxs_mins(lista, "peso",True)
    if len(lista_mas_pesados) == 1:
        print("\n\tHEROE MAS PESADO")
    else:
        if len(lista_mas_pesados) > 1:
            print("\n\tHEROES MAS PESADOS")

    encabezado_campos_heroes()
    imprimir_heroes(lista_mas_pesados)
                   
def calcular_mostrar_minimo_peso_heroe(lista:list)->None:
    """Calcula y muestra el heroe menos pesado o los heroes menos pesados si hay igualdad

    Args:
        lista (list): La lista de datos
    """
    lista_menos_pesados = calcular_los_maxs_mins(lista, "peso",False)

    if len(lista_menos_pesados) == 1:
        print("\n\tHEROE MENOS PESADO")
    else:
        if len(lista_menos_pesados) > 1:
            print("\n\tHEROES MENOS PESADOS")

    encabezado_campos_heroes()
    imprimir_heroes(lista_menos_pesados)



def menu_heroes(lista:list,opcion:str)->None:
    """Muestra el menu de opciones con sus acciones a realizar

    Args:
        lista (list): La lista de datos con la trabajara cada opcion
        opcion (str): La opcion a realizar
    """
    # CONVIERTO TODAS LAS ALTURAS/PESO QUE ESTAN EN STRING LAS PASO A FLOAT
    cambiar_tipo_campo_dic(lista,"altura",float)
    cambiar_tipo_campo_dic(lista,"peso",float)
  
    match opcion:
        case "1":
            imprimir_lista_nombres_heroes(lista)    
        case "2":
            imprimir_nombre_altura_heroes(lista)
        case "3":
            calcular_mostrar_heroe_mas_alto(lista)
        case "4":
            calcular_mostrar_heroe_mas_bajo(lista)
        case "5":
            calcular_mostrar_promedio_alturas_heroes(lista)
        case "6":
            calcular_mostrar_nombre_heroe_mas_alto(lista)
        case "7":
            calcular_mostrar_nombre_heroe_mas_bajo(lista)
        case "8":
            calcular_mostrar_maximo_peso_heroe(lista)
        case "9":
            calcular_mostrar_minimo_peso_heroe(lista)
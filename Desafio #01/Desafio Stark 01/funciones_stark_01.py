import os
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

def filtrar_heroes(lista:list, clave:str, valor:str)-> list:
    lista_filtrada = []
    for item in lista:
        if item[clave] == valor:
            lista_filtrada.append(item)
    return lista_filtrada

def listar_nombre_genero(lista:list, genero:str)->None:
    heroes = filtrar_heroes(lista,"genero",genero)
    if genero == "M":
        print("\t\t\t\t\t     ########                NOMBRE DE CADA HEROE               ########\n")
        for heroe in heroes:
            print("\t\t\t\t\t\t\t\t|{:^30}|".format(heroe['nombre']))
    else:
        print("\t\t\t\t\t     ########                NOMBRE DE CADA HEROINA              ########\n")
        for heroe in heroes:
            print("\t\t\t\t\t\t\t\t|{:^30}|".format(heroe['nombre']))

def listar_mas_alto_genero(lista:list, genero:str)->None:
    heroes = filtrar_heroes(lista,"genero",genero)
    mas_altos = calcular_los_maxs_mins(heroes,"altura",True)
    
    if len(mas_altos) == 1:
        match genero: 
            case "M":
                print("\t\t\t\t\t\t\t########                HEROE MAS ALTO               ########\n")
                encabezado_campos_heroes()
                imprimir_un_heroe(mas_altos[0])
            case "F":
                print("\t\t\t\t\t\t\t########                HEROINA MAS ALTA               ########\n")
                encabezado_campos_heroes()
                imprimir_un_heroe(mas_altos[0])
    else:
        if len(mas_altos) > 1:
            match genero:
                case "M":
                    print("\t\t\t\t\t\t\t########                HEROES MAS ALTOS               ########\n")
                    encabezado_campos_heroes()
                    imprimir_heroes(mas_altos)
                case "F":
                    print("\t\t\t\t\t\t\t########                HEROINAS MAS ALTAS               ########\n")
                    encabezado_campos_heroes()
                    imprimir_heroes(mas_altos)

def listar_mas_bajo_genero(lista:list, genero:str)->None:
    heroes = filtrar_heroes(lista,"genero",genero)
    mas_bajos = calcular_los_maxs_mins(heroes, "altura",False)
    if len(mas_bajos) == 1:
        match genero: 
            case "M":
                print("\t\t\t\t\t\t\t########                HEROE MAS BAJO               ########\n")
                encabezado_campos_heroes()
                imprimir_un_heroe(mas_bajos[0])
            case "F":
                print("\t\t\t\t\t\t\t########                HEROINA MAS BAJA               ########\n")
                encabezado_campos_heroes()
                imprimir_un_heroe(mas_bajos[0])
    else:
        if len(mas_bajos) > 1:
            match genero: 
                case "M":
                    print("\t\t\t\t\t\t\t########                HEROES MAS BAJOS               ########\n")
                    encabezado_campos_heroes()
                    imprimir_heroes(mas_bajos)
                case "F":
                    print("\t\t\t\t\t\t\t########                HEROINAS MAS BAJAS               ########\n")
                    encabezado_campos_heroes()
                    imprimir_heroes(mas_bajos)

def promediar_altura_genero(lista:list,genero:str)->None:
    heroes = filtrar_heroes(lista,"genero",genero)
    acumulador_edad = acumulador(heroes,"altura")
    promedio = sacar_promedio(acumulador_edad, len(heroes))
    match genero: 
        case "M":
            print("\t\t\t\t\t\t\t########                ALTURA PROMEDIO HEROES               ########\n")
            print("La altura promedio de los heroes es {:.2f}".format(promedio))
        case "F":
            print("\t\t\t\t\t\t\t########                ALTURA PROMEDIO HEROINAS               ########\n")
            print("La altura promedio de las heroinas es {:.2f}".format(promedio))


def nombrar_mayor_altura_genero(lista:list,genero:str)->None:
    heroes = filtrar_heroes(lista,"genero",genero)
    lista_alturas = calcular_los_maxs_mins(heroes, "altura",True)

    if len(lista_alturas) == 1:
        match genero: 
            case "M":
                print("\t\t\t\t\t\t\t########                NOMBRE DE HEROE MAS ALTO               ########\n")
                print("El heroe mas alto es {}".format(lista_alturas[0]["nombre"]))
            case "F":
                print("\t\t\t\t\t\t\t########                NOMBRE DE HEROINA MAS ALTA               ########\n")    
                print("La heroina mas alta es {}".format(lista_alturas[0]["nombre"]))
    else:
        if len(lista_alturas) > 1:
            match genero:
                case "M":
                    print("\t\t\t\t\t\t\t########                NOMBRES DE HEROES MAS ALTOS               ########\n")
                    print("Los heroes mas altos son")
                    imprimir_lista_por_campo(lista_alturas,"nombre")
                case "F":
                    print("\t\t\t\t\t\t\t########                NOMBRES DE HEROINAS MAS ALTAS               ########\n")
                    print("Las heroinas mas altas son")
                    imprimir_lista_por_campo(lista_alturas,"nombre")

def nombrar_menor_altura_genero(lista:list,genero:str)->None:

    heroes = filtrar_heroes(lista,"genero",genero)
    lista_alturas = calcular_los_maxs_mins(heroes, "altura",False)

    if len(lista_alturas) == 1:
        match genero:
            case "M":
                print("\t\t\t\t\t\t\t########                NOMBRE DE HEROE MAS BAJO               ########\n")
                print("El heroe mas bajo es {}".format(lista_alturas[0]["nombre"]))
            case "F":
                print("\t\t\t\t\t\t\t########                NOMBRE DE HEROINA MAS BAJA               ########\n")    
                print("La heroina mas baja es {}".format(lista_alturas[0]["nombre"]))
    else:
        if len(lista_alturas) > 1:
            match genero:
                case "M":
                    print("\t\t\t\t\t\t\t########                NOMBRES DE HEROES MAS BAJOS               ########\n")
                    print("Los heroes mas bajos son")
                    imprimir_lista_por_campo(lista_alturas,"nombre")
                case "F":
                    print("\t\t\t\t\t\t\t########                NOMBRES DE HEROINAS MAS BAJAS               ########\n")
                    print("Las heroinas mas bajas son")
                    imprimir_lista_por_campo(lista_alturas,"nombre")

def contar_items_categoria(lista:list,clave:str)->dict:
    #Creo un dic vacio para ir guardando los items como clave y la cantidad como valor
    dic_aux = {}
    
    for item in lista:
        #Hago una busqueda y voy guardando el item en una var
        item_guardado = item[clave].capitalize() # Primer letra en mayuscula el resto minuscula
        #Pregunto si ese item existe dentro del diccionario
        if item_guardado in dic_aux:
            #si existe le sumo 1 al valor de ese item
            dic_aux[item_guardado] += 1
        else:
            #sino existe creo la clave de ese item y le asigno el valor 1 (para indicar que es el primer item)
            dic_aux[item_guardado] = 1
    
    return dic_aux

def listar_cantidad_color_ojos(lista:list)-> None:
    print("\t\t\t\t\t     ########                CANTIDAD DE TIPOS DE COLOR DE OJOS             ########\n")
    
    color_ojos = contar_items_categoria(lista,"color_ojos")  
    
    print("\t\t\t\t\t\t\t    |           COLOR OJOS           |   CANTIDAD   |\n")
    #items tranforma ese diccionario en una lista de tuplas clave : valor
    for color,cantidad in color_ojos.items():  
        print("\t\t\t\t\t\t\t    |\t {:28s}|\t    {:2d}\t    |".format(color,cantidad))
        
def listar_cantidad_color_pelo(lista:list)->None:
    print("\t\t\t\t\t ########                CANTIDAD DE TIPOS DE COLOR DE PELO             ########\n")
    color_pelo = contar_items_categoria(lista,"color_pelo")
    
    print("\t\t\t\t\t\t\t    |         COLOR PELO        |  CANTIDAD  |\n")
    for color,cantidad in color_pelo.items():  
        print("\t\t\t\t\t\t\t    |   {:24s}|{:^12}|".format(color,cantidad))
 
def listar_cantidad_tipo_inteligencia(lista:list)->None: 
    print("\t\t\t\t\t ########                CANTIDAD DE TIPOS DE INTELIGENCIA             ########\n")
    
    tipo_inteligencia = contar_items_categoria(lista,"inteligencia")
    
    print("\t\t\t\t\t\t\t    |          INTELIGENCIA        |  CANTIDAD  |\n")
    for inteligencia,cantidad in tipo_inteligencia.items():
        print("\t\t\t\t\t\t\t    |    {:26s}|\t {:2d}\t|".format(inteligencia,cantidad))

def inicializar_clave_vacia(lista:list,clave:str,cadena_inicializar:str)-> None:
    for heroe in lista:
        if heroe[clave] == "":
            heroe[clave] = cadena_inicializar

def filtrar_heroe_categoria(lista:list, clave:str)-> dict:
    dic = {}
    
    for item in lista:
        value = item[clave].capitalize()
        if value in dic:
            dic[value].append(item)
        else:
            dic[value] = [item]
            
    return dic

def mostrar_heroe_categoria(diccionario:dict)-> None:
    for item, valores in diccionario.items():
        print(f"\n\t\t\t\t\t\t\t\t\t\t{item}")
        encabezado_campos_heroes()
        imprimir_heroes(valores)

def listar_heroes_por_color_ojos(lista:list)-> None:
    print("\t\t\t\t\t\t########                LISTA HEROES POR COLOR DE OJOS             ########")
    heroes_por_color_ojos = filtrar_heroe_categoria(lista,"color_ojos")
    mostrar_heroe_categoria(heroes_por_color_ojos)

def listar_heroes_por_color_pelo(lista:list)-> None:
    print("\t\t\t\t\t\t########                LISTA HEROES POR COLOR DE PELO             ########")
    heroes_por_color_pelo = filtrar_heroe_categoria(lista,"color_pelo")
    mostrar_heroe_categoria(heroes_por_color_pelo)
    
def listar_heroes_por_inteligencia(lista:list)-> None:
    print("\t\t\t\t\t\t########                LISTA HEROES POR INTELIGENCIA             ########")
    heroes_por_inteligencia = filtrar_heroe_categoria(lista,"inteligencia")
    mostrar_heroe_categoria(heroes_por_inteligencia)

def ingresar_menu_desafio_01(lista:list, opcion:str)->None:
    cambiar_tipo_campo_dic(lista,"altura",float)
    cambiar_tipo_campo_dic(lista,"peso",float)
    # Inicializo los valores de las claves vacias con "No tiene"
    inicializar_clave_vacia(lista,"color_pelo","No tiene")
    inicializar_clave_vacia(lista,"inteligencia","No tiene")
    match opcion:   
        case "1":
            listar_nombre_genero(lista,"M")
        case "2":
            listar_nombre_genero(lista,"F")
        case "3":
            listar_mas_alto_genero(lista,"M")
        case "4":
            listar_mas_alto_genero(lista,"F")
        case "5":
            listar_mas_bajo_genero(lista,"M")
        case "6":
            listar_mas_bajo_genero(lista,"F")
        case "7":
            promediar_altura_genero(lista,"M")
        case "8":
            promediar_altura_genero(lista,"F")
        case "9":
            nombrar_mayor_altura_genero(lista,"M")
        case "10":
            nombrar_mayor_altura_genero(lista,"F")
        case "11":
            nombrar_menor_altura_genero(lista,"M")
        case "12":
            nombrar_menor_altura_genero(lista,"F")
        case "13":
            listar_cantidad_color_ojos(lista)   
        case "14":
            listar_cantidad_color_pelo(lista)
        case "15":
            listar_cantidad_tipo_inteligencia(lista)
        case "16":
            listar_heroes_por_color_ojos(lista)
        case "17":
            listar_heroes_por_color_pelo(lista)
        case "18":
            listar_heroes_por_inteligencia(lista)
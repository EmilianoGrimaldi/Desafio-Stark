def encabezado_campos_heroes()-> None:
    """Muestra el encabezado con los campos de cada heroe
    """
    print("\n NOMBRE                  IDENTIDAD                        EMPRESA          ALTURA   PESO    GENERO    COLOR OJOS                COLOR PELO      FUERZA    INTELIGENCIA")

def imprimir_un_heroe(heroe:dict)->None:
    """Imprime los valores de cada clave de un heroe

    Args:
        heroe (dict): El diccionario del heroe
    """
    print(f" {heroe['nombre']:23s} {heroe['identidad']:32s} {heroe['empresa']:15s} {heroe['altura']:7}  {heroe['peso']:6}      {heroe['genero']:7s} {heroe['color_ojos']:26s} {heroe['color_pelo']:15s} {heroe['fuerza']:9s} {heroe['inteligencia']}")

def imprimir_heroes(lista:list)->None:
    """Imprime la lista de heroes con sus valores de cada clave

    Args:
        lista (list): La lista de heroes a imprimir
    """
    for heroe in lista:
        imprimir_un_heroe(heroe)
        
def imprimir_lista_por_campo(lista:list, campo:str)->None:
    """Imprimir la lista de heroes en un campo especifico

    Args:
        lista (list): La lista de datos a imprimir\n
        campo (str): Campo a imprimir
    """
    for heroe in lista:
        print(heroe[campo])

def menu(titulo:str,opciones:str)->str:
    """Muestra un menu con titulo y opciones personalizables

    Args:
        titulo (str): El titulo del menu\n
        opciones (str): Las opciones del menu

    Returns:
        str: La opcion
    """
    print("####             {}             ####\n".format(titulo))
    print("-----------------------------------------------------\n")
    print(opciones)
    opcion = input("Ingrese una opcion\n")
    return opcion
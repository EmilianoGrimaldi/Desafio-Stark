from re import *
#6.2. Crear la función “validar_entero” la cual recibirá por parámetro un string de
# número el cual deberá verificar que sea sea un string conformado únicamente
# por dígitos. Retornara True en caso de serlo, False caso contrario
def validar_entero(string_num:str)->bool:
    """Valida que el string ingresado tenga solo numeros

    Args:
        string_num (str): El string a validar

    Returns:
        bool: True si tiene unicamente digitos y False en caso contrario
    """
    patron = compile("^[0-9]+$")
    
    if match(patron,string_num):
        return True
    else:
        return False
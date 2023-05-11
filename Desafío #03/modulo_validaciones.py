from re import *
#6.2. Crear la función “validar_entero” la cual recibirá por parámetro un string de
# número el cual deberá verificar que sea sea un string conformado únicamente
# por dígitos. Retornara True en caso de serlo, False caso contrario
def validar_entero(string_num:str):
    patron = compile("^[0-9]+$")
    
    if match(patron,string_num):
        return True
    else:
        return False
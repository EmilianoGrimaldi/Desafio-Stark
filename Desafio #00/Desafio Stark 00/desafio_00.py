from data_stark import *
from funciones_stark import *

while True:
    os.system("cls")
    
    opcion = menu("STARK INDUSTRIES"," 1 --> Imprimir nombre de todos los heroes\n 2 --> Imprimir nombre y altura de los heroes\n 3 --> El heroe mas alto\n 4 --> El heroe mas bajo\n 5 --> Altura promedio de los heroes\n 6 --> Nombre del heroe mas alto\n 7 --> Nombre del heroe mas bajo\n 8 --> Heroe mas pesado\n 9 --> Heroe menos pesado\n10 --> Salir\n\n")
   
    menu_heroes(lista_personajes,opcion)
    
    if opcion == "10":
        while True:
            confirmacion = input("Seguro que quiere salir? [s/n]\n").lower()
            if confirmacion == "s" or confirmacion == "n":
                break
        if confirmacion == "s":
            break
    os.system("pause")
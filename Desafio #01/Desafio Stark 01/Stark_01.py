from funciones_stark_01 import *
from data_stark import *

while True:
    os.system("cls")
    
    opcion = menu("STARK INDUSTRIES 01"," 1 --> Imprimir nombre de todos los superheroes M\n 2 --> Imprimir nombre de todos los superheroes F\n 3 --> El superhéroe más alto de género M\n 4 --> El superhéroe más alto de género F\n 5 --> El superhéroe más bajo de género M\n 6 --> El superhéroe más bajo de género F\n 7 --> Altura promedio de los superhéroes de género M\n 8 --> Altura promedio de los superhéroes de género F\n 9 --> Nombre del superhéroe más alto de género M\n10 --> Nombre del superhéroe más alto de género F\n11 --> Nombre del superhéroe más bajo de género M\n12 --> Nombre del superhéroe más bajo de género F\n13 --> Cuántos superhéroes tienen cada tipo de color de ojos\n14 --> Cuántos superhéroes tienen cada tipo de color de pelo\n15 --> Cuántos superhéroes tienen cada tipo de inteligencia\n16 --> Listar todos los superhéroes agrupados por color de ojos\n17 --> Listar todos los superhéroes agrupados por color de pelo\n18 --> Listar todos los superhéroes agrupados por tipo de inteligencia\n19 --> Salir\n\n")
   
    ingresar_menu_desafio_01(lista_personajes,opcion)
    
    if opcion == "19":
        while True:
            confirmacion = input("Seguro que quiere salir? [s/n]\n").lower()
            if confirmacion == "s" or confirmacion == "n":
                break
        if confirmacion == "s":
            break
    os.system("pause")

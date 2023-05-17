from stark_04 import *

heroes = leer_archivo("Desafio #04\data_stark.json")
stark_normalizar_datos(heroes,"altura",float)
stark_normalizar_datos(heroes,"peso",float)
stark_normalizar_datos(heroes,"fuerza",int)
stark_marvel_app_5(heroes)
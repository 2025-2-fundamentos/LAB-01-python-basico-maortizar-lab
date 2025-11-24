"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    resultado = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        for linea in f:
            columnas = linea.strip().split("\t")

            letra = columnas[0]          # columna 1
            diccionario = columnas[4]    # columna 5

            suma_fila = 0
            pares = diccionario.split(",")   # separar jjj:12,bbb:3,...

            for par in pares:
                clave, valor = par.split(":")
                suma_fila += int(valor)

            if letra not in resultado:
                resultado[letra] = 0

            resultado[letra] += suma_fila

    return dict(sorted(resultado.items()))

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas donde cada tupla contiene:
    - La letra de la columna 1
    - La cantidad de elementos en la columna 4
    - La cantidad de elementos en la columna 5
    """

    resultado = []

    with open("files\input\data.csv", "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split("\t")

            letra = partes[0]

            # Columna 4: valores separados por comas
            col4 = partes[3]
            items_col4 = col4.split(",")
            cant_col4 = len(items_col4)

            # Columna 5: pares clave:valor separados por comas
            col5 = partes[4]
            items_col5 = col5.split(",")
            cant_col5 = len(items_col5)

            resultado.append((letra, cant_col4, cant_col5))

    return resultado

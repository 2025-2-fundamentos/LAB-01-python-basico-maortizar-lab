"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.
    """

    conteo = {}

    with open("files\input\data.csv", "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split("\t")
            col5 = partes[4]   # columna 5

            # separa los pares clave:valor → ["aaa:1", "bbb:2", ...]
            pares = col5.split(",")

            for p in pares:
                clave, _ = p.split(":")   # solo nos interesa la clave

                if clave not in conteo:
                    conteo[clave] = 1
                else:
                    conteo[clave] += 1

    return conteo

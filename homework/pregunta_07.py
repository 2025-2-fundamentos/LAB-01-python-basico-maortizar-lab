"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 2 y 1.
    Cada tupla contiene un valor posible de la columna 2 y una lista con todas
    las letras asociadas a dicho valor.
    """

    asociaciones = {}

    with open("files\input\data.csv", "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split("\t")

            letra = partes[0]          # columna 1
            valor = int(partes[1])     # columna 2

            if valor not in asociaciones:
                asociaciones[valor] = [letra]
            else:
                asociaciones[valor].append(letra)

    resultado = sorted(asociaciones.items())

    return resultado

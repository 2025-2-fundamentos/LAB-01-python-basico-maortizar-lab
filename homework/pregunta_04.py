"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes.
    """

    conteo_meses = {}

    with open("files\input\data.csv", "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split("\t")
            fecha = partes[2]           # 'YYYY-MM-DD'
            mes = fecha[5:7]            # extrae 'MM'

            if mes not in conteo_meses:
                conteo_meses[mes] = 1
            else:
                conteo_meses[mes] += 1

    resultado = sorted(conteo_meses.items())

    return resultado



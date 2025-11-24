"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    Obtiene por cada clave de la columna 5 (diccionario codificado)
    el valor mínimo y máximo asociados en todo el archivo.
    """

    valores = {}

    with open("files\input\data.csv", "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split("\t")
            col5 = partes[4]  # columna 5

            # dividir la columna por comas → ["aaa:1", "bbb:7", ...]
            pares = col5.split(",")

            for p in pares:
                clave, valor = p.split(":")
                valor = int(valor)

                if clave not in valores:
                    valores[clave] = {"min": valor, "max": valor}
                else:
                    if valor < valores[clave]["min"]:
                        valores[clave]["min"] = valor
                    if valor > valores[clave]["max"]:
                        valores[clave]["max"] = valor

    # Crear lista ordenada alfabéticamente
    resultado = []

    for clave in sorted(valores.keys()):
        resultado.append((clave, valores[clave]["min"], valores[clave]["max"]))

    return resultado


"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.
    """

    valores = {}

    with open("files\input\data.csv", "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split("\t")
            letra = partes[0]
            numero = int(partes[1])

            # Si la letra no está en el diccionario, inicializa max y min
            if letra not in valores:
                valores[letra] = {
                    "max": numero,
                    "min": numero
                }
            else:
                # Actualiza máximo
                if numero > valores[letra]["max"]:
                    valores[letra]["max"] = numero

                # Actualiza mínimo
                if numero < valores[letra]["min"]:
                    valores[letra]["min"] = numero

    resultado = []

    for letra in sorted(valores.keys()):
        resultado.append((letra, valores[letra]["max"], valores[letra]["min"]))

    return resultado

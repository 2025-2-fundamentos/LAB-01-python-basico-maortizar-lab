"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contenga la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.
    """

    suma_por_letra = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split("\t")

            valor = int(partes[1])     # columna 2
            col4 = partes[3]           # columna 4 (lista de letras)

            letras = col4.split(",")   # separa las letras

            for letra in letras:
                if letra not in suma_por_letra:
                    suma_por_letra[letra] = valor
                else:
                    suma_por_letra[letra] += valor

    # Ordenar alfabéticamente las claves
    resultado = {k: suma_por_letra[k] for k in sorted(suma_por_letra.keys())}

    return resultado

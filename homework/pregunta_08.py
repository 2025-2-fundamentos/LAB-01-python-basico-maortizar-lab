"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genera una lista de tuplas donde:
    - Primer elemento: valor de la segunda columna (número)
    - Segundo elemento: lista ordenada y sin repetir de las letras
      de la primera columna asociadas a ese número
    """

    asociaciones = {}

    with open("files\input\data.csv", "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split("\t")

            letra = partes[0]          # columna 1
            valor = int(partes[1])     # columna 2

            # Inicializa si no existe
            if valor not in asociaciones:
                asociaciones[valor] = set()   # usamos set para evitar repeticiones

            asociaciones[valor].add(letra)

    # Construcción del resultado ordenando claves y listas
    resultado = []

    for valor in sorted(asociaciones.keys()):
        lista_ordenada = sorted(list(asociaciones[valor]))
        resultado.append((valor, lista_ordenada))

    return resultado

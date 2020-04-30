"""Lectura del archivo .csv, pero discriminando los países mal escritos. Ej: Spain y Spain:Valencia lo consideramos como 2 países distintos.
Tuppla: (accession, length, geoLocation)"""

import csv
import statistics

sequences = []
geoLocations = []
analysisList = []

def mediana(geoLocation):
    idems = []
    for tupla in sequences:
        if tupla[2] == geoLocation:
            analysisList.append(tupla)
            idems.append(int(tupla[1]))
    median = int(statistics.median(idems))
    if idems.count(median):
        indexMedian = idems.index(median)
        result = analysisList[indexMedian]
    else: #Para cuando la mediana no cioncide con ningun elemento de la lista
        result = analysisList[min(range(len(idems)), key = lambda i: abs(idems[i] - median))]
    analysisList.clear()
    return result




with open('sequences.csv', newline='') as File:
    reader = csv.reader(File)
    row1 = next(reader)  # Eliminamos la linea de el encabezado
    for row in reader:
        accession = row[0]
        length = row[5]
        geoLocation = row[12]
        if accession != '' and length != '' and geoLocation != '':  # Para evitar que no introdizcamos algun dato vacio
            sequences.append((accession, length, geoLocation))
            if geoLocations.count(geoLocation) == 0:
                geoLocations.append(geoLocation)

    for geoLocation in geoLocations:
        median = mediana(geoLocation)
        print(median)
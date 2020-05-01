"""Lectura del archivo .csv, pero discriminando los países mal escritos. Ej: Spain y Spain:Valencia lo consideramos como 2 países distintos.
Tuppla: (accession, length, geoLocation)"""

import csv
import statistics

sequences = []
geoLocations = []
analysisList = []


def mergeSort(data):
    if len(data) <= 2:
        if len(data) == 2:
            if data[0] > data[1]:  # swap(data[0], data[1])
                temp = data[0]
                data[0] = data[1]
                data[1] = temp
        return data

    result = []
    m = len(data) // 2
    dataL = mergeSort(data[:m])
    dataR = mergeSort(data[m:])

    i = j = 0

    while i < len(dataL) and j < len(dataR):
        if dataL[i] < dataR[j]:
            result.append(dataL[i])
            i += 1
        else:
            result.append(dataR[j])
            j += 1

    result += dataL[i:]
    result += dataR[j:]
    return result


def median(list):
    list = mergeSort(list)
    n = len(list)
    if n % 2 == 1:
        return list[n // 2]
    else:
        i = n // 2
        return (list[i - 1] + list[i]) / 2


def mediana(geoLocation):
    idems = []
    for tupla in sequences:
        if tupla[2] == geoLocation:
            analysisList.append(tupla)
            idems.append(int(tupla[1]))
    med = median(idems) #Mediana realizada con funciones propias
    #med = statistics.median(idems) Calcular la mediana mediante la librería statistics.
    if idems.count(median):
        indexMedian = idems.index(med)
        result = analysisList[indexMedian]#[0] descomentar para ver solo las accession
    else:  # Para cuando la mediana no cioncide con ningun elemento de la lista
        result = analysisList[min(range(len(idems)), key=lambda i: abs(idems[i] - med))]#[0] descomentar para ver solo las accession
    analysisList.clear()
    return result


if __name__ == '__main__':
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
            res = mediana(geoLocation)
            print(res)

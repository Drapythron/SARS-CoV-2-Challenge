"""Lectura del archivo .csv, pero discriminando los países mal escritos. Ej: Spain y Spain:Valencia lo consideramos como 2 países distintos.
Tuppla: (accession, length, geoLocation)"""

import csv


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
    lengths = []
    for tupla in sequences:
        if tupla[2] == geoLocation:
            analysisList.append(tupla)
            lengths.append(int(tupla[1]))
    med = median(lengths)  # Mediana realizada con funciones propias
    # med = statistics.median(idems) Calcular la mediana mediante la librería statistics.
    if lengths.count(median):
        indexMedian = lengths.index(med)
        result = analysisList[indexMedian]
    else:  # Para cuando la mediana no cioncide con ningun elemento de la lista
        result = analysisList[min(range(len(lengths)), key=lambda i: abs(lengths[i] - med))]
    analysisList.clear()
    return result


def saveGeoLocation(reader):
    locations = []
    row1 = next(reader)
    for loc in row1:
        locations.append([loc])
    for row in reader:
        pos = 0
        for loc in row:
            if loc != '':
                locations[pos].append(loc)
            pos += 1
    return locations


def newLocation(oldLocation, locations):
    for country in locations:
        if country.count(oldLocation):
            return country[0]
    return oldLocation



if __name__ == '__main__':
    with open('sequences.csv', newline='') as File:
        with open('geoLocations.csv', newline='') as FileLoc:
            reader = csv.reader(FileLoc, delimiter=';')
            locs = saveGeoLocation(reader)
            reader = csv.reader(File)
            row1 = next(reader)  # Eliminamos la linea de el encabezado
            for row in reader:
                accession = row[0]
                length = row[5]
                geoLocation = newLocation(row[12], locs)
                if accession != '' and length != '' and geoLocation != '':  # Para evitar que no introdizcamos algun dato vacio
                    sequences.append((accession, length, geoLocation))
                    if geoLocations.count(geoLocation) == 0:
                        geoLocations.append(geoLocation)
            for geoLocation in geoLocations:
                res = mediana(geoLocation)
                print(res)
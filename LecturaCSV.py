"""Lectura del archivo .csv, pero discriminando los países mal escritos. Ej: Spain y Spain:Valencia lo consideramos como 2 países distintos.
Tuppla: (accession, length, geoLocation)"""

import csv

sequences = []
geoLocations = []
analysisList = []

def mergeSort(data):
    if len(data) <= 2:  # Cuando tenemos un pack individual o una pareja
        if len(data) == 2:
            if data[0] > data[1]:  # Si es pareja y no estan en orden, hacemos un swap
                data[0], data[1] = data[1], data[0]
        return data

    result = []
    m = len(data) // 2  # Función recursiva del mètodo Divide&Conquere
    dataL = mergeSort(data[:m])
    dataR = mergeSort(data[m:])

    i = j = 0

    while i < len(dataL) and j < len(dataR):    # Vamos añadiendo a result los datos de forma ordenada
        if dataL[i] < dataR[j]:
            result.append(dataL[i])
            i += 1
        else:
            result.append(dataR[j])
            j += 1
    # Añadimos los valores que quedasen a un lado si el otro ya ha llegado a su fin
    result += dataL[i:]
    result += dataR[j:]
    return result


def median(list):   # Función màtematica de la mediana
    list = mergeSort(list)
    n = len(list)
    if n % 2 == 1:
        return list[n // 2]
    else:
        i = n // 2
        return (list[i - 1] + list[i]) / 2


def mediana(geoLocation):
    idems = []      # Desará los length
    for tupla in sequences:
        if tupla[2] == geoLocation:     # Comprovamos que estos al país que toca
            analysisList.append(tupla)
            idems.append(int(tupla[1])) # idems tendrá los datos de solo los length
    med = median(idems)  # Mediana realizada con funciones propias

    # Ahora devolveremos el valor length correspondiente a la posición de la mediana
    if idems.count(median):     # NO CAPITXI EL MEDIAN ESTE
        indexMedian = idems.index(med)
        result = analysisList[indexMedian]
    else:  # Para cuando la mediana no coincida con ningun elemento de la lista
        result = analysisList[min(range(len(idems)), key=lambda i: abs(idems[i] - med))]

    analysisList.clear()
    return result


def saveGeoLocation(reader):
    locations = []
    row1 = next(reader)  # Eliminamos la linea de el encabezado
    for loc in row1:
        locations.append([loc])  # Vamos saparando los diferentes paises
    for row in reader:
        pos = 0
        for loc in row:
            if loc != '':
                locations[pos].append(loc)  # Dentro de cada pais, añadimos todas sus diferentes ubicaciones
            pos += 1
    return locations


def newLocation(oldLocation, locations):
    for country in locations:
        if country.count(oldLocation):
            return country[0]  # Devuelve el país, sin la región si existies
    return oldLocation


if __name__ == '__main__':
    with open('sequences.csv', newline='') as File:
        with open('geoLocations.csv', newline='') as LocationsFile:
            # Abrimos fichero con los datos de las regiones y paises
            reader = csv.reader(LocationsFile, delimiter=';')
            locations = saveGeoLocation(reader)
            reader = csv.reader(File)
            row1 = next(reader)  # Eliminamos la linea del encabezado
            for row in reader:
                accession = row[0]
                length = row[5]
                geoLocation = newLocation(row[12], locations)
                # Cogemos la ubicación del sequences (ej: USA: CA) y la traduciremos en solo el país (USA)

                if accession != '' and length != '' and geoLocation != '':  # Para evitar que no introdizcamos algun dato vacio
                    sequences.append((accession, length, geoLocation))  # Añadimos la tupla con los datos
                    if geoLocations.count(geoLocation) == 0:  # POSAR COMENTARI
                        geoLocations.append(geoLocation)

            for geoLocation in geoLocations:  # Calculamos las medianas en cada país
                res = mediana(geoLocation)
                print(res)

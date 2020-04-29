"""Lectura del archivo .csv, pero discriminando los países mal escritos. Ej: Spain y Spain:Valencia lo consideramos como 2 países distintos. """

import csv

sequences = []
geoLocations = []
analysisList = []

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
    print(geoLocations)
import csv

class LecturaCSV:
    __sequences = []
    __geoLocations = []
    __analysisList = []
    __medians = []

    def __init__(self, fileSequences):
        self.__fileSequences = fileSequences
        self.__openAndSaveFile()

    def median(self):
        for geoLocation in self.__geoLocations:  # Calculamos las medianas en cada país
            res = self.__mediana(geoLocation)
            self.__medians.append(res)
        return self.__medians

    def __openAndSaveFile(self):
        with open(self.__fileSequences, newline='') as File:
            reader = csv.reader(File)
            row1 = next(reader)  # Eliminamos la linea del encabezado
            for row in reader:
                accession = row[0]
                length = row[5]
                geoLocation = self.__newLocation(row[12])
                # Cogemos la ubicación del sequences (ej: USA: CA) y la traduciremos en solo el país (USA)

                if accession != '' and length != '' and geoLocation != '':  # Para evitar que no introduzcamos algún dato vacío
                    self.__sequences.append([accession, length, geoLocation])  # Añadimos los datos
                    if self.__geoLocations.count(geoLocation) == 0:  # Añadimos los nuevos países
                        self.__geoLocations.append(geoLocation)

    def __mediana(self, geoLocation):
        lengths = []  # Guardará las longitudes
        for tupla in self.__sequences:
            if tupla[2] == geoLocation:  # Comprovamos que estos al país que toca
                self.__analysisList.append(tupla)
                lengths.append(int(tupla[1]))  # idems tendrá los datos de solo los length
        med = self.__median(lengths)  # Mediana realizada con funciones propias

        # Ahora devolveremos el valor length correspondiente a la posición de la mediana
        if lengths.count(med):
            indexMedian = lengths.index(med)
            result = self.__analysisList[indexMedian]
        else:  # Para cuando la mediana no coincida con ningun elemento de la lista
            result = self.__analysisList[min(range(len(lengths)), key=lambda i: abs(lengths[i] - med))]

        self.__analysisList.clear()
        return result

    def __mergeSort(self, data):
        if len(data) <= 2:  # Cuando tenemos un pack individual o una pareja, caso simple
            if len(data) == 2:
                if data[0] > data[1]:  # Si es pareja y no estan en orden, hacemos un swap
                    data[0], data[1] = data[1], data[0]
            return data

        result = []
        m = len(data) // 2  # Función recursiva del mètodo Divide&Conquere
        dataL = self.__mergeSort(data[:m])
        dataR = self.__mergeSort(data[m:])

        i = j = 0

        while i < len(dataL) and j < len(dataR):  # Vamos añadiendo a result los datos de forma ordenada
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

    def __median(self, list):  # Función matemática de la mediana
        list = self.__mergeSort(list)
        n = len(list)
        if n % 2 == 1:
            return list[n // 2]
        else:
            i = n // 2
            return (list[i - 1] + list[i]) / 2

    def __saveGeoLocation(self, reader):
        locations = []
        row1 = next(reader)
        for loc in row1:
            locations.append([loc])  # Vamos separando los diferentes países
        for row in reader:
            pos = 0
            for loc in row:
                if loc != '':
                    locations[pos].append(loc)  # Dentro de cada país, añadimos todas sus diferentes ubicaciones
                pos += 1
        return locations

    def __newLocation(self, location):
        tokens = location.split(':')
        return tokens[0]


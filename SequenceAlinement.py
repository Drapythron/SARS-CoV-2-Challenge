
sequences = []

if __name__ == '__main__':

    # PROCESO DE LECTURA DEL FICHERO
    seqFASTA = open('sequencesFASTA.fasta')
    reader = seqFASTA.readline()
    pos = -1
    while reader != '':     # Hasta que no haya ni una letra
        if reader[0] == '>':    # Si nos encontramos con '>' es el inicio de los datos de un virus
            pos += 1
            reader = reader.replace('>', '').replace('\n', '').replace(' ', '')
            line = reader.split("|")    # Separamos el accession del geoLocation
            sequences.append(line)
            sequences[pos].append('')
        else:   # Estamos a las lineas del RNA
            reader = reader.replace('\n', '')
            sequences[pos][2] += reader

        reader = seqFASTA.readline()

    for i in range(len(sequences)):
        print(sequences[i])
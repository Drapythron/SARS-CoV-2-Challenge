
sequences = []

if __name__ == '__main__':

    #PROCESO DE LECTURA DEL FICHERO
    seqFASTA = open('sequencesFASTA.fasta')
    reader = seqFASTA.readline()
    pos = -1
    while reader != '':
        if reader[0] == '>':
            pos += 1
            reader = reader.replace('>', '').replace('\n', '').replace(' ', '')
            line = reader.split("|")
            sequences.append(line)
            sequences[pos].append('')
        else:
            reader = reader.replace('\n', '')
            sequences[pos][2] += reader

        reader = seqFASTA.readline()
    #print(sequences)

    #ANÁLIS DE LAS SECUENCIAS

    for i in range(len(sequences[0][2])):
        print(sequences[0][2][i])



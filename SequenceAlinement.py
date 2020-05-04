data = []
sequences = []

def unionOfLines(list):
    if len(list) <= 1:
        return list[0]
    first = list[0]
    list.remove(list[0])
    return first + unionOfLines(list)


if __name__ == '__main__':
    seq = open('sequences.fasta')
    line = seq.readline()
    pos = 0
    while line:
        if '>' in line:  # Inicio sequencia de un país
            data.append(line.split('|'))
            line = seq.readline()
            RNAcode = []
            # Vamos añadiendo las lineas de la sequencia genetica
            while line and ('>' not in line):
                RNAcode.append(line)
                line = seq.readline()
            # Ahora borramos todos los '\n' y espacios de los strings
            data[pos][0] = data[pos][0].rstrip(" >")  # NO SÉ PQ CARAI NO BORRA EL >
            data[pos][1] = data[pos][1].rstrip("\n ")
            for i in range(len(RNAcode)):
                RNAcode[i] = RNAcode[i].rstrip("\n ")
            # Ahora unimos todas las sequencias del nucleoide y lo añadimos a data
            allTogether = unionOfLines(RNAcode)
            data[pos].append(allTogether)
            pos += 1
    # Creamos la tupla con los tres datos
    for i in range(len(data)):
            accession = data[i][0]
            country = data[i][1]
            length = len(data[i][2])
            nucleotideSequence = data[i][2]
            sequences.append((accession, country, length, nucleotideSequence))
    '''
    #era per comprovar si anava sortint tot bé
    print('Sequences length: ' + str(len(sequences)))
    print('Sequences[0] length: ' + str(len(sequences[0])))
    for i in range(len(sequences)):
        print(sequences[i])
    '''

    #crear funció que compari entre països
    #printar per pantalla els resultats de les comparacions

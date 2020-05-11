import LecturaCSV
import UrlSequence
import NeedlemanWunsch


if __name__ == '__main__':

    seq = LecturaCSV.LecturaCSV('sequences.csv', 'geoLocations.csv')
    countrySequences = seq.median() #Este metodo devuelve una lista con todas las tuplas de los país

    #LLAMAMOS A LA CLASE 'UrlSequence' PARA OBTENER LAS SECUENCIAS DE ARN DE LOS PAÍSES DESDE LA WEB
    for i in range(len(countrySequences)):
        seq = UrlSequence.UrlSequence(countrySequences[i][0]).getSequence()
        countrySequences[i].append(seq)
        print(str(countrySequences[i][2]) + ' cargado.')

    #GURDAMOS LOS SCORES EN UNA TABLA

    countryScores = []
    needlemanWunsch = NeedlemanWunsch.NeedlemanWunsch()
    print('Alineando paises...')
    for i in range(len(countrySequences)-1):
        countryScores.append([])
        for j in range(i + 1, len(countrySequences)):
            seq1 = countrySequences[i][3]#[:1000]
            seq2 = countrySequences[j][3]#[:1000]
            needlemanWunsch.newEntry(seq1, seq2)
            score = needlemanWunsch.getScore()
            countryScores[i].append((countrySequences[i][2], countrySequences[j][2], score))
            print((countrySequences[i][2], countrySequences[j][2], score))
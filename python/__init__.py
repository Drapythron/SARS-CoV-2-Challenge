import LecturaCSV
import UrlSequence
import NeedlemanWunsch
import NeedlemanWunschRust

if __name__ == '__main__':

    seq = LecturaCSV.LecturaCSV('data/sequences.csv', 'data/geoLocations.csv')
    countrySequences = seq.median() #Este metodo devuelve una lista con todas las tuplas de los país

    #LLAMAMOS A LA CLASE 'UrlSequence' PARA OBTENER LAS SECUENCIAS DE ARN DE LOS PAÍSES DESDE LA WEB
    for i in range(len(countrySequences)):
        seq = UrlSequence.UrlSequence(countrySequences[i][0]).getSequence()
        countrySequences[i].append(seq)
        print(str(countrySequences[i][2]) + ' cargado.')

    #GURDAMOS LOS SCORES EN UNA TABLA

    countryScores = []
    needWunschRust = NeedlemanWunschRust.NeedlemanWunschRust()

    print('Alineando paises...')
    for i in range(len(countrySequences)-1):
        countryScores.append([])
        for j in range(i + 1, len(countrySequences)):
            seq1 = countrySequences[i][3]
            seq2 = countrySequences[j][3]
            
            score = needWunschRust.getScore(seq1, seq2)

            countryScores[i].append((countrySequences[i][2], countrySequences[j][2], score))
            print((countrySequences[i][2], countrySequences[j][2], "{0:.2f}".format(score)))

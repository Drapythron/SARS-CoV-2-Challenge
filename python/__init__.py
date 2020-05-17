import LecturaCSV
import UrlSequence
import NeedlemanWunsch
import NeedlemanWunschRust
import Clustering

if __name__ == '__main__':

    countries = []

    seq = LecturaCSV.LecturaCSV('data/sequences.csv', 'data/geoLocations.csv')
    countrySequences = seq.median() #Este metodo devuelve una lista con todas las tuplas de los país

    #LLAMAMOS A LA CLASE 'UrlSequence' PARA OBTENER LAS SECUENCIAS DE ARN DE LOS PAÍSES DESDE LA WEB
    for i in range(len(countrySequences)):
        seq = UrlSequence.UrlSequence(countrySequences[i][0]).getSequence()
        countrySequences[i].append(seq)
        countries.append(countrySequences[i][2])
        print(str(countrySequences[i][2]) + ' cargado.')
    
    size = len(countrySequences)

    #GURDAMOS LOS SCORES EN UNA MATRIZ
    
    scores = [[0 for x in range(size)] for w in range(size)]
    needWunschRust = NeedlemanWunschRust.NeedlemanWunschRust()

    print('Alineando paises...')

    for i in range(len(countrySequences)-1):
        for j in range(i + 1, len(countrySequences)):
            seq1 = countrySequences[i][3][:400]
            seq2 = countrySequences[j][3][:400]
            
            score = needWunschRust.getScore(seq1, seq2)
            scores[i][j] = float("{0:.2f}".format(score))
            scores[j][i] = float("{0:.2f}".format(score))
    

    clust = Clustering.Clustering(scores, countries)
    print(clust.getClustering(6))
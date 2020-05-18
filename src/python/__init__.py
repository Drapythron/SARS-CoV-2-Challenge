import LecturaCSV
import UrlSequence
import NeedlemanWunsch
import NeedlemanWunschRust
import Clustering
from tqdm import tqdm 

if __name__ == '__main__':

    countries = []

    seq = LecturaCSV.LecturaCSV('data/sequences.csv')
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
    loop = tqdm(total = ((len(countrySequences)-1) * (len(countrySequences)-1) ) / 2, position = 0, leave = False)
    iter = 0
    for i in range(len(countrySequences)-1):
        for j in range(i + 1, len(countrySequences)):
            seq1 = countrySequences[i][3][:500]
            seq2 = countrySequences[j][3][:500]
            
            score = needWunschRust.getScore(seq1, seq2)
            scores[i][j] = float("{0:.2f}".format(score))
            scores[j][i] = float("{0:.2f}".format(score))

            loop.set_description("Loading...".format(iter))
            loop.update(1)
            iter += 1
    
    clust = Clustering.Clustering(scores, countries)
    for i in range(len(scores)):
        print(scores[i])

    print("\n\n\n")
    print(clust.getClustering(6))
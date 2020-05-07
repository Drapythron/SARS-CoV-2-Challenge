import LecturaCSV
import UrlSequence


if __name__ == '__main__':

    seq = LecturaCSV.LecturaCSV('sequences.csv', 'geoLocations.csv')
    secuenciasPaises = seq.median() #Este metodo devuelve una lista con todas las tuplas de los países

    #LLAMAMOS A LA CLASE 'UrlSequence' PARA OBTENER LAS SECUENCIAS DE ARN DE LOS PAÍSES DESDE LA WEB
    for i in range(len(secuenciasPaises)):
        seq = UrlSequence.UrlSequence(secuenciasPaises[i][0]).getSequence()
        secuenciasPaises[i].append(seq)

    








import urllib.request


class UrlSequence:
    __sequence = ''

    def __init__(self, accession):
        self.__accession = accession
        self.__callFile()

    def __callFile(self):
        # Enlace de descarga, finaliza con el accession a descargar
        url = ('http://www.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&rettype=fasta&id=' + self.__accession)
        urllib.request.urlretrieve(url, 'sequencesFASTA.fasta') # Obtenemos fichero con la sequencia ARN

    def getSequence(self):  
        # Leemos el fichero fasta con la sequencia de ARN
        seqFASTA = open('sequencesFASTA.fasta')
        reader = seqFASTA.readline()
        reader = seqFASTA.readline()
        while len(reader) != 0:
            reader = reader.replace('\n', '')   
            self.__sequence += reader           # Ajuntando todas sus lineas para facilitar el tratamiento de datos
            reader = seqFASTA.readline()
        return self.__sequence


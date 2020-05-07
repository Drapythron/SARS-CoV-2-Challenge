import urllib.request


class UrlSequence:
    __sequence = ''

    def __init__(self, accession):
        self.__accession = accession
        self.__callFile()

    def __callFile(self):
        url = ('http://www.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&rettype=fasta&id=' + self.__accession)
        urllib.request.urlretrieve(url, 'sequencesFASTA.fasta')

    def getSequence(self):
        seqFASTA = open('sequencesFASTA.fasta')
        reader = seqFASTA.readline()
        reader = seqFASTA.readline()
        while len(reader) != 0:
            reader = reader.replace('\n', '')
            self.__sequence += reader
            reader = seqFASTA.readline()
        return self.__sequence


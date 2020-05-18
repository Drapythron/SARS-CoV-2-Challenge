class NeedlemanWunsch:
    __sequence1 = ''
    __sequence2 = ''
    __matrix = []
    __alineament1 = ''
    __alineament2 = ''

    """__gap = -5
    __similarityMatrix = [[10, -1, -3, -4],
                          [-1, 7, -5, -3],
                          [-3, -5, 9, 0],
                          [-4, -3, 0, 8]]"""

    __gap = -1
    __similarityMatrix = [[1, -1, -1, -1],
                          [-1, 1, -1, -1],
                          [-1, -1, 1, -1],
                          [-1, -1, -1, 1]]
    __RNA = ['A', 'G', 'C', 'T']

    def __init__(self):
        self.__alineament1 = ''
        self.__alineament2 = ''

    def newEntry(self, sequence1, sequence2):
        self.__sequence1 = sequence1
        self.__sequence2 = sequence2
        self.__changeSequences()
        self.__initializeMatrix()

    def __initializeMatrix(self):
        self.__matrix = []
        # Inicializamos la matriz
        for i in range(len(self.__sequence1) + 1):  # Para que podamos ir desde 0 hasta el tamaño del str
            self.__matrix.append([i * self.__gap])
        for j in range(len(self.__sequence2)):
            self.__matrix[0].append((j + 1) * self.__gap)  # Para saltarnos el 0 y llegar hasta el tamaño del str

        # Creamos la matriz con los pesos
        for i in range(1, len(self.__sequence1) + 1):
            for j in range(1, len(self.__sequence2) + 1):
                posI = self.__RNA.index(self.__sequence1[i - 1])
                posJ = self.__RNA.index(self.__sequence2[j - 1])

                opcion1 = (self.__matrix[i - 1][j - 1] + self.__similarityMatrix[posI][posJ])
                opcion2 = (self.__matrix[i - 1][j] + self.__gap)
                opcion3 = (self.__matrix[i][j - 1] + self.__gap)

                self.__matrix[i].append(max(opcion1, opcion2, opcion3))

    def __changeSequences(self):
        self.__sequence1 = self.__sequence1.replace('N', 'A')  # Cambiamos las N's por A's
        self.__sequence2 = self.__sequence2.replace('N', 'A')  # Cambiamos las N's por A's

        self.__sequence1 = self.__sequence1.replace('K', 'G')  # Cambiamos las K's por G's
        self.__sequence2 = self.__sequence2.replace('K', 'G')  # Cambiamos las K's por G's

    def getScore(self):
        score = self.__matrix[len(self.__matrix)-1]

        #CREMOS LA NUEVA PUNTUACIÓN DE 0 A 100

        score += len(self.__alineament1)

        newScore = (score / (len(self.__alineament1) * 2)) * 100

        newScore = 100 - newScore

        return newScore
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
        self.__alignment()


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

    def __alignment(self):
        self.__alineament1 = ''
        self.__alineament2 = ''

        i = len(self.__sequence1)
        j = len(self.__sequence2)

        while i > 0 and j > 0:
            score = self.__matrix[i][j]
            scoreDiag = self.__matrix[i - 1][j - 1]
            scoreUp = self.__matrix[i - 1][j]
            scoreLeft = self.__matrix[i][j - 1]

            posI = self.__RNA.index(self.__sequence1[i - 1])
            posJ = self.__RNA.index(self.__sequence2[j - 1])

            if score == scoreDiag + self.__similarityMatrix[posI][posJ]:
                self.__alineament1 += self.__RNA[posI]
                self.__alineament2 += self.__RNA[posJ]
                i -= 1
                j -= 1
            elif score == scoreLeft + self.__gap:
                self.__alineament1 += '-'
                self.__alineament2 += self.__RNA[posJ]
                j -= 1
            elif score == scoreUp + self.__gap:
                self.__alineament1 += self.__RNA[posI]
                self.__alineament2 += '-'
                i -= 1

        while i > 0:
            posI = self.__RNA.index(self.__sequence1[i - 1])

            self.__alineament1 += self.__RNA[posI]
            self.__alineament2 += '-'
            i -= 1

        while j > 0:
            posJ = self.__RNA.index(self.__sequence2[j - 1])

            self.__alineament1 += '-'
            self.__alineament2 += self.__RNA[posJ]
            j -= 1

        return self.__alineament1, self.__alineament2

    def getAlineament(self):
        return self.__alineament1, self.__alineament2

    def getScore(self):
        score = 0
        for i in range(len(self.__alineament1)):
            if self.__alineament1[i] == '-' or self.__alineament2[i] == '-':
                score += self.__gap
            else:
                posI = self.__RNA.index(self.__alineament1[i])
                posJ = self.__RNA.index(self.__alineament2[i])
                score += self.__similarityMatrix[posI][posJ]

        return score

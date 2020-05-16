import random

class KMedoids:

    def __init__(self, matrix):
        self.matrix = matrix
    
    

    def getClustering(self, k):
        centers = self.__listaAleatorios(k)
        lastCenters = [[] for i in range(k)]
        return self.__clustering(k, lastCenters, centers)
    

    def __clustering(self, k, lastCenters, centers):
        #Comrobaremos que la lista de centros anteriores no sea igual a la anterior, si lo es, significará que hemos acamado el algoritmo.
        eq = True
        for i in range(len(centers)):
            if lastCenters[i] != centers[i]:
                eq = False
        if eq :
            return centers

        #Empezamos el algoritmo
        clusters = [[] for i in range(k)]
        newCenters = []

        for i in range(len(self.matrix)):
            temp = []
            for center in centers:
                temp.append(self.matrix[i][center])
            
            minim = min(temp)
            indexMin = temp.index(minim)
            clusters[indexMin] = i
        
        
        for cluster in clusters:
            possibleCenterIndex = []
            possibleCenter = []
            for i in cluster:
                temp = 0
                for j in cluster:
                    temp += self.matrix[i][j]
                possibleCenter.append(temp)
                possibleCenterIndex.append(i)
            minim = min(possibleCenter)
            indexMin = possibleCenter.index(minim)
            newCenters.append(possibleCenterIndex[indexMin])
        
        return self.__clustering(k, centers, newCenters)


    
    def __listaAleatorios(self, n):
      lista = [0]  * n
      for i in range(len(self.matrix)):
          lista[i] = random.random()
      return lista

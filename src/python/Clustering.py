import random

class Clustering:

    def __init__(self, matrix, countries):
        self.matrix = matrix
        self.countries = countries
    
    def getClustering(self, k):
        centers = self.__listaAleatorios(k)
        lastCenters = [-1 for i in range(k)]
        clusters = self.__clustering(k, lastCenters, centers, [])
        return self.__clustersToCountries(k, clusters)

    def __clustering(self, k, lastCenters, centers, clusters):
        #Comrobaremos que la lista de centros anteriores no sea igual a la anterior, si lo es, significará que hemos acamado el algoritmo.
        eq = True
        for i in range(len(centers)):
            if lastCenters[i] != centers[i]:
                eq = False
        if eq :
            return clusters
        print("centros: " + str(centers))
        #Empezamos el algoritmo
        clusters = [[] for i in range(k)]
        newCenters = []

        #Buscamos los clusters
        for i in range(len(self.matrix)):
            temp = []
            for j in range(len(centers)):
                center = centers[j]
                temp.append(self.matrix[i][center])
            
            if i in centers: #En el caso que tengamos que hay mas de dos 0's
                index = centers.index(i)
                clusters[index].append(i)
            else:
                minim = min(temp)
                indexMin = temp.index(minim)
                clusters[indexMin].append(i)
        print("clusters: " + str(clusters))

        #Sumamos las distancias
        for w in range(len(clusters)):
            cluster = clusters[w]
            possibleCenterIndex = []
            possibleCenter = []
            for posi in range(len(cluster)):
                adder = 0
                i = cluster[posi]
                for posj in range(len(cluster)):
                    j = cluster[posj]
                    adder += self.matrix[i][j]

                possibleCenter.append(adder)
                possibleCenterIndex.append(i)

            minim = min(possibleCenter)
            indexMin = possibleCenter.index(minim)
            newCenters.append(possibleCenterIndex[indexMin])
        
        return self.__clustering(k, centers, newCenters, clusters)

    def __listaAleatorios(self, n):
      lista = []
      i = 0
      while i < n:
          num = random.randrange(0, len(self.matrix))
          if num not in lista:
              lista.append(num)
              i += 1    
      return lista

    def __clustersToCountries(self, k, clusters):
        for i in range(len(clusters)):
            for j in range(len(clusters[i])):
                country = self.countries[clusters[i][j]]
                clusters[i][j] = country
        return clusters

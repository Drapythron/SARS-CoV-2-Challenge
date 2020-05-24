#Crearemos una árbol de clusters para que sea más gráfico las clasificaciones. 

import graphviz

class Graph:
    colors = ['blue', 'chartreuse', 'chocolate', 'darkgoldenrod', 'darkorchid4',
              'deeppink', 'deepskyblue4', 'firebrick2', 'green', 'indigo', 'orange4',
              'seagreen4', 'yellow']

    def __init__(self, clusters):
        self.clusters = clusters
    
    #Crearemos el nodo "padre" y luego iremos añadiendo los hijos y nietos que estos serán las diferentes clasificaciónes del clustering
    def createGraph(self):
        graph = graphviz.Digraph(format= 'png')
        graph.node('0', 'CLUSTERS', color='red')

        for i in range(len(self.clusters)):
            graph.node(str(i + 1), 'CLUSTER ' + str(i + 1), color = str(self.colors[i]))
            graph.edge('0', str(i + 1))
            for j in range(len(self.clusters[i])):
                graph.node(str(i + 1) + str(j), str(self.clusters[i][j]), color = str(self.colors[i]))
                graph.edge(str(i + 1), str(i + 1) + str(j))

        graph.render(filename='Resultado')
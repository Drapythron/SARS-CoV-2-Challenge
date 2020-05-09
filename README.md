# README de la pràctica SARS-CoV-2-Challange del grupo Drapythron

# Alineamiento sequenciado


## Lectura de fichero

En primer lugar abriremos el fichero .fasta que contiene todos los datos de los asseccion con la length mediana de la primera parte de la pràctica.
El nombre del fichero .fasta recibe el nombre de *sequencesFASTA.fasta*
El programa esta pensado para leer un fichero con:
1. Primera hilera iniciada por >accession | geoLocation
2. A continuación la sequencia de RNA a lo largo de multiples lineas. Nosotros uniremos todas estas lineas en una sola para una mejor lectura.

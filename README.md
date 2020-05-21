# README: SARS-CoV-2-Challenge (Drapythron)

Hoy en día, unos de los grandes objetivos a nivel internacional de la comunidad científica es conseguirá una vacuna para el virus SARS-CoV-2. Uno de los problemas más significantes del coronavirus es su rápida mutación. Expertos en computación quieren clasificar las diferentes muestras de ARN para poder crear un árbol genealógico.

**El objetivo de esta práctica, reto (challenge) es clasificar las diferentes muestras del virus que hay en el mundo y mostrar su árbol genealógico.**

**Tabla de contenidos:**

- [Autores](#Autores)
- [Preparación](#Preparación)
  - [Pre-requisitos](#Pre-requisitos)
  - [Instalación](#Instalación)
- [Ejecución](#Ejecución)
- [Construcción](#Construcción)
- [Licencia](#Licencia)
- [Expresiones de Gratitud](#Expresiones-de-Gratitud)


## Autores  

Los autores del SARS CoV-2 Challange y miembros del grupo Drapythron hemos realizado el reto de forma conjunta y coordinada. Todos hemos aportado en la programación del código y en el escrito de la documentación; sobretodo gracias a la gran comunicación y numerosas videoconferencias realizadas.

Los integrantes del equipo somos:

- Sergio Beltrán Guerrero
- Jaume Guasch Llobera
- Martí Serratosa Sedó
- Sebastian Bampton Blasco

## Preparación

Para un correcto funcionamiento del programa SARS-CoV-2-Challange de Drapythron solo necesitarás tener  acceso a la herramienta de programación Python y a Internet. Estos dos aspectos si los juntamos con los ficheros del software harán que el programa se desarrolle de forma satisfactoria.

### Pre-requisitos

Para poder hacer un uso correcto del software necesitamos un fichero .csv con las secuencias a analizar y el *"locations.csv"*.

#### "sequences.csv"

Drapythron ya te proporciona el fichero *sequences.csv* pero el usuario puede usar su propio fichero. 

Para obtener los datos del virus y que no haya sorpresas a posteriori recomendamos usar la página web de la *National Center for Biotechnology Information database* para descargar los datos ([NCBI database](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?VirusLineage_ss=Severeacuterespiratorysyndromecoronavirus2(SARS-CoV-2),taxid:2697049&SeqType_s=Nucleotide "National Center for Biotechnology Information database")). Su correcta descarga seguiría este procedimiento:

1. Seleccionar los **nucleotides** que queramos. A la izquiera podemos poner condiciones.
2. Pulsar a **Download**.
3. Seleccionar en el paso 1: *Current table view result* → **CSV format**.
4. En el paso 2: **Download Selected Records**.
5. En el paso 3 las columnas que **hay que seleccionar al ser necesarias** para el correcto funcionamiento son: **Accession, Length y Geo Location**. La otra información no es necesaria.

#### "locations.csv"

El fichero *locations*  ya viene proporcionado pero si se usa un *sequences* que no es el proporcionado por Drapythron se tendrá que reajustar. El motivo por readequarlo es que en el futuro habrá más y más analisis y apareceran nuevos países y regiones que no estan contemplados.
Para actualizar el fichero "locations.csv" observa como esta formado. En la primera fila, como todo fichero .csv hay todos los países, al final podremos añadir los nuevos paises que ya no haya sido apuntados.
A continuació, tendremos que ir añadiendo hileras al final donde añadiremos las regiones / países. Para hacerlo correctamente tendremos que ir escribiento ; (puntos y comas) de forma unida hasta llegar a la que les corresponde a la columna del país dónde procederemos a escribir la región.

### Instalación

Para tener una correcta instalación del programa solo es imprescindible que los ficheros .py no hayan sido modificados, y se mantengan todos juntos en una misma carpeta.

## Ejecución

El programa funciona de forma automática, una vez es iniciado por el usuario no requiere que este interactue de ninguna manera. Al final del proceso se le devolverán los resultados esperados.

### Ejemplo de ejecución

La ejecución de la práctica se realiza en el *Main.py*. El fichero empieza leyendo las secuencias y calculando las medianas de los países. A continuación descarga de Internet la secuencia *.fasta* de ARN de la mediana de cada país. A continuación, alineamos los países con el mètodo NeedlemanWunsch de dónde extraeremos una puntuación que nos indica la similutud del la secuencia entre dos muestras del Covid-19 en dos países. Finalmente, clasificamos los datos para poder ver mejor los resultados extraidos.
**ACTUALIZAR CODIGO CON LA TERCERA PARTE!**

```python
import LecturaCSV
import UrlSequence
import NeedlemanWunsch


if __name__ == '__main__':

    seq = LecturaCSV.LecturaCSV('sequences.csv', 'geoLocations.csv')
    countrySequences = seq.median() #Este metodo devuelve una lista con todas las tuplas de los país

    #LLAMAMOS A LA CLASE 'UrlSequence' PARA OBTENER LAS SECUENCIAS DE ARN DE LOS PAÍSES DESDE LA WEB
    for i in range(len(countrySequences)):
        seq = UrlSequence.UrlSequence(countrySequences[i][0]).getSequence()
        countrySequences[i].append(seq)
        print(str(countrySequences[i][2]) + ' cargado.')

    #GURDAMOS LOS SCORES EN UNA TABLA

    countryScores = []
    needlemanWunsch = NeedlemanWunsch.NeedlemanWunsch()
    print('Alineando paises...')
    for i in range(len(countrySequences)-1):
        countryScores.append([])
        for j in range(i + 1, len(countrySequences)):
            seq1 = countrySequences[i][3]#[:1000]
            seq2 = countrySequences[j][3]#[:1000]
            needlemanWunsch.newEntry(seq1, seq2)
            score = needlemanWunsch.getScore()
            countryScores[i].append((countrySequences[i][2], countrySequences[j][2], score))
            print((countrySequences[i][2], countrySequences[j][2], score))
```

## Construcción

Las herramientas usada para crear el proyecto han sido tres:

* [PyCharm](https://www.jetbrains.com/pycharm/ "PyCharm: Python tool") - Software para programar con Python.
* [Typora](https://typora.io/ "Typora: markdown editor") - Software para editar y leer ficheros markdown.
* [Github](https://github.com/ "Github: web de desarrollo colaborativo") - Web para compartir los ficheros del proyecto entre los miembros del equipo.
* Visual Studio Code

## Licencia

Este proyecto está bajo la Licencia de Creative Commons [Reconocimiento 4.0 Internacional](http://creativecommons.org/licenses/by/4.0/) que permite:

* Compartir: copiar y redistribuir el material bajo cualquier medio y formato.
* Adaptar: transformar, adaptar y construir el material para cualquier proposito, incluso comercial.

## Expresiones de Gratitud

Queriamos mostrar nuestra más sincera expresión de gratitud a la **Universitat de Lleida** por adaptar-se a la situación actual devida al CoVid-19 intentando no perjudicar a los estudiantes y, en concreto al professor **Jordi Planes** ([Github](https://github.com/jordiplanes)) por su esforzo para apoyar a los estudiantes.

---
<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Licencia de Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />Este obra está bajo una <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">licencia de Creative Commons Reconocimiento-NoComercial 4.0 Internacional</a>.

Drapythron Team © 2020

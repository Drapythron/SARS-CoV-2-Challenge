# INFORME: SARS CoV-2 Challenge (Drapythron)

Los autores del SARS CoV-2 Challenge y miembros del grupo Drapythron somos:

- Sergio Beltrán Guerrero
- Jaume Guasch Llobera
- Sebastian Bampton Blasco
- Martí Serratosa Sedó

El programa utilizado para programar el codigo han sido PyCharm donde hemos trabajado con classes. Hay clases que corresponden exactamente con partes de la pràctica y otras partes tienen más de una classe. Para el redactado en markdown hemos utilizado Typora, tanto el informe como el readme han sido únicamente trabajados con markdown.

El informe lo dividiremos en una introducció, las diferentes partes de la práctica: preprocesamiento, alineamiento sequencial y clasificación, y, conlusión. Dentro de cada sección ya habrá más apardos si es conveniente.

**Tabla de contenidos:**

- [0. Introducción](#0.-Introducción)
- [1. Preprocesamiento](#1.-Preprocesamiento)
  - [1.1 Lectura de archivos.csv](##-1.1-Lectura-de-archivos-.csv)
  - [1.2 Función mediana(geoLocation)](##1.2-Función-mediana(geoLocation))
- [3. Alineamiento sequencial](#3.-Alineamiento-sequencial)
  - [3.1 UrlSequence](##3.1-UrlSequence)
  - [3.2 NeedlemanWunsch](##-3.2-NeedlemanWunsch)
- [4. Clasificación](#4.-Clasificación)
- [5. Conclusión](#5-conclusión)

# 0. Introducción

Hoy en día, unos de los grandes objetivos a nivel internacional de la comunidad científica es aconseguir una vacuna para el virus SARS-CoV-2. Uno de los problemas más significantes del coronavirus es su rápida mutación. Expertos en computación quieren clasificar las diferentes muestas de ARN para poder crear un árbol genalógico.

**El objetivo de esta práctica, reto (challenge) es clasificar las diferentes muestras del virus que hay en el mundo y mostrar su árbol genalógico.**

La ejecucion del programa se realiza en el Main.py este a su vez llamará otras classes para poder realizar las funciones deseadas. El orden de uso de la diferentes clases es el siguiente:

1. LecturaCSV
2. UrlSequence
3. NeedlemanWunsch
4. **ACTUALITZAR!!!!**



# 1. Preprocesamiento

La primera parte de la práctica consiste en la lectura de un archivo csv con las secuencias para poder calcular la mediana de cada país. Esta parte se ha realizado integramente en **la classe *LecturaCSV***. 

A continuación hay las correspondientes explicaciones a las funciones de la clase.



## 1.1 Lectura de archivos .csv

En nuestro programa leeremos dos archivos. Primero uno de creación propia que contiene todas la ubicaciones que se han publicado en la *National Library of Medicine* a fecha de 1 de mayo de 2020. A continuación, el archivo csv de sequences tambien obtenido de la misma página web a fecha de 31 de abril de 2020 con los datos sobre nucleoides publicados alrededor del mundo.



### 1.1.1 Lectura del archivo *geoLocations.csv*

Primero abriremos el archivo .csv que hemos creado anteriorment. Este archivo tiene este tipo de formato:

| Iraq | Tunisia        | China                | South Africa                 |
| ---- | -------------- | -------------------- | ---------------------------- |
| Iraq | Tunisia        | China: Nanchang      | South Africa:  KwaZulu-Natal |
|      | Tunisia: Tunis | China: Anhui, Fuyang |                              |
|      |                | China: Wuhan         |                              |
|      |                | China: Beijing       |                              |
|      |                | China                |                              |
|      |                | Hong Kong            |                              |

*Tabla de muestra, no está completa. Hay muchos más países y regiones en cada país.*

Como se puede observar, en la cabezera, la fila 0, hay todos los países y en cada columna del país aparecen debajo sus regiones/país entero/etc.

Ahora procederemos a guardar todos los datos del fichero .csv en el programa con la función saveGeoLocation.



####  1.1.1.1 Función saveGeoLocation(reader)

La función saveGeoLocations básicamente hace dos cosas al tratar el fichero:

1. Ir añadiendo cada país a *locations*, cogiendo los valores de la primera fila.
2. Ir añadiendo a cada país (*locations[pos]*) todas sus correspondientes regiones.

Devuelve *locations*.

El coste de este proceso es **O(n<sup>2</sup>)**, donde n es el número de líneas del archivo csv por su profundiad.




####  1.1.1.2 Función newLocation(oldLocation, locations):

La función newLocation coge el valor de la ubicación del fichero *sequences.csv* (oldLocation) y buscará su correspondiente país, por este motivo pasamos *locations*.

Buscaremos la ubicación pasada entre todas las *locations*, si la encuentra devolvemos el país dejando de lado la región si la tuviese. En caso de que no la encuentre devolveremos su GeoLocation: oldLocation.

El coste de este proceso es **O(n)**, donde n es el número de ubicaciones en *locations*.



### 1.1.2 Lectura del archivo *sequences.csv*

Primero de todo abrimos el archivo .csv para poder leer las secuencias de los países.

Luego leeremos y almacenaremos línea a línea los datos más relevantes: accession, length y geoLocation. Lo almacenaremos como tuplas (accession, length, geoLocation) para poder trabajar de manera más sencilla. Además también crearemos una lista con todos los países.

El coste de este proceso es **O(n)**, donde n es el número de líneas del archivo csv.

Seguidamente realizaremos la mediana de estos países. Para realizarla, iniciaremos un bucle con todos los países. En este bucle tenemos la función mediana, que nos devolverá la tupla "mediana" de el país.

Este proceso tiene un coste de **O(n)**, donde n es el número de países.



## 1.2 Función mediana(geoLocation)

En esta función, analizaremos todas las tuplas de la secuencia. Iremos comparando una a una con la geoLocation pasada. Si la tupla coincide, la almacenaremos la tupla en la lista 'analysisList' y el length en 'idems'. Una vez hemos comparado todas las tuplas de la secuencia, realizaremos la mediana de la lista 'idems'.

Una vez tenemos el resultado tenemos la mediana, podemos realizar dos opciones:

1. Sí la mediana esta contenida en la lista, devolveremos la posición de la mediana en la lista.

2. Sí la mediana no esta contenida en la lista, buscaremos el valor que más se acerque a la mediana.

   ```pyton
   result = analysisList[min(range(len(idems)), key = lambda i: abs(idems[i] - median))]
   ```

Una vez tenemos la posición de la mediana en la lista, devolveremos la tupla en la posición de 'analysisiList'

Este proceso tiene un coste de ***O(n)***, donde n es el tamaño de 'sequences'.

En definitiva, el proceso de lectura del archivo csv y la devolución de la mediana de cada país tiene un coste de ***O(n<sup>3</sup>)*** .



### 1.2.1 Función median

Esta función nos sirve para encontrar la mediana de los valores de la lista. La mediana devuelve el valor que se encuentra en medio de la lista.

Para ello primero tendremos que ordenar la lista, nosaltros utilizamos el métode de *Divide y Vencerás* [**Merge Sort**](https://en.wikipedia.org/wiki/Merge_sort) (explicado en el siguiente apartado).

Según la longitud de la lista (si finaliza en impar o par) la mediana puede encontrarse en un único número (impar), o entre dos posiciones (par).

Si la longitud de la lista es impar, significa que podremos encontrar la mediana en un único resultado, el valor del medio al tener la lista ordenada. Por el otro lado, en caso de longitud de la lista par, la mediana la obtendremos entre dos números, el de delante y atrás del valor del medio, y por tanto tendremos que hacer la media de los valores en conflicto. El coste de este proceso es **O(1)**, ya que solo contiene un if-else.



### 1.2.2 Función mergeSort

En la función mergeSort pretendemos ordenar las longitudes de las secuencias de menor a mayor en una lista, siendo el objetivo final poder obtener el elemento que forma la mediana de la lista.

El algoritmo empleado es del tipo "**divide y vencerás**", con un coste de **O(n·log(n))** y se emplea de forma recursiva.

En el algoritmo dividimos la lista proporcionada en dos partes, siendo la única condición que la longitud de las listas a dividir sea mayor que dos. El objetivo ahora es seguir dividiendo las dos listas obtenidas sucesivamente hasta obtener listas con elementos individuales o pares.

Una vez hemos obtenido listas formadas por uno/dos elemento(s), compararemos los valores y ordenaremos las listas, una vez realizada la ordenación de los elementos en las listas, concatenamos las listas para reducir todos los elementos a una sola lista ordenada, la cual devolvemos.

# 3. Alineamiento sequencial

La segunda parte de la práctica consiste en realizar dos tareas. 

* La primera tarea es la lectura del ARN de cada nucleoide de la mediana del país encontrada en la primera parte. Para realizar esta tarea usaremos **la clase UrlSequence**.
* La segunda tarea es comparar el código genetico entre dos paises para ver como ha mutado. Para su realización usaremos **la clase NeedlemanWunsch**.

## 3.1 UrlSequence

La clase UrlSequence **obtiene los datos ARN de la base de datos de la NCBI al pasarle un *accession***.

Para proceder a la obtención de la secuencia ARN primero de todo usando el *accession* descargaremos la secuencia ARN en formato .fasta. Para conseguirlo usamos el método *urllib.request.urlretrieve(url, 'sequencesFASTA.fast')* que nos creará un fichero temporal con los datos de la secuencia. 

A continuación, procederemos a su lectura. Iremos recorriendo todo el fichero con *.readLine()* borrando los espacios y intros si ubiese para al final añadirlo a nuestra base de datos propia. Esta base de datos ahora estará compuesta por **['Accession', 'Length', 'GeoLocation', 'ARN']**.

En el Main, tendremos un bucle que llamará a esta classe para que busque el ARN de cada *accession* de la mediana de cada país, datos obtenidos del *1. Preprocesamiento*.



## 3.2 NeedlemanWunsch

blablabla



# 4. Clasificación

blablabla



# 5. Conclusión

blablabla



---
<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Licencia de Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />Este obra está bajo una <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">licencia de Creative Commons Reconocimiento-NoComercial 4.0 Internacional</a>.

Drapythron Team © 2020

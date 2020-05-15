# INFORME: SARS CoV-2 Challenge (Drapythron)

Los autores del SARS CoV-2 Challenge y miembros del grupo Drapythron somos:

- Sergio Beltrán Guerrero
- Jaume Guasch Llobera
- Sebastian Bampton Blasco
- Martí Serratosa Sedó

El programa utilizado para programar el código han sido PyCharm donde hemos trabajado con clases. Hay clases que corresponden exactamente con partes de la práctica y otras partes tienen más de una clase. Para el redactado en markdown hemos utilizado Typora, tanto el informe como el readme han sido únicamente trabajados con markdown.

El informe lo dividiremos en una introducción, las diferentes partes de la práctica: preprocesamiento, alineamiento sequencial y clasificación, y, conclusión. Cada sección con sus apartados convenientes.

**Tabla de contenidos:**

- [0. Introducción](#0-Introducción)
- [1. Pre-procesamiento](#1-pre-procesamiento)
  - [1.1 Lectura de archivos.csv](#11-lectura-de-archivos-csv)
  - [1.2 Función mediana(geoLocation)](##12-Función-mediana(geoLocation))
- [3. Alineamiento sequencial](#3-Alineamiento-sequencial)
  - [3.1 UrlSequence](##31-UrlSequence)
  - [3.2 NeedlemanWunsch](##-32-NeedlemanWunsch)
- [4. Clasificación](#4-Clasificación)
- [5. Conclusión](#5-conclusión)

# 0. Introducción

Hoy en día, unos de los grandes objetivos a nivel internacional de la comunidad científica es hallar una vacuna para el virus SARS-CoV-2. Uno de los problemas más significantes del coronavirus, es su rápida mutación. Expertos en computación quieren clasificar las diferentes muestras de ARN para poder crear un árbol genealógico.

**El objetivo de esta práctica, reto (challenge) es clasificar las diferentes muestras del virus que hay en el mundo y mostrar su árbol genealógico.**

La ejecución del programa se realiza en el [__init__.py](python/__init__.py) este a su vez llamará otras clases para poder realizar las funciones deseadas. El orden de uso de la diferentes clases es el siguiente:

1. LecturaCSV
2. UrlSequence
3. NeedlemanWunsch
4. **ACTUALITZAR!!!!**

# 1. Pre-procesamiento

La primera parte de la práctica consiste en la lectura de un archivo csv con las secuencias para poder calcular la mediana de cada país. Esta parte se ha realizado íntegramente en **la clase *LecturaCSV***.

A continuación hay las correspondientes explicaciones de los métodos de la clase.

## 1.1 Lectura de archivos .csv

En nuestro programa leeremos dos archivos. Primero uno de creación propia que contiene todas la ubicaciones que se han publicado en la *National Library of Medicine* a fecha de 1 de mayo de 2020. A continuación, el archivo csv de sequences también obtenido de la misma página web a fecha de 31 de abril de 2020 con los datos sobre nucleotidos publicados alrededor del mundo.

### 1.1.1 Lectura del archivo *geoLocations.csv*

Primero abriremos el archivo .csv que hemos creado anteriormente. Este archivo tiene este tipo de formato:

| Iraq | Tunisia        | China                | South Africa                 |
| ---- | -------------- | -------------------- | ---------------------------- |
| Iraq | Tunisia        | China: Nanchang      | South Africa:  KwaZulu-Natal |
|      | Tunisia: Tunis | China: Anhui, Fuyang |                              |
|      |                | China: Wuhan         |                              |
|      |                | China: Beijing       |                              |
|      |                | China                |                              |
|      |                | Hong Kong            |                              |

*Tabla de muestra, no está completa. Hay muchos más países y regiones en cada país.*

Como se puede observar, en la cabecera, la fila 0, están todos los países sin regiones y en cada columna del país aparecen debajo sus regiones.

Ahora procederemos a guardar todos los datos del fichero .csv en el programa con la función saveGeoLocation.

Si en el futuro la web *National Library of Medicine* añadiese más regiones de los países, ej: Spain:Madrid, solo hará falta ir al archivo y añadir en la columna de Spain, Spain:Madrid.

#### 1.1.1.1 Método saveGeoLocation(reader)

El método saveGeoLocations básicamente hace dos cosas al tratar el fichero:

1. Ir añadiendo cada país a *locations*, cogiendo los valores de la primera fila.
2. Ir añadiendo a cada país (*locations[pos]*) todas sus correspondientes regiones.

Devuelve *locations*.

El coste de este proceso es **O(n<sup>2</sup>)**, donde n es el número de líneas del archivo csv por su profundidad.

#### 1.1.1.2 Método newLocation(oldLocation, locations)

El método newLocation coge el valor de la ubicación del fichero *sequences.csv* (oldLocation) y buscará su correspondiente país, por este motivo pasamos *locations*.

Buscaremos la ubicación pasada entre todas las *locations*, si la encuentra devolvemos el país dejando de lado la región si la tuviese. En caso de que no la encuentre devolveremos su GeoLocation: oldLocation.

El coste de este proceso es **O(n)**, donde n es el número de ubicaciones en *locations*.

### 1.1.2 Lectura del archivo *sequences.csv*

Primero de todo abrimos el archivo .csv para poder leer las secuencias de los países.

Luego leeremos y almacenaremos línea a línea los datos más relevantes: accession, length y geoLocation. Lo almacenaremos como tuplas (accession, length, geoLocation) para poder trabajar de manera más sencilla. Además también crearemos una lista con todos los países.

El coste de este proceso es **O(n)**, donde n es el número de líneas del archivo csv.

Seguidamente realizaremos la mediana de estos países. Para realizarla, iniciaremos un bucle con todos los países. En este bucle tenemos la función mediana, que nos devolverá la tupla "mediana" de el país.

Este proceso tiene un coste de **O(n)**, donde n es el número de países.

## 1.2 Método mediana(geoLocation)

En esta método, analizaremos todas las tuplas de la secuencia. Iremos comparando una a una con la geoLocation pasada. Si la tupla coincide, la almacenaremos la tupla en la lista 'analysisList' y el length en 'lengths'. Una vez hemos comparado todas las tuplas de la secuencia, realizaremos la mediana de la lista 'idems'.

Una vez tenemos el resultado tenemos la mediana, podemos realizar dos opciones:

1. Sí la mediana esta contenida en la lista, devolveremos la posición de la mediana en la lista.

2. Sí la mediana no esta contenida en la lista, buscaremos el valor que más se acerque a la mediana con el siguiente código:

   ```python
   result = analysisList[min(range(len(idems)), key = lambda i: abs(idems[i] - median))]
   ```

Una vez tenemos la posición de la mediana en la lista, devolveremos la tupla en la posición de 'analysisList'

Este proceso tiene un coste de ***O(n)***, donde n es el tamaño de 'sequences'.

En definitiva, el proceso de lectura del archivo csv y la devolución de la mediana de cada país tiene un coste de ***O(n<sup>3</sup>)*** .**REVISAR**

### 1.2.1 Función median

Esta función nos sirve para encontrar la mediana de los valores de la lista. La mediana devuelve el valor que se encuentra en medio de la lista.

Para ello primero tendremos que ordenar la lista, nosotros hemos utilizamos el método de *Divide y Vencerás* [**Merge Sort**](https://en.wikipedia.org/wiki/Merge_sort) (explicado en el siguiente apartado).

Según la longitud de la lista (si finaliza en impar o par) la mediana puede encontrarse en un único número (impar), o entre dos posiciones (par).

Si la longitud de la lista es impar, significa que podremos encontrar la mediana en un único resultado, el valor del medio al tener la lista ordenada. Por el otro lado, en caso de longitud de la lista par, la mediana la obtendremos entre dos números, el de delante y atrás del valor del medio, y por tanto tendremos que hacer la media de los valores en conflicto. El coste de este proceso es **O(1)**, ya que solo contiene un if-else.

### 1.2.2 Función mergeSort

En la función mergeSort pretendemos ordenar las longitudes de las secuencias de menor a mayor en una lista, siendo el objetivo final poder obtener el elemento que forma la mediana de la lista.

El algoritmo empleado es del tipo "**divide y vencerás**", con un coste de **O(n·log(n))** y se emplea de forma recursiva.

En el algoritmo dividimos la lista proporcionada en dos partes, siendo la única condición que la longitud de las listas a dividir sea mayor que dos. El objetivo ahora es seguir dividiendo las dos listas obtenidas sucesivamente hasta obtener listas con elementos individuales o pares.

Una vez hemos obtenido listas formadas por uno/dos elemento(s), compararemos los valores y ordenaremos las listas, una vez realizada la ordenación de los elementos en las listas, concatenamos las listas para reducir todos los elementos a una sola lista ordenada, la cual devolvemos.

# 3. Alineamiento secuencial

La segunda parte de la práctica consiste en realizar dos tareas.

* La primera tarea es la lectura del ARN de cada nucleotido de la mediana del país encontrada en la primera parte. Para realizar esta tarea usaremos la [**Clase UrlSequence**](python\UrlSequence.py).
* La segunda tarea consiste en alinear las secuencias de ARN y compararlas. Esta tarea la hemos implementado de dos formas. Usando el lenguaje de programación Python y usando el lenguaje de programación Rust.
  + La [**Clase NeedlemanWunsch**](python/NeedlemanWunsch.py) es la clase que hemos implementado en Python.
  + La [**Clase NeedlemanWunschRust**](python\NeedlemanWunschRust.py)  es la clase que hemos implementado en Rust.

## 3.1 UrlSequence

La clase UrlSequence **obtiene los datos ARN de la base de datos de la NCBI cuando le pasamos un *accession***.

Para proceder a la obtención de la secuencia ARN primero de todo usando el *accession* descargaremos la secuencia ARN en formato .fasta. Para conseguirlo usamos el método `urllib.request.urlretrieve(url, 'sequencesFASTA.fast')` que nos creará un fichero temporal con los datos de la secuencia.

A continuación, procederemos a su lectura. Iremos recorriendo todo el fichero con *.readLine()* borrando los espacios y saltos de linea. Las secuencias ya listas las añadiremos en una lista junto a accession, length y geolocation. Tal que así **['Accession', 'Length', 'GeoLocation', 'ARN']**.

En el init, tendremos un bucle que llamará a esta clase para que busque el ARN de cada *accession* de la mediana de cada país, datos obtenidos del *1. Pre-procesamiento*.

## 3.2 NeedlemanWunsch

Este algoritmo nos ayudará a obtener una puntuación en base al alineamiento de dos códigos genéticos de distintos países.
El alineamiento de secuencias es una forma de comparar dos secuencias haciendo hincapié en las zonas donde hay similitudes.
NeedlemanWunsch es el algoritmo más utilizado para comparar código genético.
Se trata de un algoritmo de orden ***O(nm)***.

Como ya hemos comentado anteriormente, hemos realizado dos implementaciónes de este algoritmo.

Primero de todo, vamos a aclarar las cosas que hay en común en las dos implementaciones.

- Los pesos para comparar son: **gap** = -1, **match** = 1 y **mismatch** = -1.

- Hemos remplazado los ácidos nucleicos que no son estándar por los estándar. El criterio que hemos seguido es el siguiente, hay ácidos nucleicos que pueden significar dos o más ácidos, por lo tanto, hemos escogido uno de los ácidos que puede significar. La siguiente tabla lo deja todo claro.

|Código de ácido nucleico |Significado |Ácido escogido|
|-------------------------|------------|--------------|
|N                        |A, G, C, T  |A             |
|B                        |G, T, C     |G             |
|Y                        |T, C        |T             |

### 3.2.1 Needleman-Wunsch en Python

Para realizar esta implementación nos hemos basado en el pseudo-código de [Wikipedia](https://es.wikipedia.org/wiki/Algoritmo_Needleman-Wunsch). El código lo hemos dividido en tres partes, la primera que nos inicia la matriz con sus pesos. Una vez tenemos la matriz creada, llamamos al método `__alignment`, para que nos realice la alineación de las secuencias usando programación dinámica. Una vez acaba el algoritmo obtenemos dos String, que estos son las secuencias alineadas. Y finalmente, para obtener la puntuación, compararemos uno a uno los ácidos de las dos secuencias, para devolver su puntuación.
A la hora de puntuar, hemos decidido que el rango de puntuación sea de [0, 100], 0 significara que son iguales y 100 que son totalmente distintas. El criterio que hemos utilizado para devolver esta puntuación es el siguiente:

  1. Como hemos escogido que, gap = -1, match = 1 y mismatch = -1, tendremos que el rango de puntuación seá [-len(secuencia_alienada), len(secuencia_alineada)].

  2. Desplazaremos a la derecha el rango para que todos los valores sean positivos, [0, len(secuencia_alineada)*2] y también desplazaremos la puntuación obtenida tal que así: `puntuación + len(secuencia_alineada)`.

  3. Realizaremos una simple regla de 3.

  ``` r

    (puntuación_desplazada / len(secuencia_alineada)*2) * 100 = nueva_puntuación

    nueva_puntuación = 100 - nueva_puntuación

  ```

### 3.2.1 Needleman-Wunsch en Rust

Para mejorar la velocidad del algoritmo hemos implementado el algoritmo anterior en el lenguaje de Programación [Rust](https://www.rust-lang.org/es/). Hemos creado una [librería](rust/src/lib.rs) en Rust con las funciones de alinear y puntuación. Una vez creada la hemos compilado y importado a nuestro código en Python.
A la hora de implementar el código en Rust, hemos importado una librería que se llama *Simple_Matrix*, la cual nos crea una matriz de enteros, con la que trabajaremos. Las demás implementaciones son igual que en python pero traducido a Rust.

# 4. Clasificación

blablabla



# 5. Conclusión

blablabla



---
<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Licencia de Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />Este obra está bajo una <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">licencia de Creative Commons Reconocimiento-NoComercial 4.0 Internacional</a>.

Drapython Team © 2020

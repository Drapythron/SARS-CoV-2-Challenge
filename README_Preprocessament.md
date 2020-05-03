# Preprocessament SARS CoV-2 Challange (Drapythron)

Los autores de la primera parte del SARS CoV-2 Challange, el *Preprocessament*, y miembros del grupo Drapythron somos:

- Sergio Beltrán Guerrero
- Jaume Guasch Llobera
- Sebastian Bampton Blasco
- Martí Serratosa Sedó



**Tabla de contenidos:** (en el github online no aparece la tabla, en otros programas sí)

[TOC]

## Lectura de archivos .csv

En nuestro programa leeremos dos archivos. Primero uno de creación propia que contiene todas la ubicaciones que se han publicado en la *National Library of Medicine* a fecha de 1 de mayo de 2020. A continuación, el archivo csv de sequences tambien obtenido de la misma página web a fecha de 31 de abril de 2020 con los datos sobre nucleoides publicados alrededor del mundo.

### Lectura del archivo *geoLocations.csv*

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

Como se puede observar, en la cabezera, la fila 0, hay todos los países y en cada columna del país sus regiones/país enteor/etc.

Ahora procederemos a guardar todos los datos del fichero .csv en el programa con la función saveGeoLocation.



####  Función saveGeoLocation(reader)

La función saveGeoLocations bàsicamente hace dos cosas al tratar el fichero.

1. Ir añadiendo cada país a *locations*, coge los valores de la primera fila.
2. Ir añadiendo a cada país (*locations[pos]*) todas sus correspondientes regiones.

Devuelve *locations*.

El coste de este proceso es **O(n<sup>2</sup>)**, donde n es el número de líneas del archivo csv por su profundiad.




####  Función newLocation(oldLocation, locations):

La función newLocation coge el valor de la ubicación del fichero *sequences.csv* (oldLocation) y buscará su correspondiente país, por este motivo pasamos *locations*.

Buscaremos la ubicación pasada entre todas las *locations*, si la encuentra devolvemos el país dejando de lado la región si la tuviese. En caso de que no la encuentre devolveremos su GeoLocation: oldLocation.

El coste de este proceso es **O(n)**, donde n es el número de ubicaciones en *locations*.



### Lectura del archivo *sequences.csv*

Primero de todo abrimos el archivo .csv para poder leer las secuencias de los países.

Luego leeremos y almacenaremos línea a línea los datos más relevantes: accession, length y geoLocation. Lo almacenaremos como tuplas (accession, length, geoLocation) para poder trabajar de manera más sencilla. Además también crearemos una lista con todos los países.

El coste de este proceso es **O(n)**, donde n es el número de líneas del archivo csv.

Seguidamente realizaremos la mediana de estos países. Para realizarla, iniciaremos un bucle con todos los países. En este bucle tenemos la función mediana, que nos devolverá la tupla "mediana" de el país.

Este proceso tiene un coste de **O(n)**, donde n es el número de países.



## Función mediana(geoLocation)

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



### Función median

Esta función nos sirve para encontrar la mediana de los valores de la lista. La mediana devuelve el valor que se encuentra en medio de la lista.

Para ello primero tendremos que ordenar la lista, nosaltros utilizamos el métode de *Divide y Vencerás* **Merge Sort** (explicado en el siguiente apartado).

Según la longitud de la lista (si finaliza en impar o par) la mediana puede encontrarse en un único número (impar), o entre dos posiciones (par).

Si la longitud de la lista es impar, significa que podremos encontrar la mediana en un único resultado, el valor del medio al tener la lista ordenada. Por el otro lado, en caso de longitud de la lista par, la mediana la obtendremos entre dos números, el de delante y atrás del valor del medio, y por tanto tendremos que hacer la media de los valores en conflicto.

El coste de este proceso es **O(1)**, ya que solo contiene un if-else. **REVISAR!!!!**



### Función mergeSort

**JAUMEE** guapo intenta calcular lo de sote:

El coste de este proceso es **O(?)**, donde n es el número de ???.

Al final del document tens la solució, la que crec vamos



# AIXÒ S'HAURIA DE BORRAR OI???

## Futuros cambios

- Modificar el result, en vez de devolver la tupla, que se devuelva una lista con todas las 'accession', así podremos mejorar el proceso de búsqueda en la web de los datos del COVID-19.
- Mejora del coste en mediana. Eliminar de 'sequences' las tuplas ya analizadas. Así realizaremos menos vueltas a la hora de comparar con los geoLocation.









# **La solució és:** O(n·log(n))

## donde n es la longitud de la lista




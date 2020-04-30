# -SARS-CoV-2-Challange
# Lectura del archivo .csv

Primero de todo abrimos el archivo .csv para poder leer las secuencias de los países.

Luego leeremos almacenaremos línea a línea los datos más relevantes: accession, length y geoLocation. Lo almacenaremos como tuplas (accession, length, geoLocation) para poder trabajar de manera más sencilla. Además también crearemos una lista con todos los países.

El coste de este proceso es **O(n)**, donde n es el número de líneas del archivo csv.

Seguidamente realizaremos la mediana de estos países. Para realizarla, iniciaremos un bucle con todos los países. En este bucle tenemos la función mediana, que nos devolverá la tupla "mediana" de el país.

Este proceso tiene un coste de **O(n)**, donde n es el número de países.

## Función mediana

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



## Futuros cambios

- Modificar el result, en vez de devolver la tupla, que se devuelva una lista con todas las 'accession', así podremos mejorar el proceso de búsqueda en la web de los datos del COVID-19.
- Mejora del coste en mediana. Eliminar de 'sequences' las tuplas ya analizadas. Así realizaremos menos vueltas a la hora de comparar con los geoLocation.

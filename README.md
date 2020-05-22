# README: SARS-CoV-2-Challenge (Drapythron)

Hoy en día, unos de los grandes objetivos a nivel internacional de la comunidad científica es conseguirá una vacuna para el virus SARS-CoV-2. Uno de los problemas más significantes del coronavirus es su rápida mutación. Expertos en computación quieren clasificar las diferentes muestras de ARN para poder crear un árbol genealógico.

**El objetivo de esta práctica, reto (challenge) es clasificar las diferentes muestras del virus que hay en el mundo y mostrar su árbol genealógico.**

**Tabla de contenidos:**

- [Autores](#autores)
- [Preparación](#preparación)
  - [Requisitos](#requisitos)
- [Ejecución](#ejecución)
- [Construcción](#construcción)
- [Expresiones de Gratitud](#expresiones-de-gratitud)

## Autores  

Los autores del SARS CoV-2 Challange y miembros del grupo Drapythron hemos realizado el reto de forma conjunta y coordinada. Todos hemos aportado en la programación del código y en el escrito de la documentación; sobretodo gracias a la gran comunicación y numerosas videoconferencias realizadas.

Los integrantes del equipo somos:

- Sergio Beltrán Guerrero
- Jaume Guasch Llobera
- Martí Serratosa Sedó
- Sebastian Bampton Blasco

## Preparación

Para poder ejecutar el programa a la perfección necesitaremos la última versión de Python y instalar las librerías que están en el archivo [requirements](requirements.txt).
Si se quiere ejecutar el proyecto de rust, es necesario instalar rust y establecer el proyecto en modo nightly.

### Requisitos

Como he mencionado anteriormente, tenemos disponible un fichero con las librerías que necesitamos para poder ejecutar el programa. Para poder instalarlas es necesarioo tener pip y desde el bash ejecutar el siguiente comando `pip install -r requirements.txt`. Ademas de tener instaladas las librerías necesitamos el archivo sequences.csv

#### "sequences.csv"

Drapython ya te proporciona el fichero *sequences.csv* pero el usuario puede usar su propio fichero.

Para obtener los datos del virus debemos usar la página web de la *National Center for Biotechnology Information database* para descargar los datos ([NCBI database](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?VirusLineage_ss=Severeacuterespiratorysyndromecoronavirus2(SARS-CoV-2),taxid:2697049&SeqType_s=Nucleotide "National Center for Biotechnology Information database")). Su correcta descarga seguiría este procedimiento:

1. Seleccionar los **nucleotides** que queramos. A la izquierda podemos poner condiciones.
2. Pulsar a **Download**.
3. Seleccionar en el paso 1: *Current table view result* → **CSV format**.
4. En el paso 2: **Download Selected Records**.
5. En el paso 3 las columnas que **hay que seleccionar al ser necesarias** para el correcto funcionamiento son: **Accession, Length y Geo Location**. La otra información no es necesaria.

Una vez descargado el fichero, debemos añadirlo en el directorio data. 

## Ejecución

Para ejecutar el programa necesitamos ir al directorio de src/python y ejecutar el siguiente comando `python3 .\sarscovhierarchy.py`.

## Construcción

Las herramientas usada para crear el proyecto han sido tres:

- [Visual Studio Code](https://code.visualstudio.com/) - Editor de código
- [PyCharm](https://www.jetbrains.com/pycharm/ "PyCharm: Python tool") - Software para programar con Python.
- [Typora](https://typora.io/ "Typora: markdown editor") - Software para editar y leer ficheros markdown.
- [Github](https://github.com/ "Github: web de desarrollo colaborativo") - Web para compartir los ficheros del proyecto entre los miembros del equipo.

## Expresiones de Gratitud

Queriamos mostrar nuestra más sincera expresión de gratitud a la **Universitat de Lleida** por adaptar-se a la situación actual devida al CoVid-19 intentando no perjudicar a los estudiantes y, en concreto al professor **Jordi Planes** ([Github](https://github.com/jordiplanes)) por su esforzo para apoyar a los estudiantes.

---
<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Licencia de Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />Este obra está bajo una <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">licencia de Creative Commons Reconocimiento-NoComercial 4.0 Internacional</a>.

Drapythron Team © 2020

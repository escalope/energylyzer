Este es un proyecto para generar herramientas de análisis que ayuden a gestores a tratar los datos de sus consumos eléctricos. Su nombre viene de *Energy* y *Analyzer*. 

El consumo eléctrico, en un escenario donde hay que gestionar el consumo hora a hora, es inviable si nuestra única herramientas son las hojas de cálculo. A partir de cierto momento, es mejor usar programación y bases de datos. 

Una alternativa podría ser el uso de herramientas visuales, estilo Microsoft Office o Libre Office, pero para algunos cómputos se vuelve un reto definir lo que se quiere hacer. 

Por otro lado, el análisis que se suele aplicar a los resultados suele ser reusable y limitado a unas cuantas preguntas básicas. Son precisamente esas preguntas básicas las que se usan como argumento para proveer un conjunto de scrips que, dada una base de datos que tenga los contratos a mantener y los consumos pertinentes, implementan de forma simple los análisis deseados.

La salida de estos scrips son ficheros csv que se pueden importar en una suite ofimática e incorporarlos a otros datos de los que se disponga.

## Requisitos

Es importante avisar que lo que se ofrece aquí no son interfaces gráficas, sino programas ejecutables desde la línea de comandos. Si no se está familiarizado con el manejo de una consola de comandos, recomiendo, al menos, intentarlo. No es difícil. 

Todo el código que se ofrece está escrito en Python 2.7.6. No está escrito por un experto o adepto al Python, así que toda recomendación para mejora del código será bienrecibida. 

También se recomienda trabajar con una distribución de linux. Es software libre e instalar todo el software que se necesita para este fin es muy rápido. Como alternativa intermedia, se puede optar  por montar una máquina virtual y una distribución linux dentro.

En linux, instalar pyton es tan simple como escribir

	sudo apt-get install python 

## Manejo

La colección de scripts irá creciendo. De momento, incluye lo siguiente:

- crearBD.py -> genera en la carpeta "salida" ficheros csv con el nombre el CUPS que representan la curva de carga de ese CUPS entre las fechas que tú digas

- curvasPorCUPS.py -> genera en la carpeta "salida" ficheros csv con el nombre el CUPS que representan la curva de carga de ese CUPS entre las fechas que tú digas

Ejemplo de invocación:

	python bin/curvasPorCUPS.py consumosycontratos.db 2014-01-01 2014-12-31

Te saca toda las curvas horarias por CUPS de todo el año en la carpeta "salida". Hay un fichero csv por CUPS. En cada fichero, la primera fila contiene la dirección y la segunda y siguientes los consumos registrados.

- matrizCUPSHora.py -> genera un fichero excel que te dice, entre las fechas que se indiquen, cómo se acumula el consumo por cada hora del día y por cups

Ejemplo de invocación:

	python bin/matrizCUPSHora.py consumosycontratos.db 2014-01-01 2015-01-01 ejemploMatriz.csv

Te genera los consumos de todo el año acumulados por hora y cups en el fichero ejemploMatriz.csv
Es relevante para conocer cómo se distribuyen nuestros consumos por cada hora del día. 

## Instalación

Hay que copiar este proyecto a una carpeta. 

## Licencia

Este software se distribuye bajo licencia GPL v3, una copia de la cual se puede encontrar en esta distribución

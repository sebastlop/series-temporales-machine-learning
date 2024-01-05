# Python y el uso de librerías

Una de las características fundamentales que hacen de Python tan popular, es la facilidad con la que se puede intercambiar y utilizar código creado por otras personas. Los códigos suelen recolectarse en formas de módulos y librerías que se pueden importar de manera muy sencilla (módulo es un unico archivo _.py_ con funciones y variables globales, librería es una colección de módulos). Existen dos tipos de módulos y librerías de Python, las pertenecientes a la librería estandar (provista por las personas que mantienen el lenguaje y su entorno) y las de terceros. A su vez estas últimas pueden estar listadas en repositorios como PyPI (Python Package Index), GitHub, GitLab, etc.

![Python](./python.png "Imagen obtenida de xkcd https://xkcd.com/353/")

[Este comic de xkcd ](https://xkcd.com/353/) es bastante gracioso y explícito sobre las bondades de Python y el uso de módulos y librerías.

Para importar un módulo o librería basta con poner
```
import nombre_de_la_librería
```
También es posible importar módulos, clases o funciones de una librería de la siguiente manera:
```
from nombre_de_la_libreria import nombre_de_la_función_o_modulo
```

y listo, a partir de allí se puede trabajar con ella creando objetos si es que tiene clases definidas, o llamando a las funciones y métodos disponibles. Esto se realiza escribiendo ```nombre_de_la_libreria.nombre_del_metodo()```.

## La librería estándar

En este curso utilizaremos los módulos **os** (para manejar operaciones del sistema operativo y de archivos), **csv** (para leer archivos de datos estructurados por líneas) y **datetime** (para manejo de fechas y horas o timestamps) de la librería estandar. 
La lista completa de la documentación de la librería estandard se encuentra en https://docs.python.org/3/library/index.html mientras que las que utilizaremos en este curso se pueden hallar en:

* https://docs.python.org/3/library/os.html
* https://docs.python.org/3/library/csv.html
* https://docs.python.org/3/library/datetime.html

La utilización de estos módulos se demuestra en [este notebook](./2.4.1-librerias-estandar.ipynb).



## La librería NumPy


Esta librería implementa una gran cantidad de herramientas numéricas para el cálculo. La documentación oficial se encuentra en https://numpy.org/.

Los objetos fundamentales sobre el cual se monta NumPy son los arrays, que tienen tamaño fijo y son mutables. Todos los elementos de un array tienen que ser del mismo tipo, y tienen por lo tanto el mismo tamaño en memoria.

Los arrays tienen asociados: shape (tupla con la cantidad de elementos que hay en cada dimension) y size(cantidad total de elementos)

Además NumPy tiene gran cantidad de funciones matemáticas optimizadas para todo tipo de cálculo numérico.

En este notebook se muestran algunas funcionalidades de NumPy, pero es imprescindible una recorrida por la documentación

La utilización de esta librería se encuentra en [este notebook](./2.4.2-librerias-numpy.ipynb).

## La librería SciPy

Esta librería está basada en NumPy y contiene una gran cantidad de módulos para tareas numéricas y científicas, como cálculos numéricos, evaluación de funciones especiales, procesamiento de señales, ajustes de curvas, etc.

La web oficial es la siguiente https://scipy.org/ donde se recomienda leer la referencia de la API para conocer los módulos existentes: https://docs.scipy.org/doc/scipy/reference/index.html

## La librería MatplotLib

Esta librería es para realizar gráficos completamente personalizables a partir de datos. Esta librería es gigante con más de 70000 líneas de código.

En esta librería se tienen objetos Figure que son contenedores de otros objetos. La jerarquía es la siguiente:

**Figure**

--> Axes (Son cada uno de los graficos)

----> ticks, lines, labels, legends and text boxes, etc.

Ejemplos de la utilización de esta librería se encuentra en [este notebook](./2.4.3-librerias-matplotlib.ipynb).

## La librería pandas

Esta es una librería dedicada al análisis de datos, permite leer archivos de manera simple, acomodarlos en tablas y extraer todo tipo de información de ellas, al estar pensada para manejar grandes volúmenes de datos, tiene aspectos de manejo de memoria muy optimizados. Pandas está basada en NumPy y también posee integraciones con Matplotlib.

Los objetos fundamentales de pandas son las _series_ y los _dataframe_, que contienen los datos que pueden ser manipulados, filtrados y utilizados de innumerables maneras

La página oficial de pandas es la siguiente: https://pandas.pydata.org/ y una completa guía de usuario puede encontrarse en este link https://pandas.pydata.org/docs/user_guide/index.html#user-guide

Dado que la librería es vasta y su utilización dependerá de cada problema particular, se sugiere una lectura de la documentación. Un vistazo a la guía 10 minutos con pandas https://pandas.pydata.org/docs/user_guide/10min.html puede ser de mucha utilidad.

## La librería statsmodels

Esta librería será de gran utilidad para el empleo de algunos modelos regresivos. Es importante notar que al momento de escribir esta nota, la versión es 0.14, lo que quiere decir que es una versión beta y no se encuentra disponible aún una versión definitiva. No obstante su utilización es cada vez más profusa

El sitio oficial: https://www.statsmodels.org/stable/index.html

Para este curso se utilizará fundamentalmente el paquete de módulos de análsis de series temporales. Se recomienda ver la documentación https://www.statsmodels.org/stable/user-guide.html#time-series-analysis

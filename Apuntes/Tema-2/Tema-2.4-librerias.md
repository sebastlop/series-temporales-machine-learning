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

La utilización de estas librerías se demuestra en [este notebook](./2.4.1-librerias-estandar.ipynb).



## La librería NumPy


Esta librería implementa una gran cantidad de herramientas numéricas para el cálculo. La documentación oficial se encuentra en https://numpy.org/.

Los objetos fundamentales sobre el cual se monta NumPy son los arrays, que tienen tamaño fijo y son mutables. Todos los elementos de un array tienen que ser del mismo tipo, y tienen por lo tanto el mismo tamaño en memoria.

Los arrays tienen asociados: shape (tupla con la cantidad de elementos que hay en cada dimension) y size(cantidad total de elementos)

Además NumPy tiene gran cantidad de funciones matemáticas optimizadas para todo tipo de cálculo numérico.

En este notebook se muestran algunas funcionalidades de NumPy, pero es imprescindible una recorrida por la documentación

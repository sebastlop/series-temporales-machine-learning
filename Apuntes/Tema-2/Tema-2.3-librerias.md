# Python y el uso de librerías

Una de las características fundamentales que hacen de Python tan popular, es la facilidad con la que se puede intercambiar y utilizar código creado por otras personas. Los códigos suelen recolectarse en formas de librerías que se pueden importar de manera muy sencilla. Existen dos tipos de librerías de Python, las pertenecientes a la librería estandar (provista por las personas que mantienen el lenguaje y su entorno) y las librerías de terceros. A su vez estas últimas pueden estar listadas en repositorios como PyPI (Python Package Index), GitHub, GitLab, etc.

Para importar una librería basta con poner
```
import nombre_de_la_librería
```
También es posible importar módulos, clases o funciones de una librería de la siguiente manera:
```
from nombre_de_la_libreria import nombre_de_la_función
```

y listo, a partir de allí se puede trabajar con ella creando objetos si es que tiene clases definidas, o llamando a las funciones y métodos disponibles. Esto se realiza escribiendo ```nombre_de_la_libreria.nombre_del_metodo()```.

En este curso utilizaremos las librerías os (para manejar operaciones dde archivos), csv (para leer archivos de datos) y datetime (para manejo de fechas y horas o timestamps) de la librería estandar. 
La lista completa de la documentación de la librería estandard se encuentra en https://docs.python.org/3/library/index.html mientras que las relevantes se pueden hallar en

* https://docs.python.org/3/library/os.html
* https://docs.python.org/3/library/csv.html
* https://docs.python.org/3/library/datetime.html
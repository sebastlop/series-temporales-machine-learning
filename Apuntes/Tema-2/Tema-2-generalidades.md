# Rudimentos de Python

Python es un lenguaje de programación **interpretado**, es decir que no hay que compilar código. Por el contrario un intérprete es un programa compilado que lee las líneas de nuestro "programa",  al que llamaremos "**script**" y lo va ejecutando línea por línea.

Python es un lenguaje de programación de código abierto y de propósito general, es decir que se puede utilizar para casi todo.

## Cómo instalar Python
Existen numerosas distribuciones de Python. Para una guía para principiantes sobre como instalarlo referirse a https://wiki.python.org/moin/BeginnersGuide

Existen distribuciones curadas y mantenidas como Anaconda, que descarga el intérprete y algunas librerías populares https://www.anaconda.com

## Por qué vamos a utilizar Python
Si bien no es condición indispensable, en este curso se utilizará Python porque la escritura de código resulta sencilla y porque la mayoría de las cosas que vamos a utilizar ya están hechas por otra persona. El espíritu colaborativo y de código abierto prima en el ambiente Python.

Muchas de las herramientas que se utilizarán en este curso se encuentran en librerías, que son colecciones de scripts ya hechas por terceros y a disposición para su utilización. Los repositorios estándares de librerías de Python son PyPI (Python Package Index) y algunas mantenidas por terceros como Anaconda.

## El intérprete en la lína de comandos

Para saber la versión de Python instalada en nuestra computadora podemos escribir en una terminal (Terminal de linux, Powershell de windows) con python debidamente instalado
```
$ python3 --version

Python 3.10.12
```
Para ingresar a la línea de comandos del intérprete:
```
$ python3
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
y el prompt cambia por ">>>", que es el prompt del intérprete de Python. 

Para obtener ayuda, podemos utilizar la ayuda online en la página oficial
https://www.python.org o utilizar la miríada de foros y páginas webs con contenido dedicado a python. También se puede utilizar la línea de comando para acceder a la ayuda escribiendo:

```
>>> help()
Welcome to Python 3.10's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.10/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> 

```
y allí dentro escribir lo que uno desee consultar. Para salir del prompt de ayuda basta con pulsar "enter" sin ningún texto, y para salir del intérprete se puede escribir ```>>> exit()``` o simplemente presionar **Ctrl+d**

## Ejecutando un script

Para ejecutar un script guardado en un archivo, por ejemplo: _script.py_, basta con poner en la línea de comandos de la terminal:
```
$ python3 script.py
```

## Utilizando IPython y el Notebook Jupyter
IPython es una interfaz con celdas ejecutables (como lo son algunos lenguajes como Mathematica, Maple, etc), que se pueden ir ejecutando una a una, al contrario de un script de python donde se ejecuta por completo y no se puede ir observando e interactuando con los estados intermedios. El entorno usual de IPython actual es **Jupyter** que utiliza notebooks con kernels (interpretes) de python.

Las notebooks de Jupyter se pueden ejecutar en diversos programas host, usualmente el navegador web (Mozilla, Chrome, etc). También existen plugins para Visual Studio Code (un entorno de desarrollo de Microsoft muy ameno) o JupiterLabs, etc. 

En este curso se alentará la utilización de Notebooks de Python para los ejemplos sencillos, más no así para los trabajos que impliquen mucho procesamiento y cálculo, por dos motivos: (i) la utilización de memoria y (ii) los errores que suelen cometerse al correr celdas de manera desordenadas.

Una vez instalada, para lanzar una Jupyter notebook en cuanlquier entorno linux basta poner:
```
$ jupyter notebook
```

Si se utiliza Anaconda, se crean accesos directos que suelen hacer simple la tarea de ejecución.
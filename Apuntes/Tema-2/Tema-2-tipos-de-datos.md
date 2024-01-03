# Tipos de Datos en Python

Dado que este es un curso _hands on_, para desarrollar este tema, es preciso seguir este [link](./2-tipos-de-datos.ipynb). 

Antes de comenzar a describir los tipos de datos que puede manejar Python, es importante destacar que todo, **ABSOLUTAMENTE TODO** en Python es un objeto. Luego veremos en detalle que son los objetos, pero lo importante en este punto es comprender que python no maneja variables como los lenguajes compilados que conocemos usualmente.

Para saber qué tipo de ojeto es alguno que ya está instanciado, basta con ejecutar ```type()``` con el nombre del objeto en los paréntesis.

Dicho esto, que no tendremos variables, sino objetos, veamos los tipos de objetos de Python más utilizados (Son muchos y solamente citaremos algunos). La precisión y el tipo de representación utilizada depende del sistema operativo 

* Tipos escalares: 
    *   Booleanos o Lógicos: que pueden valer True o False.
    *   Numéricos: **int** (enteros), **float** (números decimales) y **complex** (números complejos)
* Secuencias:
    *   List: Colecciones de objetos mutables indexadas.
    *   Tuple: Colecciones de objetos inmutables indexadas
    *   range: Secuencia inmutable de números
    *   str: Es una secuencia de caracteres
* Mapeos:
    * Diccionarios: Mapeo de conjuntos Hasheables. En Python se puede generar un Hash a partir de números, strings y tuplas.


Toda la información se encuentra en la documentación oficial que está en el siguiente link: https://docs.python.org/3/library/stdtypes.html

## Cometarios sobre objetos
Un objeto tiene dos características fundamentales: Poseen atributos y métodos. Los tributos tienen la forma de variables internas del objeto, mientras que los métodos son acciones que pueden realizar. 

En python el valor de un atributo de un objeto se puede obtener utilizando: _nombre.atributo_, y los métodos se pueden ejecutar de la siguiente manera: _nombre.metodo()_

Por ejemplo, una cadena de caracteres ```a = 'mi mamá me mima'``` puede ejecutar el método split() de la siguiente manera
```
>>> a = 'mi mama me mima'
>>> a.split()
['mi', 'mama', 'me', 'mima']
```
donde split() es una acción que devuelve una lista de 4 strings utilizando el espacio como separador.


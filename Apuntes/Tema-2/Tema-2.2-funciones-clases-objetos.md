# Funciones, Clases y Objetos

Los procedimientos tienen la funcionalidad de acortar y estructurar código. Normalmente en los paradigmas de programación procedural y orientada a objetos, las tareas repetitivas pueden escribirse una sola vez y ser llamadas cada vez que se necesiten, esto permite estructurar el código y reducirlo notablemente. Por otra parte los objetos sirven para mantener en memoria bloques autónomos con comportamiento propio, que pueden realizar tareas y almacenar valores.

Existen una serie de fuciones intrínsecas de Python que están listadas en la documentación https://docs.python.org/3/library/functions.html

## Funciones

Las funciones son objetos fundamentales de la programación en Python, estas se definen de la siguiente manera:
```
def nombre_de_la_func ( [argumentos] ):
    ...
    bloque de ejecucion
    ...

    [return objetos_de_retorno]
```

La palabra clave ```def``` indica que se define una función. Ésta debe tener un nombre y una serie de argumentos. Luego tiene un valor de retorno (puede ser cualquier tipo y número de objetos). Tanto los argumentos como el return son opcionales.

La función más simple es aquella que no tiene ni argumentos ni return definido, por ejemplo:
```
def imprime_algo():
    print('algo')
```
Cuando se llama a esta función, simplemente imprime "algo". Se la llama desde la línea de comandos simplemente como ```imprime_algo()```

Los argumentos pueden ser de 3 tipos diferentes:

*   argumentos posicionales: importa el orden en que son definidos y luego provistos
*   argumentos por palabras claves: no importa el orden, y su número puede ser desconocido. Normalmente se los denomina como _*args_ y _**kwargs_

[En este notebook hay algunos ejemplos](./2.2-funciones-clases-objetos.ipynb)

## Clases y Objetos

Las clases y objetos son el alma de la programación en Python, dado que todo es un objeto en Python. Naturalmente el paradigma de programación que se sigue en Python suele ser el paradigma orientado a objetos (POO) aunque no es el único posible, dada la flexibilidad que presenta este lenguaje.

En una burda definición una Clase es el "molde" para la creación de objetos, es decir la plantilla con que se crearán los objetos. La clase tiene asociadas cierta cantidad de variables, denominadas atributos, y funciones que realiza. Éstas reciben el nombre de métodos. Cuando se crea un objeto a partir de una clase, se dice que se crea una instancia de la clase.

Las clases tienen conceptos de herencias y alcances de espacios de nombre. Para comprender estos temas un poco más avanzados  es importante leer la documentación oficial sobre clases https://docs.python.org/3/tutorial/classes.html

Finalmente, una clase se define de la siguiente manera:
```
class nombre (Clase madre si existe):
    definiciones de atributos y métodos
```

Para ver ejemplos y ejecutarlos ir a [este notebook](./2.2-funciones-clases-objetos.ipynb).



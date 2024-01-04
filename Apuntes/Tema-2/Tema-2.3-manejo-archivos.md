# Manejo de archivos

Es importante saber cómo leer y escribir archivos, para ello se utiliza la función incluida ```open(args)``` y cuya documentación se encuentra en https://docs.python.org/3/library/functions.html?highlight=open#open

Siempre los objetos de archivo deben cerrarse con close()

Es usual utilizar un _handler_ por medio de la construcción _with_ y _as_, para evitar tener que cerrar el objeto de archivo y tambien evitar errores de control de finalización (EOF de end of file) detengan la ejecución del script. La construcción típica es la siguiente:

```
with open(file, mode = str, ...) as file_object:
    # do something with file_object
    content = file_object.read()
```
los mode disponibles son:


|Character|Meaning|
|---|---|
|'r'  |open for reading (default)|
|'w'|open for writing, truncating the file first|
|'x'|open for exclusive creation, failing if the file already exists|
|'a'|open for writing, appending to the end of file if it exists|
|'b'|binary mode|
|'t'|text mode (default)|
|'+'|open for updating (reading and writing)|

Los métodos y atributos de los objetos de archivos se encuentran aquí: https://docs.python.org/3/tutorial/inputoutput.html#tut-files

La lectura y escritura de archivos se realizará de multiples maneras, incluso utilizando librerías específicas y de manera natural a lo largo del curso, por lo que no se adjunta ninguna Notebook de Jupyter particular para este tema.
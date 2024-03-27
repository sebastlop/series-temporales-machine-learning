# Ejercicio propuesto (repaso de Python)

Realizar un script que realice las siguientes cosas:

1. Crear una clase que tenga los siguiente atributos:
    
    1.1. Un array de floats para el tiempo

    1.2. Un array de floats para cada columna

2. La clase anterior debe tener los siguientes métodos


    2.1 un método que abra un archivo de la carpeta Data/acelerometro y pueda leerlo con un formato numérico adecuado

    2.2 El método \_\_init\_\_ () que lea el archivo usando otro método específico y guarde los atributos previos descritos.

    2.3 Un método que devuelva un objeto de interpolación de la columna seleccionada

    2.4 Un método que realice el ajuste de la funcion $y = a \sin{(\omega t+\phi)}+b$, devuelva los parámetros $a,b,\omega,\phi$

3. Crear una instancia de la clase para cada archivo de la carpeta, graficar cada una conjuntamente con el fiteo y guardarlo en un archivo de imagen .png

4. Si el fiteo tiene sentido, encontrar el período correspondiente $\tau = 2\pi/\omega $


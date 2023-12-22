
# 1. Definiciones

Definiciones. Tipos. inspección ocular.
---

Una serie temporal (ST) es un conjunto de datos ordenados en el tiempo. Ejemplos de series temporales son mediciones de variables ambientales, señales de ultrasonido, sensores de movimiento durante un período, secuencias de imágenes ordenadas en el tiempo, etc.

Una ST puede ser univariada o multivariada. Por ejemplo, si tenemos una serie de medidas de temperatura a lo largo del tiempo, solo tenemos una variable, mientras que para una secuencia de imágenes el valor de cada pixel varía en el tiempo. Cada uno de los pixeles corresponde a una variable. 

Para un caso general de $m$ variables $\pmb{X} = (X_1, X_2, ..., X_m)$, la ST que consiste en $N$ datos temporales se puede representar simplemente como $\left[\pmb{X}(t_1), \pmb{X}(t_2),..., \pmb{X}(t_N)\right]$.

Además, es importante notar que los valores que pueden tomar las diferentes variables $X_i$ pueden ser discretos (como en el caso de los valores de intensidad de los píxeles), o continuos como en el caso de la temperatura. El proceso de obtención de las variables (proceso de medición) influye en estas características. Dado que se trabaja con datos digitales, a la postre todas las variables serán discretas.
 
## Tipos de series temporales

- __Continua__: está valuada para todos los instantes 

![ST continua](./pulso_sonido.png "señal continua típica")
- __Discreta__: está valuada en algunos instantes
![ST discreta](./precio_trigo.png "señal discreta típica (valores ficticios)")
- __Repetitiva__: repite un patrón a lo largo de toda la serie
- __Periódica__: caso particular de serie repetitiva donde el patrón se repite en espacios de tiempo uniformes. Existe un período constante
- __Determinista__: puede ser expresada de manera unívoca por una expresión analítica
- __No determinista__: no puede ser expresada analíticamente. Esto puede darse por dos motivos fundamentales:
    
    - No se tiene acceso a toda la información del problema
    - La naturaleza del proceso tiene componentes aleatorias

## Procesos estocásticos

En un proceso estocástico $X$ corresponde a un conjunto de variables aleatorias

## La adquisición de datos

Cuando las series temporales se obtienen a partir de mediciones de variables analógicas continuas, se realizan una serie de procesos relacionados con la transducción, acondicionamientos de señales, entre otras etapas. Luego las señales acondicionadas deben ser muestreadas y cuantificadas.

Las etapas descriptas no se tratarán aquí, ya que son un objeto de estudio en sí mismo, sólo diremos que:

> * El muestreo es la realización periódica con que se toma una medición.
> * La cuantificación es la medición de la amplitud de la señal de entrada. 

Así, la frecuencia de muestreo nos dará los intervalos temporales que habrán entre mediciones, mientras que la cuantificación nos proporcionará la magnitud medida.

* Teorema de Nyquist

* Aliasing
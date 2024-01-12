# Análisis Estadístico de series temporales

En términos generales, las series temporales (ST) varían en el tiempo y el análisis de esta variación es lo que se realiza en los análisis clásicos. Normalmente, aunque esto no es la regla general, se intenta descomponer a las variaciones que sigue la ST en los siguientes términos:
1. Tendencia: se suele representar mediante una función monótona que sigue la  media de la serie.
2. Fluctuaciones estacionales: cambios periódicos que sufre la ST. 
3. Fluctuaciones cíclicas: cambios cíclicos que sufre la ST sin un período exacto.
3. Fluctuaciones irregulares: este tipo de fluctuaciones puede ser aleatorio, sin ningun tipo de relación con características evidentes, como así también puede ser un proceso autoregresivo.

Dentro de las caracterizaciones que se pueden realizar de las ST, la primera y más importante es poder establecer si una serie es estacionaria. Dependiendo del autor la definición varía. En este punto seguiremos la definición porporcionada en la referencia [2] ya que resulta concisa. Una serie se dice estacionaria si la distribución probabilística de los datos permanece constante en el tiempo. 

> **Series estacionarias:** Aquellas que mantienen la distribución probabilística de los datos constantes en el tiempo. La ***media*** y la ***varianza*** son constantes en la serie. 

Una manera de observar la estacionariedad de una serie temporal es analizar la distribución de datos en diferentes ventanas de tiempo. 

[En este notebook se analiza este tema](./Tema-3.1-plots-estacionariedad.ipynb)

# Análisis de tendencias

<details>
  <summary>Asectos generales</summary>

## Aspectos generales

El análisis de tendencias se debe realizar sobre cada una de las componentes de las ST cuando son multivariadas. Si bien no existe una receta para analizar tendencias, existen ciertas técnicas estandarizadas, como el análisis de cambios (derivadas), el análisis a partir del suavizado de curvas utilizando diferentes técnicas, la transformación de variables, el fiteo de curvas, etc.

</details>

<details>
    <summary> Análisis de cambios locales (derivadas) </summary>

## Análisis de cambios locales (derivadas) 

La derivada tiempo a tiempo de una ST, se puede realizar numéricamente de muchas maneras y considerando diferente cantidad de puntos de la serie.

* Diferencia finita hacia adelante:
    $$X'(t_i) = \frac{X(t_{i+1})-X(t_i)}{t_{i+1}-t_i}$$
* Diferencia finita hacia atras:
    $$X'(t_i) = \frac{X(t_{i})-X(t_{i-1})}{t_{i}-t_{i-1}}$$
* Diferencia finita en el punto medio:
    $$X'(t_i) = \frac{X(t_{i+1})-X(t_{i-1})}{t_{i+1}-t_{i-1}}$$

Cualquiera de los tres casos previos es útil para el análisis de tendencias. Una serie con tendencia lineal tendrá por resultado una distribución derivada aproximadamente constante, mientras que si la derivada posee cambios y tendencia a su vez en el tiempo, tal tendencia puede ser de otro tipo funcional (logarítmica, exponencial, polinómica, etc). 
</details>

<details>
    <summary> Suavizado: Media Móvil (MA) </summary>

## Suavizado: Media Móvil (MA)

La media móvil, cuando es simétrica permite eliminar oscilaciones alrededor de la media. Si bien existen tratados sumamente exhaustivos, en este curso veremos la más simple de todas. La media móvil es una transformación que lleva nuestra distribución $X(t)$ en $Y(t)$. La expresión general de este tipo de transformaciones que llamaremos $Sm$ (por smooth):
$$
Sm[X(t_i)] = \sum_{r=-q}^{s}a_r\ X(t_{i+r})
$$
Si se toma $q=s$ y todos los pesos $a_r=\frac{1}{(2q+1)}$ tenemos la expresión típica de la media móvil en ventanas de ancho $2q+1$. La inspección de la media móvil sobre anchos diferentes puede servir para descartar oscilaciones y su ajuste para extraer la tendencia global, o por tramos. Es importante notar que este tipo de suavizados produce una nueva serie con $N-(2q+1)$ puntos.
</details>
## Suavizado exponencial (ETS)

Similar a la media móvil, se puede realizar un suavizado, considerando la historia de la serie hacia atrás, de modo tal que los puntos más recientes son más importantes que los previos. El decaimiento de la importancia es de forma exponencial.
$$
Sm[X(t_i)] = \sum_{j=0}^{\infty}\alpha(1-\alpha)^j X(t_{i-j}),
$$
donde $\alpha$ es una constante que satisface: $0<\alpha<1$ y recibe el nombre de constante de suavizado (smooth constant).

## Ajustes de funciones

Si se tiene una curva suave a partir de la serie original mediante algún procedimiento como la media móvil, se puede realizar un ajuste de diferentes familias funcionales $f_{\vec{\alpha}}(t)$, con $\vec{\alpha}$ un conjunto de parámetros. Supongamos que $Y$ es la ST que pretendemos ajustar, donde $\hat{y}_i$ son los valores de la serie correspondientes a $Y(t_i)$. Diremos que el ajuste corresponfiente $y_i = f_{\vec{\alpha}}(t_i)$ es el mejor ajuste si el conjunto de parámetros $\vec{\alpha}$ minimiza alguna función de error. Algunas de las funciones de error más utilizadas son:

* Error cuadrático medio (___MSE___):
        $$ MSE = \frac{1}{N}\sum_{i=1}^{N}{(\hat{y}_i-y_i)}^2$$
* Error del valor absoluto medio (___MAE___):
        $$ MAE = \frac{1}{N}\sum_{i=1}^{N}{\vert\hat{y}_i-y_i\vert}^2$$

Luego existen otras funciones que sirven para estimar dentro de predicciones el error, para ver alguna de ellas, ver el capítulo 4 de la referencia [2].

## Predicciones detendencia

Utilizando las herramientas previas, se puede cuantificar la tendencia global de una ST realizando ajustes de las diferentes curvas obtenidas. Dependiendo de los análisis que se realicen las 

</details>


## _Bibliografía_
[1] Chatfield, Chris. The Analysis of Time Series: An Introduction, Sixth Edition. Reino Unido: CRC Press, 2003.

[2] Joseph, Manu. Modern Time Series Forecasting with Python: Explore Industry-ready Time Series Forecasting Using Modern Machine Learning and Deep Learning. Reino Unido: Packt Publishing, 2022.
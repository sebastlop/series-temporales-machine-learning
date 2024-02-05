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

El análisis de tendencias se debe realizar sobre cada una de las componentes de las ST cuando son multivariadas. Si bien no existe una receta para analizar tendencias, existen ciertas técnicas estandarizadas, como el análisis de cambios (derivadas), el análisis a partir del suavizado de curvas utilizando diferentes técnicas, la transformación de variables, el fiteo de curvas, etc. A continuación se presentan algunas de ellas:

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

<details>
    <summary> Suavizado exponencial (ETS) </summary>

## Suavizado exponencial (ETS)

Similar a la media móvil, se puede realizar un suavizado, considerando la historia de la serie hacia atrás, de modo tal que los puntos más recientes son más importantes que los previos. El decaimiento de la importancia es de forma exponencial.
$$
Sm[X(t_i)] = \sum_{j=0}^{\infty}\alpha(1-\alpha)^j X(t_{i-j}),
$$
donde $\alpha$ es una constante que satisface: $0<\alpha<1$ y recibe el nombre de constante de suavizado (smooth constant).

Si se considera sólo el primer término de la expansión, este método se denomina _Suavizado exponencial simple_ (**SES**). Si se consideran los dos primeros términos de la serie: _Suavizado exonencial doble_ (**DES**).

</details>

<details>
    <summary> Ajustes de funciones </summary>

## Ajustes de funciones

Si se tiene una curva suave a partir de la serie original mediante algún procedimiento como la media móvil, se puede realizar un ajuste de diferentes familias funcionales $f_{\vec{\alpha}}(t)$, con $\vec{\alpha}$ un conjunto de parámetros. Supongamos que $Y$ es la ST que pretendemos ajustar, donde $\hat{y}_i$ son los valores de la serie correspondientes a $Y(t_i)$. Diremos que el ajuste corresponfiente $y_i = f_{\vec{\alpha}}(t_i)$ es el mejor ajuste si el conjunto de parámetros $\vec{\alpha}$ minimiza alguna función de error. Algunas de las funciones de error más utilizadas son:

* Error cuadrático medio (___MSE___):
        $$ MSE = \frac{1}{N}\sum_{i=1}^{N}{(\hat{y}_i-y_i)}^2$$
* Error del valor absoluto medio (___MAE___):
        $$ MAE = \frac{1}{N}\sum_{i=1}^{N}{\vert\hat{y}_i-y_i\vert}$$

Luego existen otras funciones que sirven para estimar dentro de predicciones el error, para ver alguna de ellas, ver el capítulo 4 de la referencia [2].

</details>

<details>
    <summary> Predicciones a partir de tendencias globales </summary>

## Predicciones a partir de tendencias globales

Utilizando las herramientas previas, se puede cuantificar la tendencia global de una ST realizando ajustes de las diferentes curvas obtenidas. Dependiendo de los análisis que se realicen, los modelos serán diferentes y a partir del conocimiento del problema en sí mismo y la experiencia del analista se podrán aplicar con mayor o menor grado de validez.

La técnica más burda corresponde a la repetición del último valor. Normalmente es llamado modelo **Naïve**. Este modelo puede utilizarse con el valor de la última media móvil, repitiendo este valor. Claramente este modelo tiene memoria de más valores del pasado, denominaremos a este modelo **NaïveMA**.


Una de las técnicas usuales de predicción suele seguir los siguientes pasos:
1. Realizar un suavizado mediante _MA_ para una ventana temporal determinada
2. Analizar la variación de la pendiente mediante derivadas
3. Ajustar la tendencia mediante alguna función analítica. 
4. Utilizar esta función para predecir el punto siguiente en el tiempo

</details>

<details>
    <summary> Predicciones a partir de tendencias locales </summary>

## Predicciones a partir de tendencias locales
Lo que se realiza usualmente es observar tendencias en ventanas de tiempo, no globales de toda la serie, para esto los análisis previos se realizan  sobre ventanas temporales y se guardan de manera numérica (no analítica) en porciones donde la media permanece constante.
</details>


[En este notebook analizamos tendencias](./Tema-3.2-analisis-tendencias.ipynb)

# Estacionalidad

Una serie puede tener estacionalidad, el análisis de la estacionalidad se puede observar a partir del gráfico de la serie temporal, y también del conocimiento previo de la medición.
<details>
    <summary>Gráficos estacionales</summary>

## Gráficos estacionales

Cuando se conoce el intervalo de estacionalidad, la tendencia se puede obtener haciendo un suavizado con ventanas del tamaño igual al periódo de estacionalidad. Luego se utilizan los gráficos estacionales, que consisten en graficar cada período superpuesto.

Una vez caracterizada la estacionalidad, se puede realizar un análisis del comportamiento de la distribución para saber si la estacionalidad se comporta de manera aditiva, o multiplicativa respecto de la tendencia. Si se observa que la desviación estándar no muestra una tendencia clara de crecimiento/decrecimiento en el tiempo se puede pensar que la serie se puede escribir como:
$$X(t) = m_t + S_t + \varepsilon_t,$$
donde $m_t$ será la tendencia, $S_t$ será la oscilación estacional y $\varepsilon_t$ un ruido estocástico.

Por el contrario, si existe una tendencia marcada de la desviación estándar, se puede escribir de manera multiplicativa como 
$$X(t) = m_t S_t + \varepsilon_t, $$ 
o también 
$$X(t) = m_t  S_t  \varepsilon_t.$$ 
Determinar el tipo de descomposición es una tarea ardua y artesanal.
</details>


<details>
    <summary>Correlaciones y autocorrelación</summary>

## Correlación y Autocorrelación

La correlación entre dos pares de variables $X$ e $Y$ de la misma longitud ($N$) se define como

$$
r_{xy} = \frac{\sum_{i=1}^N (x_i - \bar{x})(y_i-\bar{y})}{\sigma_x \sigma_y}
$$

Donde $\sigma_{x,y}$ es la desviación estándar de cada una de la series. Cuando la correlación es mayor, significa que las series son más similares. Si en la expresión anterior miramos cómo se correlaciona una serie consigo misma desplazada, podemos encontrar estacionalidades de la siguiente manera: tomamos la serie $X(t_1), X(t_2),..., X(t_{N-1})$ y la correlacionamos con la serie desfasada en uno $X(t_2), X(t_3),..., X(t_{N})$, la ecuación anterior se puede escribir
$$
r_{1} = \frac{\sum_{i=1}^{N-1} (x_i - \bar{x}_1)(x_{i+1}-\bar{x}_2)}{\sigma_x \sigma_{x_{i+1}}},
$$
donde 
$$
\bar{x}_1 = \frac{\sum_{i=1}^{N-1}x_i}{N-1}\ \ y\ \ \bar{x}_2 = \frac{\sum_{i=2}^{N-1}x_i}{N-1}
$$

</details>


[En este notebook analizamos la estacionalidad](./Tema-3.3-analisis-estacionalidad.ipynb)

# Filtrado de señales

El filtrado es un conjunto de técnicas que sirven para resaltar o esconder ciertas características de las series, como la detección de saltos, picos, o estructuras particulares.

Existen muchos tipos de transformaciones que suelen aplicarse, siendo el análisis de señales mediante filtros un curso en sí mismo. Dado que no es el objeto de este curso ahondar en estas técnicas, describiremos aquí algunos basados en una operación matemática denominada __*convolución*__. La convolución entre dos funciones continuas $f$ y $g$ de una sola variable se escribe como
$$
(f \star g)(\tau) = \int_{-\infty}^{\infty}f(t)g(t-\tau) dt,
$$
que puede interpretarse como la aplicación de una plantilla $g(t)$ sobre una función $f(t)$ desplazada en una cantidad $\tau$. Se puede observar cierta analogía con las correlaciones y la media móvil.

Si por el contrario, se tienen dos series discretas $X(t_i)$ y $Y(t_i)$, la convolución discreta se escribe como

$$
(X \star Y)(\tau_j) = \sum_{i = 1}^{N_X}X(t_i)Y(t_i-\tau_j),
$$
donde $N_X$ es el número de muestras de la serie X, y el resultado $(X \star Y)(\tau_j)$ tendrá $N_X - N_Y$ puntos. Es usual encontrarse un aumentado de puntos para obtener la misma cantidad de puntos que la serie inicial. Esto se suele hacer agregando $N_Y/2$ valores al comienzo de $X$ y $N_Y/2$ ó $N_Y/2+1$ al final dependiendo de si el número de puntos $N_Y$ es par o impar respectivamente. Los valores que se agregan pueden ser constantes, o correspondientes a alguna extrapolación, o los valores del final de la serie X, para hacer la convolución circular.


<details>
    <summary>Casos de interés</summary>

## Casos de interés

### Covarianza
    
La covarianza entre dos series temporales de igual longitud se escribe: 
$$
    Cov(X,Y) = \frac{1}{N}\sum_{i=1}^N{(x_i-\bar{x})(y_i-\bar{y})}
$$ 
Si hacemos las transformaciones $\tilde{X} = X-\bar{x}$ y $\tilde{Y} =Y-\bar{y}$ se observa simplemente que la covarianza se puede calcular  
$$
    Cov(X,Y) = \frac{(\tilde{Y} \star \tilde{X})}{N_X}(\tau_0)
$$

### Correlación
De manera análoga a la covarianza, la correlación se puede calcular de manera inmediata realizando las siguientes transformaciones:
$$
    \tilde{X} = \frac{X-\bar{x}}{\sigma_x} , \ \  \ \tilde{Y} =\frac{Y-\bar{y}}{\sigma_y}
$$
La correlación se reduce a la convolución entre las nuevas series $(\tilde{Y} \star \tilde{X})(\tau_0)$

### Derivada centrada

### Suavizado Gaussiano

### Derivada Gaussiana


</details>

## _Bibliografía_
[1] Chatfield, Chris. The Analysis of Time Series: An Introduction, Sixth Edition. Reino Unido: CRC Press, 2003.

[2] Joseph, Manu. Modern Time Series Forecasting with Python: Explore Industry-ready Time Series Forecasting Using Modern Machine Learning and Deep Learning. Reino Unido: Packt Publishing, 2022.

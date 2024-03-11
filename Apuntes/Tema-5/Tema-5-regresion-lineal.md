# Problemas simples de aprendizaje supervisado

De todos los problemas de aprendizaje automatizado, tal vez los más simples son los correspondientes a la regresión lineal y la regresión logística (que es un problema de clasificación). Utilizaremos estos problemas para comprender aspectos básicos relacionados al aprendizaje automatizado.

## Regresión lineal

Si se tiene un conjunto de datos {X, Y}, uno puede pensar si existe alguna relación entre ellos, normalmente lo primero que suele hacerse es ver si cumplen una relación lineal entre sí, es decir que dado un $x$ se cumple dentro de un error aceptable que $y = a x + b$ para todo el conjunto de datos.

El primer algoritmo de aprendizaje automatizado que veremos en detalle es la regresión lineal. Este problema consiste en conseguir los mejores parámetros $a$ y $b$ que minimizen un criterio de error para todo el conjunto de datos.

Los criterios a tener en cuenta pueden ser varios, dependiendo del problema, pero en términos generales se puede definir una función denominada de costo o pérdida $\mathcal{L}$ , que pueda ser extremada, cuando el error sea mínimo. Regresando al problema planteado, vamos a definir como el modelo que representa a nuestro conjunto de datos una función $f$, tal que 

$$ 
\begin{align}
    y &= f(x)=ax+b.  
\end{align}
$$ 
A la variable independiente $x$ se la suele denominar como _feature_ y nosotros llamaremos simplemente _variable_. Así, se tendrán a disposición un conjunto de pares de valores $\{x_i\}$ y $\{\hat{y}_i\}$. A los valores medidos o sabidos $\{\hat{y}_i\}$ se los suele denominar valores verdaderos o _ground truth values_.

La función $\mathcal{L}$ será una función explícita de $y$ y $\hat{y}$, es decir $\mathcal{L} = \mathcal{L}(y, \hat{y})$ y mediante la definición de la Ecuación (1) es función de los parámetros $a$ y $b$.

Para un problema de regresión típico, donde la variable $x \in R$, es decir es contínua, se suele utilizar como función de costo al error cuadrático medio (MSE), o al error absoluto medio (MAE), entre otros. Utilizando el MSE, la función de costo se puede escribir:

$$
\begin{align}
\mathcal{L} &= \frac{1}{N}\sum_{i=1}^{N}{(\hat{y}_i - y_i)^2},
\end{align}
$$
donde $N$ es el conjunto de datos, y $y_i$ es el valor que arroja el modelo para el valor de entrada $x_i$. Ahora bien, cómo se puede utilizar esta función para determinar los valores de los parámetros $a$ y $b$?. Eso se puede hacer de manera simple. Minimizando $\mathcal{L}$ respecto de los parámetros precisamente. Es decir, encontrando los valores tal que

$$
\begin{align}
\frac{\partial\mathcal{L}}{\partial a} &= 0, \\
\frac{\partial\mathcal{L}}{\partial b} &= 0.
\end{align}
$$

Utilizando la regla de la cadena a partir de la Ecuación (2). se obtienen las condiciones para la función de costo:

$$
\begin{align}
\frac{\partial\mathcal{L}}{\partial a} &= -\frac{2}{N}\sum_{i=1}^{N}{(\hat{y}_i - (a x_i + b))}x_i = 0, \\
\frac{\partial\mathcal{L}}{\partial b} &= -\frac{2}{N}\sum_{i=1}^{N}{(\hat{y}_i - (a x_i + b))}= 0.
\end{align}
$$

Con lo que se encuentran los parámetros óptimos. En este punto es importante notar que lamentablemente el proceso de minimización se debe realizar numéricamente porque no se pueden factorizar los parámetros de la suma. Por ello se utilizan diferentes métodos como el decenso por gradientes (GD) y todas sus variantes como el descenso por el gradiente estocástico (SGD) entre otros. 

## Descenso por gradiente y tasa de aprendizaje

El algoritmo de descenso por gradiente propone descender hacia el mínimo de la función de pérdida dando pasos, en la dirección opuesta al gradiente (ya que el gradiente señala la dirección de mayor crecimiento de la función objetivo)


Supongamos que tenemos una serie temporal (ST) $X[t_i]$, y queremos observar si tiene una tendencia lineal, para ello se puede 
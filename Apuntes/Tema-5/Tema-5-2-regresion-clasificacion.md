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
donde $N$ es el conjunto de datos, y $y_i$ es el valor que arroja el modelo para el valor de entrada $x_i$. Ahora bien, cómo se puede utilizar esta función para determinar los valores óptimos de los parámetros $a$ y $b$?. Eso se puede hacer de manera simple. Minimizando $\mathcal{L}$ respecto de los parámetros precisamente. Es decir, encontrando los valores tal que

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

El algoritmo de descenso por gradiente propone descender hacia el mínimo de la función de pérdida dando pasos, en la dirección opuesta al gradiente (ya que el gradiente señala la dirección de mayor crecimiento de la función objetivo). Supongamos que partimos con valores al azar de los parámetros. El algoritmo para encontrar un mínimo (relativo) consiste en realizar hasta alcanzar un criterio de convergencia la siguiente transformación de manera iterativa:

$$
\begin{align}
a' &\rightarrow  a- \alpha \frac{\partial\mathcal{L}}{\partial a}\\
b' &\rightarrow  b- \alpha \frac{\partial\mathcal{L}}{\partial b},
\end{align}
$$
donde $\alpha$ es un parámetro denominado tasa de aprendizaje (learning rate o lr) y es positivo. Este algoritmo desciende suavemente por la hipersuperficie de los parámetros hasta encontrar un mínimo.

### Efectos de la tasa de aprendizaje

Cuando la tasa de aprendizaje es muy pequeña, el descenso hacia un mínimo puede llevar muchas iteraciones sobre el conjunto de datos. Por el contrario cuando su valor es demasiado grande, el algoritmo puede no converger y realizar saltos sin una regla clara, incluso llevando a la evaluación de valores infinitos para los parámetros.

Estos aspectos se pueden observar en [esta notebook](./Tema-5-machine-learning-libs-fw.ipynb)

## Regresión Logística y clasificación

La regresión logística se usa desde los albores del siglo XX en el campo de la biología, y ha resultado útil para muchos problemas de diversas áreas. En general se utiliza para clasificar datos, en este caso particular veremos clasificación binaria, es decir dos clases de datos. Las variables que pueden ser clasificados en una cantidad discreta de grupos se denominan categóricas. Por ejemplo separar fotos de gatos y perros, o determinar si un email es spam o no, etc. Lo importante para que este tipo de regresión funcione, es que el dominio de las variables que se clasifican posea una frontera entre una y otra clase. 

> Para clarificar pongamos un ejemplo simple. Supongamos que queremos clasificar fotografías como oscuras y claras, para ello utilizamos alguna digitalización en un bit (blanco y negro), sobre la cual tomamos el promedio sobre todos los valores de los pixeles, si el promedio es mayor o igual que 0.5, la imagen es clara, si es menor a 0.5 es oscura. 

En este ejemplo la variable $x$ (feature) que disponemos es el valor del promedio de bits. Claramente hay un valor de frontera que es 0.5, que separa la categoría clara de oscura.

El problema puede ser mucho más complejo e involucrar muchas variables. Dado que es un problema de aprendizaje supervisado, se debe tener un conjunto de entrenamiento etiquetado para cada una de las categorías.

El modelo de la regresión logística consiste en aplicar una función sigmoide
$$
\begin{align}
y &= f(z) = \frac{1}{1+e^{-z}}
\end{align}
$$
donde $z=a x + b$, en este caso cuanto mayor es $a$ más parecida a una función escalón será $f$, mientras que $b$ desplaza el centro de simetría sobre el eje $x$ una cantidad $-b/a$.

Para tener una función de pérdida monótona en este tipo de problemas, no se pueden utilizar los errores vistos previamente (MSE y MAE), y conviene definir a la función de pérdida de la siguiente manera
$$
\begin{align}
\mathcal{L}(y,\hat{y}) &= -\hat{y} \log{[f(ax+b)]}-(1-\hat{y})\log{[1-f(ax+b)]}
\end{align}
$$

A partir de esta definición se puede utilizar el método de descenso por el gradiente como se ha definido para la regresión lineal. Para esto, sólo basta con conocer las derivadas respecto de los parámetros
$$
\begin{align}
\frac{\partial\mathcal{L}}{\partial a} &= \frac{1}{N}\sum_{i=1}^{N}{[f(a x_i + b)-\hat{y}_i ]}x_i, \\
\frac{\partial\mathcal{L}}{\partial b} &= \frac{1}{N}\sum_{i=1}^{N}{f(a x_i + b)\hat{y}_i },\end{align}
$$
y las Ecuaciones (7) y (8) se pueden aplicar.

### Muchas variables

Cuando se tiene más de una variable, el problema es similar, suponiendo que se tiene una frontera definida entre las diferentes categorías. El modelo que se propone es
$$
y = f(a_1 x_1 + a_2 x_2 +...+b),
$$
donde $f$ es una función sigmoide como la de la Ecuación (9).

Tanto por notación como por la practicidad inherente, resulta importante escribir el problema de la siguiente manera:

$$
y = f(\vec{w}^T\cdot \vec{x}),
$$
donde $\vec{w} = (b, a_1,...,a_n)$ y $x=(1, x_1, ... , x_n)$. El gradiente se obtiene a partir de la regla de la cadena de manera sencilla

$$
\begin{align}
\frac{\partial\mathcal{L}}{\partial w_i} &= \frac{1}{N}\sum_{i=1}^{N}{[f(\vec{w}^T\cdot \vec{x})-\hat{y}_i ]}x_i
\end{align}
$$

Para comprender este problema es importante ver [este notebook](./Tema-5-2-regresion-logistica.ipynb)

# Ejercicios propuestos

1. Utilizando los datos del Servicio Meteorológico Nacional del mes de junio provistos en la carpeta _/Data/junio-SMN_ crear un modelo de regresión lineal para la serie temporal de la temperatura con un delay de 24 horas para un día intermedio y estimar el error en la predicción para los días subsiguientes.

    * Plantear una medida del error cometido en la predicción y estudiar cómo evoluciona el error a lo largo del tiempo.

    * Extender el modelo para incorporar en el aprendizaje más días.

2. Para el mismo set de datos:
    
    * Realizar un predictor que sea capaz de distinguir entre las estaciones Salta y Ushuaia ¿cúantas variables o features son necesarias?

    * Realizar lo mismo para las estaciones Salta y Tucuman
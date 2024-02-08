# Procesos estocásticos

Para describir someramente este tipo de procesos vamos a seguir la presentación de la referencia [1].

Los __procesos estocásticos__ son aquellos que se pueden describir mediante distribuciones de ___variables aleatorias___. Una serie temporal se puede caracterizar como una variable aleatoria que se va registrando en instantes sucesivos de tiempo. Normalmente se utiliza el concepto de _ensemble_ para caracterizar estas variables aleatorias, y evaluar los diferentes valores esperados. Un _ensemble_ es un conjunto de muchas (sino infinitas) ___realizaciones___ de una variable aleatoria. Como en las series temporales por lo general se toma un solo dato en cada instante $t$, se dice que la serie temporal corresponde a una de las posibles realizaciones del _ensemble_ del __proceso estocástico__.

Para describir las distribuciones aleatorias, es conveniente utilizar los denominados momentos. Los momentos de más bajo orden de una variable aleatoria univariada $X(t)$ son:

* Media
$$\mu(t) = E[X(t)]$$
* Varianza
$$Var[X(t)] = \sigma^2(t)= E[(X(t)-\mu)^2]$$
* Autocovarianza
$$ \gamma(t_1,t_2) = E\{[X(t_1)-\mu(t_1)][X(t_2)-\mu(t_2)]\}$$

A partir de las definiciones previas, caracterizaremos diferentes tipos de series temporales

## Procesos Estacionarios

Como ya se ha visto en las secciones descriptivas previas, un proceso se dice estacionario, cuando la distribución no varía en el tiempo, es decir que la media y la varianza son constantes para todos los subconjuntos $\{t_1, t_2, ... , t_n\}$:
$$
\mu(t) = \mu \\
\sigma^2(t) = \sigma^2
$$
mientras que la autocovarianza de la distribución conjunta para un par de tiempos $t_1,t_2$ cumple que dependen del retardo $\tau = (t_2-t_1)$, es decir

$$
\gamma(t_1, t_2) = \gamma(\tau)=E\{[X(t)-\mu][X(t+\tau)-\mu]\}
$$

En este punto resulta útil definir la autocorrelación (con valores entre 0 y 1) como

$$
\rho(\tau) = \frac{\gamma(\tau)}{\gamma(0)}
$$

## Procesos puramente aleatorios

Cuando tenemos una sucesión temporal de variables completamente aleatorias e idénticas entre sí (no existe ninguna causalidad entre ellas), y dado que $\mu$ y $\sigma^2$ son constantes porque en cada instante son distribuciones idénticas, se puede mostrar fácilmente que
$$
\rho(k) =1 \ \ si \ \ k=0 \ \ \,
$$
mientras que 
$$
\rho(k) = 0 \ \ si \ \ k\neq 0 \ \ \
$$

## Caminata aleatoria

Supongamos que tenemos un proceso puramente aleatorio $Z(t)$ con media $\mu_Z$ y varianza $\sigma_Z^2$. Una caminata aleatoria se define como:

$$
X(t_{i}) = X(t_{i-1}) + Z(t_i).
$$

Si $X(t=0) = 0$, se puede ver que $X(t_1) = Z(t_1)$, y en el _n-ésimo_ paso $X(t_n) = \sum_{i=1}^n{Z(t_i)}$. Este proceso no es estacionario, ya que $E[X]=t\mu_Z$ y $Var[X]=t \sigma_Z^2$.

## Procesos de media móvil



## _Bibliografía_
[1] Chatfield, Chris. The Analysis of Time Series: An Introduction, Sixth Edition. Reino Unido: CRC Press, 2003.

[2] Joseph, Manu. Modern Time Series Forecasting with Python: Explore Industry-ready Time Series Forecasting Using Modern Machine Learning and Deep Learning. Reino Unido: Packt Publishing, 2022.

# Análisis en el espectro de frecuencias

Cuando se tiene un proceso estocástico estacionario (ya sea naturalmente, o el resultado de haber extraído la tendencia), resulta de especial interés comprender si existen _estacionalidades_ o componentes oscilatorias marcadas. Para ello la Transformada de Fourier es la herramienta adecuada. Si bien la transformada de Fourier está formulada para funciones continuas, existe una interpretación para funciones discretas. En éste caso se denomina Transformada Discreta de Fourier (DFT), y para la cual existe un algoritmo especial denominada Transformada Rápida de Fourier (FFT). A lo largo de este tema estudiaremos algunas definiciones y utilidades de este tipo de transformaciones y su posterior análisis. En este curso utilizaremos números complejos.  

Sea $z = a + ib$ un número complejo, donde la parte real es $a$ y la función que tiene como imagen esta componente es: $Re(z)=a$. De igual manera la parte imaginaria es $b$ y se obtiene como $Im(z)=b$. Para el desarrollo de este curso utilizaremos la notación de Euler para los números complejos

$$
z = Re^{i\theta} = R [\cos{(\theta)}+i\sin{(\theta)}],
$$
con $R = \sqrt{a^2 + b^2}$ y $\theta = \arg{(z)} = \arctan(b/a)$. Esta notación es sumamente compacta y útil para desarrollar estos temas.


## La Serie de Fourier

Una función continua y periódica $f(t)$ en el intervalo $[-\tau/2,\tau/2]$ puede aproximarse como 
$$
\begin{align}
f(t)\approx \frac{a_0}{2} + \sum_{n=1}^{\infty}{a_n e^{i\frac{2n\pi t}{\tau}}}
\end{align}
$$

donde los coeficientes se obtienen como 

$$
\begin{align}
a_n = \int_{-\tau/2}^{\tau/2} {f(t) e^{-i\frac{2n\pi t}{\tau}} dt}
\end{align}
$$

## Transformada de Fourier
La transformada de Fourier de una función continua $f(t)$ se define como
$$
\begin{align}
\mathcal{F}(\omega) &=& \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{-i\omega t}f(t) dt\\
&=& \frac{1}{\sqrt{2\pi}}\left[\int_{-\infty}^{\infty}\cos{(\omega t)}f(t)dt+ i \int_{-\infty}^{\infty}\sin{(\omega t)}f(t)dt\right].
\end{align}
$$

Con las definiciones anteriores se puede ver que $\mathcal{F}$ es una función compleja, pero cuyas componentes pueden obtenerse en términos de integrales en el dominio real.

## Transformada discreta de Fourier (DFT)

Como las series temporales que se utilizan en este curso, son esencialmente discretas, describiremos la DFT. Sea nuestra serie $X(t_n)$ con $N$ elementos enumerados desde cero, es decir $\{0,1,..,N-1\}$. La DFT se escribe como

$$
\tilde{X}(f_j) = \frac{1}{\sqrt{N}}\sum_{n = 0}^{N-1}e^{-i \frac{2 \pi\ j\ n}{N}}X(t_n),\ \ \ j = \{0,1,2,....,N-1\}
$$

Se puede ver que no se necesita el espaciado temporal para calcular la DFT, por ello, resulta imprescindible poder relacionar el dominio temporal y el de frecuencias.
Si contamos con una discretización temporal dada por $\Delta t$, las frecuencias $f_j$ quedan determinadas por el número total de elementos y el espaciado temporal de la siguiente manera:  
$$\Delta f = \frac{1}{N\Delta t} $$
y las frecuencias estarán dadas en el intervalo: 
$$
\begin{align}
\left[-\frac{N}{2} , \frac{N}{2}-1 \right] \Delta f &   & si \ N \ par\\
\left[-\frac{N-1}{2} , \frac{N-1}{2} \right] \Delta f & & si \ N \ impar
\end{align}
$$


El algoritmo más importante para calcular es la transformada rápida de Fourier (FFT).

## Espectro de potencia

El espectro de potencia (o densidad espectral) muestra cuáles son las frecuencias más importantes de una serie temporal. El espectro de frecuencia está dado por el módulo cuadrado de la función transformada de Fourier

Cuando las series temporales son muy largas o densas, o cuando no son sampleadas en intervalos regulares, el cómputo de la DFT se torna computacionalmente costoso en el primer caso, o incierta su interpretación en el segundo, por lo que se recurre a diferentes estimadores del espectro de frecuencias. Entre los diferentes estimadores que se pueden utilizar, el más importante es el cálculo del periodograma, de igual modo se suelen utilizar ajustes por cuadrados mínimos de señales reconstruidas. Estos tópicos implican diversos. Dado que no es el objeto de este curso entrar en sumo detalle de las diversas técnicas, en caso de ser necesaria una mayor profundización, se puede encontrar una lista de algunas técnicas de estimación en este [link](https://en.wikipedia.org/wiki/Spectral_density_estimation#Periodogram).

## Espectrogramas

Existe una herramienta muy utilizada para analizar series temporales, que es intentar realizar un análisis combinado en el dominio temporal conjuntamente con el espectro de frecuencias. Si bien ambos dominios son complementarios, y por lo tanto es imposible conseguir una función de ambas variables, lo que se suele hacer para una serie temporal es observar el espectro de frecuencias posibles en diferentes segmentos de tiempo. Esto se puede realizar de una gran cantidad de maneras, fundamentalmente basadas en la manera en que se toman las ventanas de tiempo.
La más común y que utilizaremos en este curso es la _Windowed Fourier Transform_ donde en cada ventana temporal se realiza la DFT.


La librería scipy trae una implementación muy buena ([spectrogram](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.spectrogram.html))
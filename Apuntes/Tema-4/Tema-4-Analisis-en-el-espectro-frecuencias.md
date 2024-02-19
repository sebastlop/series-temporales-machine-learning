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

Como las series temporales que se utilizan en este curso, son esencialmente discretas, describiremos la DFT. Sea nuestra serie $X(t_i)$ con $N$ elementos enumerados desde cero, es decir $\{0,1,..,N-1\}$. La DFT se escribe como

$$
\tilde{X}(\omega_j) = \frac{1}{\sqrt{2\pi N}}\sum_{i = 0}^{N}e^{-i\omega_j t_i}X(t_i),\ \ \ j = \{0,1,2,....,N-1\}
$$

donde las frecuencias quedan determinadas por el número total de elementos:  $\omega_j = i/N$

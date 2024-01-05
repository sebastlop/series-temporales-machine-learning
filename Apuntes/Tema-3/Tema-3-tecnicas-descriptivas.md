# Análisis Estadístico de series temporales

En términos generales, las series temporales (ST) varían en el tiempo y el análisis de esta variación es lo que se realiza en los análisis clásicos. Normalmente, aunque esto no es la regla general, se intenta descomponer a las variaciones que sigue la ST en los siguientes términos:
1. Tendencia: se suele representar mediante una función monótona que sigue la  media de la serie.
2. Fluctuaciones cíclicas: cambios cíclicos que sufre la ST. Cuando se trata de ST que varían a lo largo de los años se suele hablar de estacionalidad
3. Fluctuaciones irregulares: este tipo de fluctuaciones puede ser aleatorio, sin ningun tipo de relación con características evidentes, como así también puede ser un proceso autoregresivo.

Dentro de las caracterizaciones que se pueden realizar de las ST, la primera y más importante es poder establecer si una serie es estacionaria. Dependiendo del autor la definición varía. En este punto seguiremos la definición porporcionada en la referencia [2] ya que resulta más concisa. Una serie se dice estacionaria si la distribución probabilística de los datos permanece constante en el tiempo. 

> **Series estacionarias:** Aquellas que mantienen la distribución probabilística de los datos constantes en el tiempo. La ***media*** y la ***varianza*** son constantes en la serie. 

Una manera de observar la estacionariedad de una serie temporal es analizar la distribución de datos en diferentes ventanas de tiempo 

# Análisis de tendencias



## _Bibliografía_
[1] Chatfield, Chris. The Analysis of Time Series: An Introduction, Sixth Edition. Reino Unido: CRC Press, 2003.

[2] Joseph, Manu. Modern Time Series Forecasting with Python: Explore Industry-ready Time Series Forecasting Using Modern Machine Learning and Deep Learning. Reino Unido: Packt Publishing, 2022.
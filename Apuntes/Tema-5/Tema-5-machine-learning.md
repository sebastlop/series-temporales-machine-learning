# Machine Learning

El aprendizaje automatizado o machine learning (ML) es un conjunto de herramientas matemáticas que sirven para modelar un problema sin conocer la forma de dependencia de las variables involucradas, tal dependencia entre las variables es precisamente lo que el modelo aprende automáticamente. 

En el trabajo de modelado usual, lo que se realiza es proponer una forma funcional de las variables involucradas a partir de principios teóricos o observacionales que se denominan leyes.

El ML lo que hace es proponer una forma general de relación funcional cuyas propiedades y formas relacionales se ajustan a partir de la observación.

Supongamos que para un proceso $P$, se propone un modelo que puede representarse mediante alguna relación $f$ de la siguiente manera $y = f(x)$, donde $x$ representa todas las magnitudes de entrada del modelo y $y$ todas las salidas.

Existen numerosos ejemplos en ciencias de modelados que siguen razonamientos desde primeros principios (sean estos verificables o no). Un ejemplo es la ley de Ohm, que surge a partir de la extrapolación de los trabajos de Fourier sobre la transferencia de calor. La ley de Ohm resultó fundamental para construir el electromagnetismo. Esta ley surgió de pensar que la corriente eléctrica seguía las mismas formas que la transferencia de calor en conductores proponiendo que la tensión era directamente proporcional a la corriente.

Por el contrario, en el ML el proceso que se seguiría para encontrar esta ley sería aproximadamente esta: proponer una relación general entre las variables medidas, y ajustar los parámetros de la relación. El encargado de ajustar y encontrar los parámetros involucrados en el modelo será un algoritmo.

# Tipos de problemas del ML

Dada la amplitud del tema, el ML suele clasificarse en dos grandes grupos (hoy se consideran 3).

## Aprendizaje supervisado

Este tipo de machine learning utiliza datos _etiquetados_ de entrada y salida para ser procesados en algoritmos de aprendizaje automático. Cada par de datos entrada/salida permite al algoritmo cambiar el modelo para crear salidas lo más cercanas posible al resultado deseado. Entre los algoritmos más utilizados en el aprendizaje supervisado se encuentran las redes neuronales (neural networks), los árboles de decisión (decision trees), la regresión lineal (linear regression).

## Aprendizaje sin supervisar

Mientras que en el aprendizaje supervisado el algoritmo ajusta los parámetros del modelo a partir de los datos provistos como datos correctos, en el aprendizaje no supervisado (unsupervised learning) el algoritmo busca patrones en los datos. Entre los algoritmos más utilizados en el aprendizaje no supervisado se encuentran los modelos, k-means, la agrupación jerárquica (hierarchical clustering) entre otros.

## Tercer tipo? Aprendizaje por refuerzo

El aprendizaje por refuerzo (reinforcement learning) no es un tipo de aprendizaje supervisado, porque no se basa estrictamente en un conjunto de datos etiquetados, sino en la monitorización de la respuesta a las acciones tomadas. Tampoco es un aprendizaje no supervisado, ya que, cuando modelamos a nuestro "aprendiz" sabemos de antemano cuál es la recompensa esperada.  

Este es el tipo de machine learning más parecido al aprendizaje humano. El algoritmo o agente utilizado aprende interactuando con su entorno y obteniendo una recompensa positiva o negativa. Los algoritmos más comunes son la diferencia temporal (temporal difference), las redes adversarias profundas (deep adversarial networks) y el aprendizaje Q (Q-learning).


Existen muchas referencias en la web como estos artículos de los que se extrajeron algunas definiciones:

https://www.coursera.org/mx/articles/types-of-machine-learning
https://telefonicatech.com/blog/que-algoritmo-elegir-en-ml-aprendizaje


# Librerías y Frameworks 

En este curso utilizaremos diferentes librerías y frameworks para analizar las series temporales:

* Scikit-learn: las instrucciones de instalación se encuentran en este link https://scikit-learn.org/stable/install.html

* PyTorch: las instrucciones para instalar PyTorch se encuentran aquí: https://pytorch.org/multipy/main/setup.html

Para ver todas las cosas que se pueden hacer con Scikit-learn se puede ver este link:
https://scikit-learn.org/stable/user_guide.html


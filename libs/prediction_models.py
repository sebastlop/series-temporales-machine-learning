import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

def naive(x):
    '''
    El input es un array con el primer indice correspondiente a los diferentes samples
    '''
    assert type(x) == type(np.zeros(1)), 'x debe ser un array de numpy'
    return np.take(x,-1,axis=x.ndim-1)

class delayed_naive:
    '''
        Esta clase es un predictor univariado de regresion lineal para todos los datos del conjunto de entrenamiento
        Es un wrapper de LinarRegression de SciKit learn.
        Toma una serie temporal y genera un conjunto de entrenamiento donde x(t) = a * x(t-delay) + b
    '''
    def __init__(self, serie, delay = 1) -> None:
        self.delay = delay
        self.x_train = serie[:-self.delay].reshape(-1,1)
        self.y_train = serie[self.delay:].reshape(-1,1)
        # Linear regressor
        self._regresor = LinearRegression()
        self._regresor.fit(self.x_train, self.y_train)
        self.a = self._regresor.coef_.reshape(-1)[0]
        self.b = self._regresor.intercept_.reshape(-1)[0]
        # get MAE of training set
        self.train_MAE = mean_absolute_error(self.y_train, self.predict(self.x_train))

    def get_attributes(self):
        attr = {
            'training_len' : len(self.x_train),
            'training_MAE' : self.train_MAE,
            'slope' : self.a,
            'bias' : self.b  
        }
        return attr

    def __call__(self, x):
        return self.predict(x)


    def predict(self, x):
        x.reshape(-1,1)
        return self._regresor.predict(x)


if __name__ == '__main__':
    x = np.random.randint(0,10,size=(10,3))
    print(x)
    print(naive(x))
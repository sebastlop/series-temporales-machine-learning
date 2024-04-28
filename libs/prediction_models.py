import numpy as np

def naive(x):
    '''
    El input es un array con el primer indice correspondiente a los diferentes samples
    '''
    assert type(x) == type(np.zeros(1)), 'x debe ser un array de numpy'
    return np.take(x,-1,axis=x.ndim-1)

class delayed_naive:
    def __init__(self, delay = 1):

        self.delay = delay

        # training stage

    def predict(self, x):
        return self.slope * x + self.bias 

    def loss(self, y, y_hat):
        return np.mean((y_hat-y)**2)

    def dloss(self, a, b, x, y_hat):
        da = -2*np.mean((y_hat-a*x-b)*x)
        db = -2*np.mean((y_hat-a*x-b))
        return da, db

    def train(self, x_train, y_train, epochs = 30, a = 1, b=1, lr = 0.001, hist = False):
        if hist:
            grad = self.dloss(a, b, x_train, y_train)  
            history = [[a, b, self.loss(a*x_train + b , y_train)]] 

        for i in range(epochs):
            grad = self.dloss(a, b, x_train, y_train) 
            a -= lr * grad[0]   
            b -=  lr * grad[1]  
            if hist:
                history.append([a, b, self.loss(a*x_train+b,y_train)])  # guardo la historia

        self.slope = a
        self.bias = b
        if hist:
            return a, b, history
        else:
            return a, b



if __name__ == '__main__':
    x = np.random.randint(0,10,size=(10,3))
    print(x)
    print(naive(x))
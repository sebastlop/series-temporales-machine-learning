import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
import os, csv


class procesador:
    ''' Esta clase sirve para procesar los 
        archivos obtenidos con el acelerometro
    '''
    def __init__(self, filepath):
        self.filepath = filepath
        self.read(self.filepath)
    
    def read(self, filename):
        with open(filename, 'r') as fp: # handler del archivo
            reader = csv.reader(fp, delimiter=';') # creamos el objeto que leera el archivo linea por linea
            data = [] # guardaremos cada linea en una lista
            for row in reader: # recorremos cada linea
                data.append(row) # agregamos cada linea
            columnas = data[0]
            data = np.array(data[1:], dtype = np.float32)
        self.tiempo = data[:,0]
        self.acels = data[:,1:]
        return columnas

    def interpolacion(self, col):
        assert type(col) == int, 'ojo amigue, col es int'
        return interp1d(self.tiempo, self.acels[:, col],kind='linear')

    def fit_params(self, col, pp):
        return curve_fit(self.func_fit,
                  self.tiempo, 
                  self.acels[:,col], 
                  p0 = pp)[0]
    
    def func_fit(self, x, a, b, w, fi):
        return a * np.sin(w*x+fi) + b
    
if __name__ == '__main__':
    filename = os.path.join('..','Data', 
                            'acelerometro','oscilador.csv')
    arch1 = procesador(filename)
    print(arch1.acels[:2])
    arch2 = procesador(os.path.join('..','Data', 
                            'acelerometro','caminata-ejemplo.csv'))
    columna = 0
    opt_val = arch2.fit_params(columna, [1,1,5,1])
    print(f'los valores optimos son: {opt_val}')
    print(f'el periodo correspondiente: {opt_val[2]/2/np.pi}')
    plt.xlabel('tiempo ', fontsize = 24)
    plt.xticks(fontsize = 18)
    plt.plot(arch2.tiempo, arch2.acels[:,columna])
    plt.plot(arch2.tiempo, arch2.func_fit(arch2.tiempo, *opt_val))
    plt.show()
 

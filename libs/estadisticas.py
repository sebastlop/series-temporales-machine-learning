def ma(t, x, ws= 5):
    ''' Funcion para calcular la media movil de una serie temporal (simetrica)
        Entradas:
            - t: timestamps
            - x: serie datos
            - ws: tamaño de la ventana
        Salidas:
            - t: timestamps
            - y: media movil
    '''

    assert ws%2 == 1, 'ws debe ser entero e impar' 
    n_samples = x.shape[0]
    n_windows = n_samples-ws
    tstamps = []
    y = np.zeros(n_windows)
    for i in range(0, n_windows):
        right = n_samples - i 
        left = n_samples - i - ws 
        y[n_windows - i - 1] = x[left:right].mean() 
        tstamps.insert(0,t[(left+right)//2])
    return tstamps, y

def mstd(t, x, ws= 5):
    ''' Funcion para calcular la desviacion estandar movil de una serie temporal (simetrica)
        Entradas:
            - t: timestamps
            - x: serie datos
            - ws: tamaño de la ventana
        Salidas:
            - t: timestamps
            - y: media movil
    '''

    assert ws%2 == 1, 'ws debe ser entero e impar' 
    n_samples = x.shape[0]
    n_windows = n_samples-ws
    tstamps = []
    y = np.zeros(n_windows)
    for i in range(0, n_windows):
        right = n_samples - i 
        left = n_samples - i - ws 
        y[n_windows - i - 1] = x[left:right].std() 
        tstamps.insert(0,t[(left+right)//2])
    return tstamps, y

# Los datos del SMN tienen dos columnas de encabezado, hay que leer con cuidado, 
# parece estar hecho en un encoding traido de windows.
# Los archivos parecen tener ancho de columnas fijas

import os, datetime
import numpy as np

class read_smn:
    def __init__(self, data_folder):
        # Leemos toda la carpeta
        raw_data = []
        for f in os.listdir(data_folder):
            headers, data = self.read_fixed_columns_file(os.path.join(data_folder, f),
                                widths=[0,8,14,20,25,33,38,43,1000],
                                n_heads=2)
            raw_data.append(self.clean_raw(data))
        
        # damos formato
        self.data_fmttd = []
        for day in raw_data:
            for d in day:
                # Since data is not very well structured and a lot of carriage return appear
                if len(d) > 7:
                    self.data_fmttd.append({
                        'timestamp': datetime.datetime.strptime(d[0],'%d%m%Y')+ datetime.timedelta(hours= int(d[1])),
                        'temp': float(d[2]),
                        'hum': float(d[3]),
                        'pres': float(d[4]),
                        'v_direcc': float(d[5])%360, # modulo function to put data into one cycle
                        'v_intens': float(d[6]),
                        'estac': d[7]
                    }
                    )

    
    def read_fixed_columns_file(self, filename, widths, n_heads):
        '''
        Se deben proveer las posiciones de comienzo de las diferentes columnas, salvo la ultima
        Por ejemplo: para un archivo con dos columnas cuyos anchos sean 5 caracteres y 10
                    widths = [0,5]
        n_heads: Numero de lineas de encabezado
        '''
        assert type(widths) == type([])
        with open(filename, 'rb') as fp:
            headers = []
            for i in range(n_heads):
                headers.append(next(fp).decode(errors='replace').split()) # elimino errores de codificación
            raw_data = []
            for line in fp:
                lines = line.decode(errors='replace')

                raw_data.append(
                    [lines[widths[i]:widths[i+1]].strip() for i in range(len(widths)-1)]
                    )
        return headers, raw_data

    def clean_raw(self, raw_data):
        '''
        Como los archivos tienen varios problemas, esta función va desarrollandose a medida que
        tales problemas aparecen. Por ahora se observa que existen saltos de carro en algunas lineas
        de los archivos de texto
        '''
        # limpiando las columnas con salto de carro
        clean = []
        for l in raw_data:
            if l[0] != '':
                clean.append(l)
        # reemplazando los strings vacíos por -1 
        for l in range(len(clean)):
            for it in range(len(clean[l])):
                if clean[l][it] == '':
                    clean[l][it] = '-1' # Controlando los datos vacíos

        return clean
    
    def filter_by_station(self,station_substring):
        time = []
        data = []
        for element in self.data_fmttd:
            if element['estac'].find(station_substring) >= 0:
                time.append(element['timestamp'])
                data.append([
                    element['temp'], 
                    element['hum'], 
                    element['pres'], 
                    element['v_direcc'], 
                    element['v_intens']])
        # hacemos arrays de numpy con las listas y las ordenamos en el tiempo
        time = np.array(time)
        idx_sorted = np.argsort(time)
        time = time[idx_sorted]
        data = np.array(data)[idx_sorted]
        return time, data






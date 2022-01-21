## Aquí irán las funciones encargadas de la simulación y el graficado de los datos.
from asyncore import poll
import matplotlib.pyplot as plt

## AQUI EN CUANTO ESTÉ HECHO LO DE FILTRAR POR AÑOS DEBEMOS AGREGAR UN ARGUMENTO A plotter
## QUE PIDA EL AÑO SOLICITADO Y CAMBIAR EL X LABEL DE LOS PLOTS PARA QUE CORRESPONDA AL AÑO
def plotter(x_axys: str, y_axis: str, y_axis2: str,pollutant:str,factor:str):

    if pollutant == 'CO(GT)':
        #print("WTF")
        concentration='CO (Monóxido de carbono) [mg/m^3]'
    elif pollutant =='PT08.S1(CO)':
        concentration='PT08.S1 (Oxido de estaño) [mg/m^3]'
    elif pollutant =='NMHC(GT)':
        concentration='NMHC (Hidrocarburos no-metánicos) [microg/m^3]'
    elif pollutant =='C6H6(GT)':
        concentration='C6H6 (Benceno) [microg/m^3]'
    elif pollutant =='PT08.S2(NMHC)':
        concentration='PT08.S2 (Titanio) [microg/m^3]'
    elif pollutant =='NOx(GT)':
        concentration='NOx (Óxido de nitrógeno) [ppb]'
    elif pollutant =='PT08.S3(NOx)':
        concentration='PT08.S3 (Óxido de tungsteno) [microg/m^3]'
    elif pollutant =='NO2(GT)':
        concentration='NO2 (Dióxido de nitrógeno) [microg/m^3]'
    elif pollutant =='PT08.S4(NO2)':
        concentration='PT08.S4 (Óxido de tungsteno) [microg/m^3]'
    elif pollutant =='PT08.S5(O3)':
        concentration='PT08.S5 (Óxido de indio) [microg/m^3]'

    if factor =='AH':
        factor1='Humedad Absoluta'
        factor2='Humedad Absoluta [g/m^3]'
    if factor =='T':
        factor1='Temperatura'
        factor2='T [ºC]'

    ##NOTA, CORREGIR LOS LIMITES DE PLOTEO
    plt.figure()
    plt.subplot(211)
    plt.plot(x_axys[0:1000], y_axis[0:1000],"-")
    plt.title('Concentración de {} a lo largo del tiempo'.format(pollutant))
    plt.ylabel("{}".format(concentration))
    plt.xlabel("Tiempo")

    plt.subplot(212)
    plt.plot(x_axys[0:1000], y_axis2[0:1000],"-", color="r")
    plt.title('Medición de {} a lo largo del tiempo'.format(factor1))
    plt.ylabel("{}".format(factor2))
    plt.xlabel("Tiempo")
    fig = plt.gcf()
    fig.set_size_inches(20, 10)
    #fig.savefig('Graficas.png', dpi=100)
    plt.show()

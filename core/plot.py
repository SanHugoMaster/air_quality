import matplotlib.pyplot as plt
from constants import pollutant_labels, factor_labels

## AQUI EN CUANTO ESTÉ HECHO LO DE FILTRAR POR AÑOS DEBEMOS AGREGAR UN ARGUMENTO A plotter
## QUE PIDA EL AÑO SOLICITADO Y CAMBIAR EL X LABEL DE LOS PLOTS PARA QUE CORRESPONDA AL AÑO


def label_interpreter(pollutant: str, factor: str):
    concentration, variable = (pollutant_labels[pollutant], factor_labels[factor])
    return (concentration, variable)


def plotter(x_axys: str, y_axis: str, y_axis2: str, pollutant: str, factor: str):
    concentration, factors = label_interpreter(pollutant, factor)

    # NOTA, CORREGIR LOS LIMITES DE PLOTEO
    plt.figure()
    plt.subplot(211)
    plt.plot(x_axys[0:1000], y_axis[0:1000], "-")
    plt.title(f"Concentración de {pollutant} a lo largo del tiempo")
    plt.ylabel(f"{concentration}")
    plt.xlabel("Tiempo")
    plt.subplot(212)
    plt.plot(x_axys[0:1000], y_axis2[0:1000], "-", color="r")
    plt.title(f"Medición de {factors[0]} a lo largo del tiempo")
    plt.ylabel(f"{factors[1]}")
    plt.xlabel("Tiempo")
    fig = plt.gcf()
    fig.set_size_inches(20, 10)
    # fig.savefig('Graficas.png', dpi=100)
    return plt.show()

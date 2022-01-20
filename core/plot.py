## Aquí irán las funciones encargadas de la simulación y el graficado de los datos.
import matplotlib.pyplot as plt


def plotter(x_axys: str, y_axis: str):
    plt.figure()
    plt.plot(x_axys[0:1000], y_axis[0:1000], "-")
    fig = plt.gcf()
    fig.set_size_inches(20, 10)
    plt.show()
    # TODO: Falta nombrar los nombres de los ejes "x" y "y"

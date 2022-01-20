from utils import DataAnalysis
from plot import plotter

# from commons.constants import pollutants


## Estos diccionarios no deberian estar aquí, sino importarse desde el archivo de constantes
## pero no he logrado resolver el problema de por qué no me deja importarlos
## directamente
pollutants = {
    "CO": "CO(GT)",
    "PT08_S1": "PT08.S1(CO)",
    "NMHC": "NMHC(GT)",
    "C6H6": "C6H6(GT)",
    "PT08_S2": "PT08.S2(NMHC)",
    "NOX": "NOx(GT)",
    "PT08_S3": "PT08.S3(NOx)",
    "NO2": "NO2(GT)",
    "PT08_S4": "PT08.S4(NO2)",
    "PT08_S5": "PT08.S5(O3)",
}
variables = {"T": "T", "H": "AH"}


class UserInterface:
    def input_retriever(self):
        while True:
            try:
                ## mejor cambie este print acá porque abajo se veía feon
                print(
                    "Bienvenido al programa que te permite recuperar información gráfica acerca de algunos contaminantes"
                )
                self.pollutant = input(
                    f"Escoge un contaminante a analizar de la siguiente lista: {pollutants.keys()}\n"
                )
                self.factor = input(
                    f"Escoge una propiedad de la siguiente lista: {variables.keys()}\n"
                )
                pollutant = pollutants.get(self.pollutant)
                factor = variables.get(str(self.factor))
                analysis = DataAnalysis().data_retriever(
                    "raw_data/AirQualityUCI.csv", pollutant, factor
                )
                ## Aquí tendría que invocar una función que elimine los registros NaN
                DataAnalysis().empty_data_remover()
                ## A continuación invoco a otra función para darle formato a
                ## la fecha y al contaminante, su definición la pueden encontrar en
                ## el archivo de utils.py
                DataAnalysis().data_formatter(analysis, pollutant)
                ## Moví el código que había aquí para graficar y lo metí en una función
                ## que se dedica exclusivamente al graficado y la pueden encontrar
                ## en el archivo core/plot.py
                plotter(analysis["Date"], analysis[pollutant])
                print("ADIOS")
                return analysis
            except:
                print("Los datos ingresados son incorrectos")
                ## Creo que me parece más conveniente que el usuario solo
                ## escriba la letra "n" en caso de no querer continuar
                retry = input("¿Quieres intentar de nuevo? s/n\n")
                if retry == "n":
                    break


UserInterface().input_retriever()

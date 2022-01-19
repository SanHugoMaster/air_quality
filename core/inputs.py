from utils import DataAnalysis

# from commons.constants import pollutants

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
                self.pollutant = input(
                    f"Escoge un contaminante de la siguiente lista: {pollutants.keys()}\n"
                )
                self.factor = input(
                    f"Escoge una propiedad de la siguiente lista: {variables.keys()}\n"
                )
                analysis = DataAnalysis().data_retriever(
                    "raw_data/AirQualityUCI.csv",
                    pollutants.get(str(self.pollutant)),
                    variables.get(str(self.factor)),
                )
                print(analysis)
                print("ADIOS")
                return analysis
            except:
                print("Los datos ingresados son incorrectos")
                v = input("¿Quieres intentar de nuevo? si/no\n")
                if v == "no":
                    break


## En esta clase(que aun no estoy segura de dejar como clase), indicarás dónde
# estará ubicada la animación o resultado final.
# class FinalResult:
#     def plot_location(self):

print("Rafa estuvo aquí")
 
print(
    "Bienvenido al programa que te permite recuperar información gráfica acerca de algunos contaminantes"
)

UserInterface().input_retriever()

from argparse import ArgumentDefaultsHelpFormatter
import pandas as pd
import matplotlib.pyplot as plt
import math

class DataAnalysis:
    def file_reader(self, file: str):
        dataframe = pd.read_csv(file, delimiter=";")

        return dataframe

    def data_retriever(self, file, data1: str, data2: str):
        data = self.file_reader(file)[["Date", "Time", data1, data2]]
        return data


############ RESULTADO FINAL:
# solo se introducen tres variables, el tipo de contaminante,
# otra variable a comparar y el rango de fechas (opcional) con
# formato específico. Como output se muestra la animación y se
# da una interpretación de los datos (con esto igual puedes hacer
# un rango de datos).


##ESTOY USANDO UTILS.PY PARA HACER PRUEBAS; ESTO SE PUEDE COPIAR COMPLETO EN OTRO ARCHIVO
#Esto lo necesito para definir variables, se va a borrar después
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
    "PT08_S5": "PT08.S5(O3)",}
variables = {"T": "T", "H": "AH"}
#Esto era para probar la ubicación del archivo y generar el dataframe
analysis = DataAnalysis().data_retriever(
                    "raw_data/AirQualityUCI.csv",
                    pollutants.get("CO"),
                    variables.get("T")
                    )
    #print(analysis)
    ###Innecesario cambiando el : por . en format
    #Cambiamos el formato del tiempo para que se pueda leer más adelante
    #analysis["Time"]=analysis["Time"].str.replace('.',':')
    #print(analysis["Time"])
##Juntamos las columnas Date y Time en Date
#Esto es necesario para convertir en to_datetime y graficar correctamente
analysis["Date"]=analysis["Date"]+' '+analysis["Time"]
    #print(analysis["Date"])
##Cambiamos el formato de date y de CO
# FALTA CAMBIAR EL FORMATO DE TODAS LAS OTRAS COLUMNAS DE CONTAMINANTES O HACERLO AUTOMATIZADO
analysis["Date"]=pd.to_datetime(analysis["Date"],format="%d/%m/%Y %H.%M.%S")
##Cambiamos comas por puntos y convertimos to_numeric
analysis["CO(GT)"]=pd.to_numeric(analysis["CO(GT)"].str.replace(',','.').str.replace('-200',''))
##Ploteamos figura del punto 0 al punto 1000 (completo son muchos datos)
#HABRIA QUE PEDIR EL AÑO QUE SE DESEA GRAFICAR Y OBTENER LAS COORDENADAS DE LOS DATOS
plt.figure()
plt.plot(analysis["Date"][0:1000],analysis["CO(GT)"][0:1000],"-")
#Para hacer la figura más grande y se vea bonito
fig=plt.gcf()
fig.set_size_inches(20, 10)
plt.show()

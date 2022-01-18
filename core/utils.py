import pandas as pd


class DataAnalysis:
    def file_reader(self, file: str):
        dataframe = pd.read_csv(file, delimiter=";")

        return dataframe

    def data_retriever(self, file, data1: str, data2: str):
        data = self.file_reader(file)[["Date", "Time", data1, data2]]
        return data


# resultado final:
# solo se introducen tres variables, el tipo de contaminante,
# otra variable a comparar y el rango de fechas (opcional) con
# formato específico. Como output se muestra la animación y se
# da una interpretación de los datos (con esto igual puedes hacer
# un rango de datos).

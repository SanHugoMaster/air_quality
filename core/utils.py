import pandas as pd
import numpy as np


class DataAnalysis:
    def file_reader(self, file: str):
        return pd.read_csv(file, delimiter=";")

    def data_retriever(self, file, data1: str, data2: str):
        return self.file_reader(file)[["Date", "Time", data1, data2]]

    def data_formatter(self, data: pd.DataFrame, pollutant: str):
        data["Date"] = data["Date"] + " " + data["Time"]
        data["Date"] = pd.to_datetime(data["Date"], format="%d/%m/%Y %H.%M.%S")
        data[pollutant] = pd.to_numeric(
            data[pollutant].str.replace(",", ".").str.replace("-200", "")
        )
        return data

    def empty_data_remover(self,data:pd.DataFrame)
        data.replace(r'^\s*$', np.nan, regex=True,inplace=True)
        data.dropna(inplace=True)
        return None

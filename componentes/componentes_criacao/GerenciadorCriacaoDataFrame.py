from abc import ABC, abstractmethod #implementacao da classe abstrata
import pandas as pd
import streamlit as st

class CriacaoDoDataFrame(ABC):
    
    @abstractmethod
    def retornar_dataframe(self):
        pass

class CriacaoDoDataFrameEmCSV(CriacaoDoDataFrame):

    def __init__(self,arquivo_bruto):
        self.arquivo_bruto = arquivo_bruto

    @st.cache()
    def retornar_dataframe(self):
        try:
            dataframe = pd.read_csv(self.arquivo_bruto)
            return dataframe
        except UnicodeDecodeError:
            raise Exception("ISO incompatível")
            
        
class CriacaoDoDataFrameEmExcel(CriacaoDoDataFrame):

    def __init__(self,arquivo_bruto):
        self.arquivo_bruto = arquivo_bruto
    
    @st.cache()
    def retornar_dataframe(self):
        try:
            dataframe = pd.read_excel(self.arquivo_bruto)
            return dataframe
        except UnicodeDecodeError:
            raise Exception("ISO incompatível")


class GerenciadorCriacaoDataFrame:

    def __init__(self,dataframe :CriacaoDoDataFrame,componente_slider,componente_multiselect):
        self.dataframe = dataframe
        self.componente_slider = componente_slider
        self.componente_multiselect = componente_multiselect
    
    def visualizar_dataframe(self):
        if len(self.componente_multiselect) == 0:
            st.dataframe(self.dataframe.iloc[0:self.componente_slider])

        else:
            st.dataframe(self.dataframe[self.componente_multiselect].iloc[0:self.componente_slider])

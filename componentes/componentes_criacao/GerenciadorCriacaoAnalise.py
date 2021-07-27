from abc import ABC,abstractmethod
import streamlit as st
import base64
from io import BytesIO
import pandas as pd

class CriacaoAnalise(ABC):

    @abstractmethod
    def gerar_analise(self):
        pass

class CriacaoAnaliseCategorica(CriacaoAnalise):

    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def gerar_analise(self):
        try:
            descricao_categorica = self.dataframe.describe(include=[object])
            novo_index_categorico = ['Quantidade','único','Valor mais frequente','frequência do mais frequente']
            descricao_categorica.index = novo_index_categorico        
            st.dataframe(descricao_categorica)
            return descricao_categorica
        except ValueError:
            return None

    def converter_excel(self,analise_desc_categorica):
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        analise_desc_categorica.to_excel(writer, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data

    def gerar_link_download(self,analise_desc_categorica):
        val = self.converter_excel(analise_desc_categorica)
        b64 = base64.b64encode(val) 
        return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="dados.xlsx">Download dados</a>'

class CriacaoAnaliseNumerica(CriacaoAnalise):

    def __init__(self,dataframe):
        self.dataframe = dataframe

    def gerar_analise(self):
        try:
            descricao_numerica =self.dataframe.describe()
            novo_index_num = ['quantidade','média','desvio padrão','min','25%', '50%', '75%', 'max']
            descricao_numerica.index = novo_index_num
            st.dataframe(descricao_numerica)
            return descricao_numerica
        except ValueError:
            return None
    
    def converter_excel(self,analise_desc_numerica):
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        analise_desc_numerica.to_excel(writer, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data

    def gerar_link_download(self,analise_desc_numerica):
        val = self.converter_excel(analise_desc_numerica)
        b64 = base64.b64encode(val) 
        return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="dados.xlsx">Download dados</a>'
        


class GerenciadorCriacaoAnalise:

    def __init__(self, analise: CriacaoAnalise):
        self.analise = analise
    
    def visualizar_analise(self):
        dados = self.analise.gerar_analise()
        if dados is not None:
            st.markdown(self.analise.gerar_link_download(dados), unsafe_allow_html=True)
        else:
            st.error('Erro ao criar analise descritiva')
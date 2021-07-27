import streamlit as st


class ComponenteDeConfiguracaoDoDataFrame:
    def __init__(self,dataframe):
        self.dataframe = dataframe
    
    def visualizar_configuracoes_do_dataframe(self):
        componente_slider = st.slider('Selecione a quantidade de linhas', 0, len(self.dataframe), 10)
        
        componente_multiselect = st.multiselect('Selecione as colunas',list(self.dataframe.columns.tolist()))

        return (componente_slider,componente_multiselect)
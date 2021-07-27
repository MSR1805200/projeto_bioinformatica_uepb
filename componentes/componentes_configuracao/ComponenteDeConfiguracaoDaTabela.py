import streamlit as st
from abc import ABC,abstractmethod

class ComponenteDeConfiguracaoDaTabela(ABC):

    @abstractmethod
    def visualizar_configuracoes_tabela(self):
       pass

class ComponenteDeConfiguracaoDaTabelaDeRepeticaoFrequencia(ComponenteDeConfiguracaoDaTabela):

    def __init__(self,colunas_categoricas,chave):
        self.colunas_categoricas = colunas_categoricas
        self.chave = chave
        
    def visualizar_configuracoes_tabela(self):
        coluna = st.selectbox('Selecione a coluna', self.colunas_categoricas, key = self.chave[0])
        return coluna

class ComponenteDeConfiguracaoDaTabelaDeContingencia(ComponenteDeConfiguracaoDaTabela):

    def __init__(self,colunas_categoricas,chave):
        self.colunas_categoricas = colunas_categoricas
        self.chave = chave
    
    def visualizar_configuracoes_tabela(self):
        linha = st.selectbox('Selecione a linha', self.colunas_categoricas, key = self.chave[0])
        coluna = st.selectbox('Selecione a coluna', self.colunas_categoricas, key = self.chave[1])

        return (linha,coluna)
    
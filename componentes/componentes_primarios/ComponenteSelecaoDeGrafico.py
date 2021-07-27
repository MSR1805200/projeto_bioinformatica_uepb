import streamlit as st


class ComponenteSelecaoDeGrafico:
    def __init__(self,coluna,chave):
        self.coluna = coluna
        self.chave = chave
    
    def visualizar_opcoes_grafico(self):

        lista_de_graficos = ['Dispersão','Histograma','Barras','BoxPlot','Linha']
        grafico = self.coluna.selectbox('Selecione o tipo de gráfico', lista_de_graficos,key = self.chave[0])        
        return grafico
      
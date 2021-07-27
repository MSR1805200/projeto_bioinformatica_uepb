from abc import ABC, abstractmethod #implementacao da classe abstrata
import streamlit as st
import plotly.express as px

class CriacaoDoGrafico(ABC):

    @abstractmethod
    def criar_grafico(self):
        pass


class CriacaoDoGraficoDeHistograma(CriacaoDoGrafico):

    def __init__(self,eixo_x,coluna,dataframe):
        self.eixo_x = eixo_x
        self.coluna = coluna
        self.dataframe = dataframe

    def criar_grafico(self):
        try:
            fig = px.histogram(x = self.dataframe[self.eixo_x], labels = {'x' : self.eixo_x})
            return fig
        except KeyError:
            return None

class CriacaoDoGraficoDeDispersao(CriacaoDoGrafico):

    def __init__(self,eixo_x,eixo_y,coluna,dataframe):
        self.eixo_x = eixo_x
        self.eixo_y = eixo_y
        self.coluna = coluna
        self.dataframe = dataframe
    
    def criar_grafico(self):
        try:
            fig = px.scatter(x = self.dataframe[self.eixo_x], y = self.dataframe[self.eixo_y], labels = {'x' : self.eixo_x, 'y' : self.eixo_y})
            return fig
        except KeyError:
            return None

class CriacaoDoGraficoDeBarras(CriacaoDoGrafico):
    
    def __init__(self,eixo_x,coluna,dataframe):
        self.eixo_x = eixo_x
        self.coluna = coluna
        self.dataframe = dataframe

    def criar_grafico(self):
        try:
            fig = px.bar(self.dataframe[self.eixo_x].value_counts().sort_values(ascending = False))
            return fig
        except KeyError:
            return None
class CriacaoDoGraficoDeBox(CriacaoDoGrafico):

    def __init__(self,eixo_x,coluna,dataframe):
        self.eixo_x = eixo_x
        self.coluna = coluna
        self.dataframe = dataframe

    def criar_grafico(self):
        try:
            fig = px.box(self.dataframe[self.eixo_x], labels = {'index' : self.eixo_x})
            return fig
        except KeyError:
            return None

class CriadorDoGraficoDeLinha(CriacaoDoGrafico):
    
    def __init__(self,eixo_x,eixo_y,coluna,dataframe):
        self.eixo_x = eixo_x
        self.eixo_y = eixo_y
        self.coluna = coluna
        self.dataframe = dataframe
    
    def criar_grafico(self):
        try:
            fig = px.line(x = self.dataframe[self.eixo_x], y = self.dataframe[self.eixo_y], labels = {'x' : self.eixo_x, 'y' : self.eixo_y})
            return fig
        except KeyError:
            return None

class GerenciadorCriacaoDeGrafico:

    def __init__(self,coluna,grafico: CriacaoDoGrafico):
        self.grafico = grafico
        self.coluna = coluna
    def visualizar_grafico(self):
        grafico = self.grafico.criar_grafico()
        if grafico is not None:
            self.coluna.plotly_chart(grafico, use_container_width=True)
        else:
            self.coluna.error('Erro ao criar o grafico')
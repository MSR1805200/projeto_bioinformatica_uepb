from abc import ABC, abstractmethod #implementacao da classe abstrata
import streamlit as st

class ComponenteDeConfiguracaoDoGrafico(ABC):

    @abstractmethod
    def visualizar_configuracoes_do_grafico(self):
        pass


class ComponenteDeConfiguracaoDoGraficoDeHistograma(ComponenteDeConfiguracaoDoGrafico):

    def __init__(self,colunas_numericas,coluna,chave):
        self.colunas_numericas = colunas_numericas
        self.coluna = coluna
        self.chave = chave

    def visualizar_configuracoes_do_grafico(self):
        eixo_x = self.coluna.selectbox('Eixo x',key = self.chave[1] ,options = self.colunas_numericas)
        return eixo_x

class ComponenteDeConfiguracaoDoGraficoDeDispersao(ComponenteDeConfiguracaoDoGrafico):

    def __init__(self,colunas_numericas,coluna,chave):
        self.colunas_numericas = colunas_numericas
        self.coluna = coluna
        self.chave = chave
    
    def visualizar_configuracoes_do_grafico(self):
        eixo_x = self.coluna.selectbox('Eixo X',key = self.chave[1], options = self.colunas_numericas)   
        eixo_y = self.coluna.selectbox('Eixo Y',key = self.chave[2],options = self.colunas_numericas)

        return(eixo_x,eixo_y)

class ComponenteDeConfiguracaoDoGraficoDeBarras(ComponenteDeConfiguracaoDoGrafico):

    def __init__(self,colunas_categoricas,coluna,chave):
        self.colunas_categoricas = colunas_categoricas
        self.coluna = coluna
        self.chave = chave

    def visualizar_configuracoes_do_grafico(self):
        eixo_x = self.coluna.selectbox('Selecione o eixo x',key = self.chave[1], options = self.colunas_categoricas)   
        return eixo_x

class ComponenteDeConfiguracaoDoGraficoDeBox(ComponenteDeConfiguracaoDoGrafico):

    def __init__(self,colunas_numericas,coluna,chave):
        self.colunas_numericas = colunas_numericas
        self.coluna = coluna
        self.chave = chave

    def visualizar_configuracoes_do_grafico(self):
        eixo_x = self.coluna.selectbox('Selecione o eixo x',key = self.chave[1], options = self.colunas_numericas)
        return eixo_x

class ComponenteDeConfiguracaoDoGraficoDeLinha(ComponenteDeConfiguracaoDoGrafico):
    def __init__(self,colunas_numericas,coluna,chave):
        self.colunas_numericas = colunas_numericas
        self.coluna = coluna
        self.chave = chave

    def visualizar_configuracoes_do_grafico(self):
        eixo_x = self.coluna.selectbox('Eixo X',key = self.chave[1], options = self.colunas_numericas)   
        eixo_y = self.coluna.selectbox('Eixo Y',key = self.chave[2], options = self.colunas_numericas)
        return(eixo_x,eixo_y)


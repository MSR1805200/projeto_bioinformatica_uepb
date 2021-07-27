from abc import ABC, abstractmethod #implementacao da classe abstrata
import pandas as pd
import streamlit as st
import base64
from io import BytesIO


class CriacaoTabela(ABC):

    @abstractmethod
    def criar_tabela(self):
        pass

class CriacaoTabelaRepeticaoFrequencia(CriacaoTabela):

    def __init__(self,dataframe,coluna):
        self.dataframe = dataframe
        self.coluna = coluna

    def ordenar_dados(self,dados):
        return sorted(dados)

    def calcular_frequencia_absoluta(self,dados_ordenados):
        freq_absoluta = [list(dados_ordenados).count(i) for i in dados_ordenados.unique()]
        return freq_absoluta

    def calcular_frequencia_relativa(self,dados_ordenados,frequencia_absoluta):
        freq_relativa = [frequencia_absoluta[i]/ sum(frequencia_absoluta)*100 for i in range(len(dados_ordenados.unique()))]
        return freq_relativa

    def calcular_frequencia_absoluta_acumulada(self,frequencia_absoluta):
        soma = 0
        freq_abs_acu = []
        for i in frequencia_absoluta:
            soma = soma + i
            freq_abs_acu.append(soma)
        return freq_abs_acu

    def calcular_frequencia_relativa_acumulada(self,frequencia_relativa):
        soma = 0
        freq_rela_acu = []
        for i in frequencia_relativa:
            soma = soma + i
            freq_rela_acu.append(soma)
        return freq_rela_acu
    
    def criar_tabela(self):
        try:
            dados_ordenados = self.dataframe[self.coluna].sort_values(ascending = True)

            frequencia_absoluta = self.calcular_frequencia_absoluta(dados_ordenados)
            frequencia_relativa = self.calcular_frequencia_relativa(dados_ordenados,frequencia_absoluta)

            frequencia_absoluta_acumulada = self.calcular_frequencia_absoluta_acumulada(frequencia_absoluta)
            frequencia_relativa_acumulada = self.calcular_frequencia_relativa_acumulada(frequencia_relativa)
            
            data = {
            'XI' :dados_ordenados.unique(), 
            'FI':frequencia_absoluta,
            'FR(%)':frequencia_relativa,
            'FAC': frequencia_absoluta_acumulada,
            'FRAC': frequencia_relativa_acumulada
            }
    
            tabela_repeticao_frequencia = pd.DataFrame(data)

            tabela_repeticao_frequencia =tabela_repeticao_frequencia.append({'XI': 'Total:',
                                                                            'FI':sum(frequencia_absoluta),
                                                                            'FR(%)':sum(frequencia_relativa),
                                                                            'FAC': ' - ',
                                                                            'FRAC': ' - '
                                                                            },ignore_index=True)
            return tabela_repeticao_frequencia

        except KeyError:
            return None

        except ValueError:
            return None

    def converter_excel(self,tabela_trf):
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        tabela_trf.to_excel(writer, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data

    def gerar_link_download(self,tabela_trf):
        val = self.converter_excel(tabela_trf)
        b64 = base64.b64encode(val) 
        return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="dados.xlsx">Download dados</a>'


class CriacaoTabelaContingencia(CriacaoTabela):

    def __init__(self,linha,coluna,dataframe):
        self.linha = linha
        self.coluna = coluna
        self.dataframe = dataframe
    
    def criar_tabela(self):
        try:
            tabela_contingencia = pd.crosstab(self.dataframe[self.linha],
                                                self.dataframe[self.coluna],
                                                rownames = [self.linha],colnames= [self.coluna],
                                                margins = True,margins_name = "Total")
            


            return tabela_contingencia
        
        except KeyError:
            return None
            
        except ValueError:
            return None

        
    def converter_excel(self,tabela_contingencia):
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        tabela_contingencia.to_excel(writer, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data

    def gerar_link_download(self,tabela_contingencia):
        val = self.converter_excel(tabela_contingencia)
        b64 = base64.b64encode(val) 
        return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="dados.xlsx">Download dados</a>'


class GerenciadorCriacaoTabela:

    def __init__(self, tabela:CriacaoTabela, chave):
        self.tabela = tabela
        self.chave = chave
    def visualizar_tabela(self):
        if st.button('gerar', key = self.chave):
            dados = self.tabela.criar_tabela()

            if dados is not None:
                st.dataframe(dados)
                st.markdown(self.tabela.gerar_link_download(dados), unsafe_allow_html=True)
            else:
                st.error('Erro na criação da tabela')
from componentes.componentes_primarios.ComponenteArrastaESolta import ComponenteArrastaESolta
from componentes.componentes_primarios.ComponenteSelecaoDeFuncao import ComponenteSelecaoDeFuncao
from componentes.componentes_primarios.ComponenteSelecaoDeGrafico import ComponenteSelecaoDeGrafico

from componentes.componentes_configuracao.ComponenteDeConfiguracaoDoDataFrame import ComponenteDeConfiguracaoDoDataFrame
from componentes.componentes_configuracao.ComponenteDeConfiguracaoDoGrafico import ComponenteDeConfiguracaoDoGraficoDeBarras,ComponenteDeConfiguracaoDoGraficoDeDispersao,ComponenteDeConfiguracaoDoGraficoDeBox,ComponenteDeConfiguracaoDoGraficoDeLinha,ComponenteDeConfiguracaoDoGraficoDeHistograma
from componentes.componentes_configuracao.ComponenteDeConfiguracaoDaTabela import ComponenteDeConfiguracaoDaTabelaDeContingencia,ComponenteDeConfiguracaoDaTabelaDeRepeticaoFrequencia

from componentes.componentes_criacao.GerenciadorCriacaoTabela import CriacaoTabelaContingencia,CriacaoTabelaRepeticaoFrequencia,GerenciadorCriacaoTabela
from componentes.componentes_criacao.GerenciadorCriacaoDataFrame import GerenciadorCriacaoDataFrame
from componentes.componentes_criacao.GerenciadorCriacaoDataFrame import CriacaoDoDataFrameEmCSV, CriacaoDoDataFrameEmExcel
from componentes.componentes_criacao.GerenciadorCriacaoDeGrafico import CriacaoDoGraficoDeBarras,CriacaoDoGraficoDeBox,CriacaoDoGraficoDeDispersao,CriacaoDoGraficoDeHistograma,CriadorDoGraficoDeLinha, GerenciadorCriacaoDeGrafico
from componentes.componentes_criacao.GerenciadorCriacaoAnalise import CriacaoAnaliseCategorica,CriacaoAnaliseNumerica, GerenciadorCriacaoAnalise

import streamlit as st

CHAVE_COLUNA_1 = ['tipo_grafico_1','eixo_x_1','eixo_y_1']
CHAVE_COLUNA_2 = ['tipo_grafico_2','eixo_x_2','eixo_y_2']
CHAVE_COLUNA_3 = ['tipo_grafico_3','eixo_x_3','eixo_y_3']
CHAVE_COLUNA_4 = ['tipo_grafico_4','eixo_x_4','eixo_y_4']

CHAVE_CONTINGENCIA = ['contingencia_linha','contingencia_coluna','botao_contingencia']
CHAVE_TRF = ['coluna_trf','botao_trf']

def identificar_tipo_do_arquivo(arquivo_bruto):
    nome_do_arquivo_bruto_dividido = arquivo_bruto.name.split('.')
    tipo_do_arquivo = nome_do_arquivo_bruto_dividido[-1]
    return tipo_do_arquivo

def retornar_dataframe_pelo_tipo(tipo,arquivo_bruto):
    if tipo == 'csv':
         componente_criacao_do_dataframe_em_csv = CriacaoDoDataFrameEmCSV(arquivo_bruto)
         return componente_criacao_do_dataframe_em_csv

    elif tipo == 'xlsx':
        componente_criacao_do_dataframe_em_excel = CriacaoDoDataFrameEmExcel(arquivo_bruto)
        return componente_criacao_do_dataframe_em_excel

def retornar_configuracoes_do_grafico_escolhido(tipo_do_grafico,coluna,colunas_numericas,colunas_categoricas,chave):
    if tipo_do_grafico == 'Dispersão':
        componente_de_configuracao_do_grafico_de_dispersao = ComponenteDeConfiguracaoDoGraficoDeDispersao(colunas_numericas,coluna,chave)
        return componente_de_configuracao_do_grafico_de_dispersao
    
    elif tipo_do_grafico == 'Histograma':
        componente_de_configuracao_do_grafico_de_histograma = ComponenteDeConfiguracaoDoGraficoDeHistograma(colunas_numericas,coluna,chave)
        return componente_de_configuracao_do_grafico_de_histograma
    
    elif tipo_do_grafico == 'Barras':
        componente_de_configuracao_do_grafico_de_barras = ComponenteDeConfiguracaoDoGraficoDeBarras(colunas_categoricas,coluna,chave)
        return componente_de_configuracao_do_grafico_de_barras
    
    elif tipo_do_grafico == 'BoxPlot':
        componente_de_configuracao_do_grafico_box = ComponenteDeConfiguracaoDoGraficoDeBox(colunas_numericas,coluna,chave)
        return componente_de_configuracao_do_grafico_box
    
    elif tipo_do_grafico == 'Linha':
        componente_de_configuracao_do_grafico_de_linha = ComponenteDeConfiguracaoDoGraficoDeLinha(colunas_numericas,coluna,chave)
        return componente_de_configuracao_do_grafico_de_linha

def retornar_criador_do_grafico(tipo_do_grafico,parametros,coluna,dataframe):
    if tipo_do_grafico == 'Dispersão':
        componente_de_criacao_do_grafico_de_dispersao = CriacaoDoGraficoDeDispersao(parametros[0],parametros[1],coluna,dataframe)
        return componente_de_criacao_do_grafico_de_dispersao
    
    elif tipo_do_grafico == 'Histograma':
        componente_de_criacao_do_grafico_de_histograma = CriacaoDoGraficoDeHistograma(parametros,coluna,dataframe)
        return componente_de_criacao_do_grafico_de_histograma
    
    elif tipo_do_grafico == 'Barras':
        componente_de_criacao_do_grafico_de_barras = CriacaoDoGraficoDeBarras(parametros,coluna,dataframe)
        return componente_de_criacao_do_grafico_de_barras
    
    elif tipo_do_grafico == 'BoxPlot':
        componente_de_criacao_do_grafico_box = CriacaoDoGraficoDeBox(parametros,coluna,dataframe)
        return componente_de_criacao_do_grafico_box
    
    elif tipo_do_grafico == 'Linha':
        componente_de_criacao_do_grafico_de_linha = CriadorDoGraficoDeLinha(parametros[0],parametros[1],coluna,dataframe)
        return componente_de_criacao_do_grafico_de_linha

def gerar_configuracoes_do_grafico(coluna,chave,colunas_numericas,colunas_categoricas,dataframe):
    componente_de_selecao_de_grafico = ComponenteSelecaoDeGrafico(coluna,chave)
    tipo_do_grafico = componente_de_selecao_de_grafico.visualizar_opcoes_grafico()
                                                                                     
    componente_de_configuracao_do_grafico = retornar_configuracoes_do_grafico_escolhido(tipo_do_grafico,coluna,colunas_numericas,colunas_categoricas,chave)
    parametros_do_grafico = componente_de_configuracao_do_grafico.visualizar_configuracoes_do_grafico()
    
    componente_de_criacao_do_grafico = retornar_criador_do_grafico(tipo_do_grafico,parametros_do_grafico,coluna,dataframe)
    componente_gerenciador_da_criacao_do_grafico = GerenciadorCriacaoDeGrafico(coluna,componente_de_criacao_do_grafico)
    
    componente_gerenciador_da_criacao_do_grafico.visualizar_grafico()

st.set_page_config(layout='wide')
st.header('Projeto de Bioinformática')

componente_arrasta_e_solta = ComponenteArrastaESolta()
arquivo_bruto = componente_arrasta_e_solta.visualizar_arrasta_e_solta()

if arquivo_bruto is not None :
    tipo_do_arquivo = identificar_tipo_do_arquivo(arquivo_bruto)
    criacao_do_dataframe = retornar_dataframe_pelo_tipo(tipo_do_arquivo,arquivo_bruto)
    dataframe = criacao_do_dataframe.retornar_dataframe()

    componente_selecao_de_funcao = ComponenteSelecaoDeFuncao()

    dataframe = dataframe.infer_objects()
    colunas_categoricas = list(dataframe.select_dtypes(['object']).columns)
    colunas_numericas = list(dataframe.select_dtypes(['float64','float32','int64','int32']).columns)
    
    opcao = componente_selecao_de_funcao.visualizar_opcoes()

    if opcao == 'Visualização dos dados':
        st.subheader('Visualização dos dados')
        componente_de_configuracao_do_dataframe = ComponenteDeConfiguracaoDoDataFrame(dataframe)
        componente_slider,componente_multiselect = componente_de_configuracao_do_dataframe.visualizar_configuracoes_do_dataframe()
        componente_gerenciador_da_criacao_do_dataframe = GerenciadorCriacaoDataFrame(dataframe,componente_slider,componente_multiselect)
        componente_gerenciador_da_criacao_do_dataframe.visualizar_dataframe()
    
    elif opcao == 'Análise':
        st.subheader('Análise dos dados')
        
        st.subheader('Análise Categórica')
        componente_de_criacao_da_analise_categorica = CriacaoAnaliseCategorica(dataframe)
        componente_gerenciador_da_criacao_da_analise_categorica = GerenciadorCriacaoAnalise(componente_de_criacao_da_analise_categorica)
        componente_gerenciador_da_criacao_da_analise_categorica.visualizar_analise()

        st.subheader('Análise Numérica')        
        componente_de_criacao_da_analise_numerica = CriacaoAnaliseNumerica(dataframe)
        componente_gerenciador_da_criacao_analise_numerica = GerenciadorCriacaoAnalise(componente_de_criacao_da_analise_numerica)
        componente_gerenciador_da_criacao_analise_numerica.visualizar_analise()

        st.subheader('Tabela de Contingência')
        componente_de_configuracao_da_tabela_de_contingencia = ComponenteDeConfiguracaoDaTabelaDeContingencia(colunas_categoricas,CHAVE_CONTINGENCIA)
        linha_contingencia,coluna_contingencia = componente_de_configuracao_da_tabela_de_contingencia.visualizar_configuracoes_tabela()
        componente_de_criacao_da_tabela_de_contingencia = CriacaoTabelaContingencia(linha_contingencia,coluna_contingencia,dataframe)
        componente_gerenciador_da_criacao_da_tabela_de_contingencia = GerenciadorCriacaoTabela(componente_de_criacao_da_tabela_de_contingencia,CHAVE_CONTINGENCIA[2])
        componente_gerenciador_da_criacao_da_tabela_de_contingencia.visualizar_tabela()

        st.subheader('Tabela de Repetição de frequência')
        componente_de_configuracao_da_tabela_trf = ComponenteDeConfiguracaoDaTabelaDeRepeticaoFrequencia(colunas_categoricas,CHAVE_TRF)
        coluna_trf = componente_de_configuracao_da_tabela_trf.visualizar_configuracoes_tabela()
        componente_de_criacao_da_tabela_trf = CriacaoTabelaRepeticaoFrequencia(dataframe,coluna_trf) 
        componente_gerenciador_da_criacao_da_tabela_trf = GerenciadorCriacaoTabela(componente_de_criacao_da_tabela_trf,CHAVE_TRF[1])
        componente_gerenciador_da_criacao_da_tabela_trf.visualizar_tabela()
    

    elif opcao == 'Criação de gráficos':
        st.subheader('Criação dos dados')

        col1,col2 = st.beta_columns(2)
        col3,col4 = st.beta_columns(2)

        gerar_configuracoes_do_grafico(col1,CHAVE_COLUNA_1,colunas_numericas,colunas_categoricas,dataframe)
        gerar_configuracoes_do_grafico(col2,CHAVE_COLUNA_2,colunas_numericas,colunas_categoricas,dataframe)
        gerar_configuracoes_do_grafico(col3,CHAVE_COLUNA_3,colunas_numericas,colunas_categoricas,dataframe)
        gerar_configuracoes_do_grafico(col4,CHAVE_COLUNA_4,colunas_numericas,colunas_categoricas,dataframe)